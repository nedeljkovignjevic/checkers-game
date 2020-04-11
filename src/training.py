from torch.utils.data import DataLoader
from torch import nn
from torch import optim

from src.neural_network import Net, CheckersDataset


def train():
    device = 'cuda'
    dataset = CheckersDataset()
    train_loader = DataLoader(dataset, batch_size=128, shuffle=True)

    model = Net()
    optimizer = optim.Adam(model.parameters())
    f_loss = nn.MSELoss()

    model.cuda()
    model.train()

    for epoch in range(5):
        all_loss = 0
        n_loss = 0
        for data, target in train_loader:
            target = target.unsqueeze(-1)
            data, target = data.to(device), target.to(device)
            data, target = data.float(), target.float()

            optimizer.zero_grad()
            output = model(data)

            loss = f_loss(output, target)
            loss.backward()
            optimizer.step()

            all_loss += loss.item()
            n_loss += 1

        print(f'{epoch} {all_loss / n_loss}')

