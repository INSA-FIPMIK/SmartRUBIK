from __future__ import print_function
import argparse
import numpy as np
import torch
from torchvision import datasets, transforms
from torch.optim.lr_scheduler import StepLR
import pandas as pd
import torch.optim as optim
from src.Custom_dataset import CustomDataset
from src.Trainer import Trainer
from src.Net import Net

#------------- Ce programme vise a resoudre le rubik s cube via un reseau de neuronne-------------------

def reseau_neurone (dataset1, dataset2):
    
    use_cuda = torch.cuda.is_available()
    torch.manual_seed(0)
    
    train_loader = torch.utils.data.DataLoader(CustomDataset(dataset1), **train_kwargs)
    test_loader = torch.utils.data.DataLoader(CustomDataset(dataset2), **test_kwargs)
    
    training = Trainer(use_cuda)

    scheduler = StepLR(training.optimizer, step_size=1, gamma=0.7)
    
    old_loss = 100
    
    for epoch in range(1, 2):
        training.training_epochs(train_loader, epoch)
        training.test(test_loader)
        scheduler.step()
        if training.test_loss < old_loss :
            old_loss = training.test_loss
            print("saving model....")
            torch.save(training.model.state_dict(), "./models/mnist.pt")
            
def split(dataset):
    '''Procedure permettant de spliter le Dataset
    Split du Dataset a 70% pour le training et 30% pour le test'''

    nb_dataset_train = int(dataset.shape[0] * 0.7)
    nb_dataset_test = int(dataset.shape[0] - nb_dataset_train)

    dataset1 = pd.read_csv('../../data/Creation_Data/Data.csv', header = nb_dataset_train)
    dataset2 = pd.read_csv('../../data/Creation_Data/Data.csv', header = nb_dataset_test)

    print("Definition du dataset d entree :\n   Shape of training: ", dataset1.shape, "\n   Shape of test: ", dataset2.shape, "\n")

    return dataset1, dataset2

            
def main():
    
    use_cuda = torch.cuda.is_available()
    torch.manual_seed(0)
    
    if use_cuda:
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")

    
    use_cuda = torch.cuda.is_available()
    train_kwargs = {'batch_size': 64}
    test_kwargs = {'batch_size': 4096}
    if use_cuda:
        cuda_kwargs = {'num_workers': 1,
                       'pin_memory': True,
                       'shuffle': True}
        train_kwargs.update(cuda_kwargs)
        test_kwargs.update(cuda_kwargs)

    dataset = pd.read_csv('../../data/Creation_Data/Data.csv')
    
    dataset1, dataset2 = split(dataset)
    
    train_loader = torch.utils.data.DataLoader(
        CustomDataset(dataset1),
        **train_kwargs
    )
    test_loader = torch.utils.data.DataLoader(
        CustomDataset(dataset2),
        **test_kwargs
    )
    
    model = Net().to(device)
    optimizer = optim.Adadelta(model.parameters(), lr=1.0)
    scheduler = StepLR(optimizer, step_size=1, gamma=0.7)
    
    trainer = Trainer(use_cuda)

    for epoch in range(1, 10):
        trainer.training_epochs( train_loader, epoch)
        trainer.test(test_loader)
        scheduler.step()

    torch.save(model.state_dict(), "'../../data/reseau_neuronne/res.pt'")

    
     
            
if __name__ == '__main__':
    main()