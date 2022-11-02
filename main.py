# imports 
import os
import torch
import torchvision
import pandas as pd
import torch.nn as nn
import torch.nn.functional as F
from tqdm.notebook import tqdm
import torchvision.models as models
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torch.utils.data import random_split
from torchvision.utils import make_grid
import torchvision.transforms as transforms
from torchvision.datasets.folder import default_loader
import matplotlib.pyplot as plt

# hyperparams
image_size = (64,64)
batch_size = 128
stats = (0.5, 0.5, 0.5), (0.5, 0.5, 0.5)

# TODO: preprocess data

# TODO: init model

# TODO: train model

# TODO