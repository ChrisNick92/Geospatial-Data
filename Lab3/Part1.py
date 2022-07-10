# %%
import os
import rasterio
import numpy as np
import torch
import torch.nn as nn
import lib
from torch.utils.data import DataLoader
from sklearn.metrics import classification_report

training_path = os.path.join(os.getcwd(),"HyRANK_satellite", "TrainingSet")

# Here need to display the RGB images of Dioni & Loukia

# Reading the tif files first
dioni_train = rasterio.open(os.path.join(training_path,"Dioni.tif"))
dioni_val = rasterio.open(os.path.join(training_path,"Dioni_GT.tif"))
loukia_train = rasterio.open(os.path.join(training_path,"Loukia.tif"))
loukia_val = rasterio.open(os.path.join(training_path,"Loukia_GT.tif"))

# Preparing the dataset
X,y = lib.np_data_transformer(dioni_train, dioni_val)
X_test, y_test = lib.np_data_transformer(loukia_train, loukia_val)

# %% Testing some classic ML classifiers

target_names = np.array(['Dense Urban Fabric', 'Mineral Extraction Sites', 'Non Irrigated Arable Land',
               'Fruit Trees', 'Olive Groves', 'Broad-leaved Forest', 'Coniferous Forest',
               'Mixed Forest', 'Dense Sclerophyllous Vegetation', 'Sparce Scerophyllous Vegetation',
               'Sparcely Vegetated Areas', 'Rocks and Sand', 'Water', 'Coastal Water'])
random_state = 42

from sklearn.ensemble import RandomForestClassifier
clf_forest = RandomForestClassifier(max_depth = 16, random_state = random_state)
clf_forest.fit(X, y)
preds = clf_forest.predict(X_test)
print(classification_report(y_test, preds, target_names = target_names))

# %% MLP classifier
# Check if cuda is available
if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"


# Train - test - val loaders
batch_size = 64
epochs = 200
lr = 1e-5
loss_fn = nn.CrossEntropyLoss().to(device)

train_set = lib.MLP_Dataset(X, y)
portion = int(0.8*len(train_set)) # 80 % for train, 20 % for validation
train_set, val_set = torch.utils.data.random_split(train_set,
                                                  [portion, len(train_set)-portion])
train_dloader = DataLoader(train_set, batch_size = batch_size,
                          shuffle = True)
val_dloader = DataLoader(val_set, batch_size = batch_size)
test_set = lib.MLP_Dataset(X_test,y_test)
test_dloader = DataLoader(test_set, batch_size = batch_size)

in_features = dioni_train.count
out_features = len(target_names)
model = lib.MLP_Net(in_features = in_features, out_features = out_features,
               layers = [512, 256, 128]).to(device)


# %% Training loop of MLP
lib.training_loop(model, train_dloader, val_dloader, epochs = epochs,
             lr = lr, batch_size = batch_size, loss_fn = loss_fn,
             regularization = 'L2', reg_lambda = 1e-1)

# %% Evaluation of MLP
preds, targets = lib.test_loop(model, test_dloader, device = 'cuda')
print(classification_report(targets, preds, target_names=target_names))