import numpy as np

import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset


class CheckersDataset(Dataset):
    """
    Checkers dataset -> http://www.fierz.ch/download.php
    About 20_000 games
    """

    def __init__(self):
        data = np.load('data/processed.npz')
        self.x = data['arr_0']
        self.y = data['arr_1']

    def __len__(self):
        return self.x.shape[0]

    def __getitem__(self, index):
        return self.x[index], self.y[index]


class Net(nn.Module):
    """
    TODO: Try with RL, TD, NEAT (neuroevolution) ...
    """

    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(32, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 128)
        self.fc4 = nn.Linear(128, 128)
        self.fc5 = nn.Linear(128, 256)
        self.fc6 = nn.Linear(256, 256)
        self.last = nn.Linear(256, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        x = F.relu(self.fc5(x))
        x = F.relu(self.fc6(x))

        x = x.view(-1, 256)
        x = self.last(x)

        return F.tanh(x)
