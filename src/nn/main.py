from __future__ import print_function
import argparse
import glob
import os
import random

import numpy as np
import torch
from torchvision import datasets, transforms
from torch.optim.lr_scheduler import StepLR
import pandas as pd
import torch.optim as optim
from sklearn.model_selection import train_test_split

from nn.preprocess.custom_dataset import CustomDataset
from nn.trainer import Trainer
from nn.models.model import Net

random.seed(0)
np.random.seed(0)
torch.manual_seed(0)

#------------- Ce programme vise a resoudre le rubik s cube via un reseau de neuronne-------------------


def split():
    path = '../../data/generated_data/'
    all_files = glob.glob(os.path.join(path , "*.csv"))
    li = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)
    dataset = pd.concat(li, axis=0, ignore_index=True)
    dataset = dataset.drop_duplicates()

    train, test = train_test_split(dataset, test_size=0.2, shuffle=True)
    print(f"Train set: size = {len(train)}")
    print(f"Test set: size = {len(test)}")
    return train, test


def main():
    num_epochs = 40
    
    #configuration Pytorch (utilisation GPU si possible)
    use_cuda = torch.cuda.is_available()
    torch.manual_seed(0)
    use_cuda = torch.cuda.is_available()
    if use_cuda:
        device = torch.device("cuda")
    else:
        device = torch.device("cpu") 
    print(f"Using device: {device}")
    
    
    #Configuration Data / Preprocessing
    train_kwargs = {'batch_size': 128}
    test_kwargs = {'batch_size': 4096}
    
    if use_cuda:
        cuda_kwargs = {'num_workers': 1,
                       'pin_memory': True,
                       'shuffle': True}
        
        train_kwargs.update(cuda_kwargs)
        test_kwargs.update(cuda_kwargs)
        
    load_from_checkpoint='../../models/nn2.pt'

    model = Net().to(device)
    optimizer = optim.Adam(model.parameters(), lr=2e-4)
    scheduler = StepLR(optimizer, step_size=1, gamma=1)
    trainer = Trainer(
        model,
        optimizer,
        scheduler,
        num_epochs,
        device,
        load_from_checkpoint='../../models/nn2.pt'
    )
    
    
    if os.path.exists(load_from_checkpoint) == False :
        prin("daccord")
        dataset1, dataset2 = split()

        train_loader = torch.utils.data.DataLoader(
            CustomDataset(dataset1, predict_or_train = 0),
            **train_kwargs
        )
        test_loader = torch.utils.data.DataLoader(
            CustomDataset(dataset2,  predict_or_train = 0),
            **test_kwargs
        )

        #Training
        trainer.fit(train_loader, test_loader)

        
        
    #Prediction
    rubik_str = pd.read_csv('../../data/generated_data/prediction.csv')
    customprediction = CustomDataset(rubik_str,  predict_or_train = 1)

    predict_loader = torch.utils.data.DataLoader(
        CustomDataset(rubik_str,  predict_or_train = 1),
        **test_kwargs
    )
    trainer.predict(predict_loader)
       
     
            
if __name__ == '__main__':
    main()
