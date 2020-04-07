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
    Random CNN (similar used for chess), not working, need to try some other options
    TODO: Try with RL, TD, NEAT (neuroevolution) ...
    """

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(32, 16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(16, 16, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(16, 32, kernel_size=3, stride=2)

        self.conv4 = nn.Conv2d(32, 32, kernel_size=3, padding=1)
        self.conv5 = nn.Conv2d(32, 32, kernel_size=3, padding=1)
        self.conv6 = nn.Conv2d(32, 64, kernel_size=3, stride=2)

        self.conv7 = nn.Conv2d(64, 64, kernel_size=2, padding=1)
        self.conv8 = nn.Conv2d(64, 64, kernel_size=2, padding=1)
        self.conv9 = nn.Conv2d(64, 128, kernel_size=2, stride=2)

        self.conv10 = nn.Conv2d(128, 128, kernel_size=1)
        self.conv11 = nn.Conv2d(128, 128, kernel_size=1)
        self.conv12 = nn.Conv2d(128, 128, kernel_size=1)
        self.last = nn.Linear(128, 1)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))

        x = F.relu(self.conv4(x))
        x = F.relu(self.conv5(x))
        x = F.relu(self.conv6(x))

        x = F.relu(self.conv7(x))
        x = F.relu(self.conv8(x))
        x = F.relu(self.conv9(x))

        x = F.relu(self.conv10(x))
        x = F.relu(self.conv11(x))
        x = F.relu(self.conv12(x))

        x = x.view(-1, 128)
        x = self.last(x)

        return F.tanh(x)













