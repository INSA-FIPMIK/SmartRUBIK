import torch
import numpy as np
import pandas as pd

class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data

    def __getitem__(self, idx):
        item = self.preprocess(self.data[idx])
        return item

    def __len__(self):
        return len(self.data)

    def preprocess(self, data):
        '''Conversion de la rubik_str et mvt_choisi en variables numeriques 0<x<1
        blanc = 0
        rouge = 0.2
        vert = 0.4
        jaune = 0.6
        orange = 0.8
        bleu = 1
        '''
        
        data_dict = {}
        rubik_str = data.iloc[0]
        rubik_str = rubik_str.replace("w", "0")
        rubik_str = rubik_str.replace("r", "0.2")
        rubik_str = rubik_str.replace("g", "0.4")
        rubik_str = rubik_str.replace("y", "0.6")
        rubik_str = rubik_str.replace("o", "0.8")
        rubik_str = rubik_str.replace("b", "1")
        
        data_dict['rubik_str'] = torch.Tensor(pd.array(data[0])).float()
        
        target = data.iloc[1]
        target = target.replace('U0','0')
        target = target.replace('D0','1')
        target = target.replace('F0','2')
        target = target.replace('B0','3')
        target = target.replace('R0','4')
        target = target.replace('L0','5')

        target = target.replace('U1','6')
        target = target.replace('D1','7')
        target = target.replace('F1','8')
        target = target.replace('B1','9')
        target = target.replace('R1','10')
        target = target.replace('L1','11')

        target = target.replace('U2','12')
        target = target.replace('D2','13')
        target = target.replace('F2','14')
        target = target.replace('B2','15')
        target = target.replace('R2','16')
        target = target.replace('L2','17')
        
        
        data_dict['target'] = data[1]
        return data_dict