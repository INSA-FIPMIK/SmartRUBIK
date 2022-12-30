import torch
import numpy as np
import pandas as pd

class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data
        '''Conversion de la rubik_str et mvt_choisi en variables numeriques 0<x<1
        blanc = 0
        rouge = 0.2
        vert = 0.4
        jaune = 0.6
        orange = 0.8
        bleu = 1
        '''
        self.pos2float = {
            "w": 0,
            "r": 0.2,
            "g": 0.4,
            "y": 0.6,
            "o": 0.8,
            "b": 1
        }
        # conversion move to target number
        self.mv2float = {
            "U0": 0,
            "D0": 1,
            "F0": 2,
            "B0": 3,
            "R0": 4,
            "L0": 5,
            "U1": 6,
            "D1": 7,
            "F1": 8,
            "B1": 9,
            "R1": 10,
            "L1": 11,
            "U2": 12,
            "D2": 13,
            "F2": 14,
            "B2": 15,
            "R2": 16,
            "L2": 17,
        }

    def __getitem__(self, idx):
        item = self.preprocess(self.data.iloc[idx])
        return item

    def __len__(self):
        return len(self.data)

    def preprocess(self, data):
        data_dict = {}
        rubik_str = data['rbk_str']
        rubik_str = [self.pos2float[elmt] for elmt in rubik_str]
        data_dict['rubik_str'] = torch.Tensor(rubik_str).float()
        
        target = data['mvt']
        target = [self.mv2float[elmt] for elmt in target.split()]
        # only take first move as target
        data_dict['target'] = target[0]
        return data_dict