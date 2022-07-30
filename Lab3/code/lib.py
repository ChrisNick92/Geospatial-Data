import numpy as np
import matplotlib.pyplot as plt
from torch.optim import Adam
import seaborn as sns

# Normalizing images
def normalize(band):
    return (band - band.min()) / (band.max() - band.min())

# A function to visualize the RGB images
def display_rgb(tiff_file, image_name, rgb = (23,11,7)):
    image = np.dstack((normalize(tiff_file.read(rgb[0])),
                       normalize(tiff_file.read(rgb[1])),
                       normalize(tiff_file.read(rgb[2]))))
    fig, ax = plt.subplots(figsize = (15,10))
    ax.imshow(image)
    ax.set_title("RGB Image of " + image_name, fontsize = 15)
    plt.show()

# Data transformer for ML classifier & MLP
def np_data_transformer(raster_features, raster_labels, norm = True):
    """
    :param raster_features: The raster of features
    :param raster_labels: The raster of ground truth labels
    :return: Return features X (num samples x num features), Return labels y, (num samples x 1)
    """
    num_bands = raster_features.count  # Total number of bands
    width = raster_features.width
    height = raster_features.height
    X = np.zeros(shape=(width * height, num_bands))  # X -> Features
    y = raster_labels.read(1).flatten()  # y -> labels
    for band in range(num_bands):
        X[:, band] = raster_features.read(band + 1).flatten()
    # dropping rows that correspond to label with value 0
    mask = (y != 0)
    X,y = X[mask,:], y[mask]
    if norm:
        X = (X - X.min(axis = 0))/(X.max(axis = 0) - X.min(axis = 0))
    return X,y

# MLP Architecture

import torch
from torch import nn
from collections import OrderedDict
from torch.utils.data import Dataset

# The dataset class for the MLP
class MLP_Dataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.from_numpy(X).type(torch.float32)
        self.y = torch.from_numpy(y).type(torch.LongTensor) - 1

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return self.X[idx, :], self.y[idx]

# The Architecture
class MLP_Net(nn.Module):
    def __init__(self, in_features, out_features, layers=[10]):
        super(MLP_Net, self).__init__()
        num_layers = [in_features] + layers
        self.structure = OrderedDict()

        # Main Architecture
        for i, layer in enumerate(num_layers[:-1]):
            self.structure['linear' + str(i + 1)] = nn.Linear(num_layers[i], num_layers[i + 1])
            self.structure['BatchNorm' + str(i + 1)] = nn.BatchNorm1d(num_layers[i + 1])
            self.structure['ReLU' + str(i + 1)] = nn.ReLU()
            self.structure['Dropout' + str(i + 1)] = nn.Dropout(p=0.3)

        self.structure['linear' + str(i + 2)] = nn.Linear(num_layers[i + 1], out_features)
        self.linear_relu_stack = nn.Sequential(self.structure)

    def forward(self, x):
        return self.linear_relu_stack(x)

# Training loop

def training_loop(model, train_loader, val_loader, epochs,
                  lr, batch_size, loss_fn, regularization=None,
                  reg_lambda=None, mod_epochs=20):
    optim = Adam(model.parameters(), lr=lr)
    if torch.cuda.is_available():
        device = "cuda"
    else:
        device = "cpu"

    train_loss_list = []
    val_loss_list = []
    num_train_batches = len(train_loader)
    num_val_batches = len(val_loader)

    for epoch in range(epochs):
        model.train()
        train_loss, val_loss = 0.0, 0.0
        for train_batch in train_loader:
            X, y = train_batch[0].to(device), train_batch[1].to(device)
            preds = model(X)
            loss = loss_fn(preds, y)
            train_loss += loss.item()

            # Regulirization
            if regularization == 'L2':
                l_norm = sum(p.pow(2.0).sum() for p in model.parameters())
                loss = loss + reg_lambda * l_norm
            elif regularization == 'L1':
                l_norm = sum(p.abs().sum() for p in model.parameters())
                loss = loss + reg_lambda * l_norm

            # Backpropagation
            optim.zero_grad()
            loss.backward()
            optim.step()
        model.eval()
        with torch.no_grad():
            for val_batch in val_loader:
                X, y = val_batch[0].to(device), val_batch[1].to(device)
                preds = model(X)
                val_loss += loss_fn(preds, y).item()
        train_loss /= num_train_batches
        val_loss /= num_val_batches
        train_loss_list.append(train_loss)
        val_loss_list.append(val_loss)
        if (epoch + 1) % mod_epochs == 0:
            print(
                f"Epoch: {epoch + 1}/{epochs}{5 * ' '}Training Loss: {train_loss:.4f}{5 * ' '}Validation Loss: {val_loss:.4f}")

    fig, ax = plt.subplots(figsize=(8, 8))
    sns.set_style("dark")
    ax.plot(range(1, epochs + 1), train_loss_list, label='Train Loss')
    ax.plot(range(1, epochs + 1), val_loss_list, label='Val Loss')
    ax.set_title("Train - Val Loss")
    ax.set_xlabel("Loss")
    ax.set_ylabel("Epochs")
    plt.legend()
    plt.show()


def test_loop(model, test_dloader, device='cpu'):
    predictions_list = np.array([], dtype=np.int64)
    targets_list = np.array([], dtype=np.int64)
    model.eval()

    for val_sample in test_dloader:
        X = val_sample[0].to(device)
        y = val_sample[1].cpu().numpy()
        targets_list = np.concatenate((targets_list, y))

        with torch.no_grad():
            preds = model(X)
            predictions_list = np.concatenate((predictions_list,
                                               torch.argmax(preds, dim=-1).cpu().numpy()))

    return predictions_list, targets_list



