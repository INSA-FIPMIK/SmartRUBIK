import torch
import numpy as np

class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data

    def __getitem__(self, idx):
        item = self.preprocess(self.data[idx])
        return item

    def __len__(self):
        return len(self.data)

    def preprocess(self, data):
        data_dict = {}
        data_dict['image'] = torch.Tensor(np.array(data[0])).float()
        data_dict['label'] = data[1]
        data_dict['image']  = data_dict['image'] / 255 # Avoir une loi normale centrée réduite cad valeurs comprise entre 0 et 1
        #print(data_dict)
        return data_dict