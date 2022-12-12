from __future__ import print_function
import argparse
import numpy as np
import torch
from torchvision import datasets, transforms
from torch.optim.lr_scheduler import StepLR
import pandas as pd

from src.Custom_dataset import CustomDataset
from src.Trainer import Trainer

#------------- Ce programme vise a resoudre le rubik s cube via un reseau de neuronne-------------------



def main():
    use_cuda = torch.cuda.is_available()
    torch.manual_seed(0)
    
    train_kwargs = {'batch_size': 10}
    test_kwargs = {'batch_size': 5}
    if use_cuda:
        cuda_kwargs = {'num_workers': 1,
                       'pin_memory': True,
                       'shuffle': True}
        train_kwargs.update(cuda_kwargs)
        test_kwargs.update(cuda_kwargs)

    dataset = pd.read_csv('/menu/app/Projet_Rubik_cube/data/Creation_Data/Data.csv')
    
    #Split du Dataset a 70% pour le training et 30% pour le test
    nb_dataset_train = int(dataset.shape[0] * 0.7)
    nb_dataset_test = int(dataset.shape[0] - nb_dataset_train)
    
    dataset1 = pd.read_csv('/menu/app/Projet_Rubik_cube/data/Creation_Data/Data.csv', header = nb_dataset_train)
    dataset2 = pd.read_csv('/menu/app/Projet_Rubik_cube/data/Creation_Data/Data.csv', header = nb_dataset_test)
    
    x_train = dataset1.iloc[:,1]
    y_train = dataset1.iloc[:,2]
    x_test = dataset2.iloc[:,1]
    y_train = dataset2.iloc[:,2]
    
    print("Definition du dataset d entree :\n   Shape of training: ", x_train.shape, "\n   Shape of test: ", x_test.shape, "\n")
    
    train_loader = torch.utils.data.DataLoader(
        CustomDataset(dataset1),
        **train_kwargs
    )
    test_loader = torch.utils.data.DataLoader(
        CustomDataset(dataset2),
        **test_kwargs
    )

    training = Trainer(use_cuda)

    scheduler = StepLR(training.optimizer, step_size=1, gamma=0.7)
    
    old_loss = 100

""" 
    for epoch in range(1, 2):
        training.training_epochs(train_loader, epoch)
        training.test(test_loader)
        scheduler.step()
        if training.test_loss < old_loss :
            old_loss = training.test_loss
            print("saving model....")
            torch.save(training.model.state_dict(), "./models/mnist.pt")
"""
            
            
if __name__ == '__main__':
    main()