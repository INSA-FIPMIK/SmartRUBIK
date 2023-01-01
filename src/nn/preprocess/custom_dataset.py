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
            "r": 1,
            "g": 2,
            "y": 3,
            "o": 4,
            "b": 5
        }
        # conversion move to target number
        self.mv2float = {
            "U0": 6,
            "D0": 7,
            "F0": 8,
            "B0": 9,
            "R0": 10,
            "L0": 11,
            "U1": 12,
            "D1": 13,
            "F1": 14,
            "B1": 15,
            "R1": 16,
            "L1": 17,
            "U2": 18,
            "D2": 19,
            "F2": 20,
            "B2": 21,
            "R2": 22,
            "L2": 23,
        }

    def __getitem__(self, idx):
        item = self.preprocess(self.data.iloc[idx])
        return item

    def __len__(self):
        return len(self.data)

    def preprocess(self, data):
        data_dict = {}
        rubik_str = data['rbk_str']
        rubik_str = [24] + [self.pos2float[elmt] for elmt in rubik_str]
        rubik_str += [26] * (100 - len(rubik_str))
        data_dict['rubik_str'] = torch.Tensor(rubik_str).long()
        
        target = data['mvt']
        target = [24] + [self.mv2float[elmt] for elmt in target.split()]
        target += [-100] * (100 - len(target))
        # only take first move as target
        #data_dict['target'] = target[0]
        data_dict['target'] = torch.Tensor(target).long()
        return data_dict