import os

import torch
import torch.optim as optim
import torch.nn.functional as F

from models.model import Net
from preprocess.custom_dataset import CustomDataset


class Trainer ():
    def __init__(self, model, optimizer, scheduler, num_epochs, device, load_from_checkpoint=None):
        self.model = model
        if load_from_checkpoint:
            if os.path.isfile(load_from_checkpoint):
                print("Loading checkpoint...")
                self.model.load_state_dict(torch.load(load_from_checkpoint))
        self.optimizer = optimizer
        self.scheduler = scheduler
        self.num_epochs = num_epochs
        self.device = device
        self.model.to(self.device)
        self.min_val_loss = 100
        self.test_loss = 0
        self.vocab_size = 27
        
    def training_epochs (self, epoch, train_loader):
        self.model.train()
        for batch_idx, train_batch in enumerate(train_loader):
            self.optimizer.zero_grad()
            data, target = train_batch['rubik_str'].to(self.device), train_batch['target'].to(self.device)
            outputs = self.model(data.flatten(1), target)
            loss = outputs.loss
            loss.backward()
            if batch_idx % 100 == 0:
                print(f"Train Epoch: {epoch} [{batch_idx * len(data)}/{len(train_loader.dataset)}" \
                      f"({100. * batch_idx / len(train_loader):.0f}%)]\tLoss: {loss.item():.6f}")
            self.optimizer.step()
    
    def test(self, test_loader):
        self.model.eval()
        correct_elmts = 0
        correct_seqs = 0
        total_elmts = 0
        total_seqs = 0
        with torch.no_grad():
            for test_batch in test_loader:
                data, target = test_batch['rubik_str'].to(self.device), test_batch['target'].to(self.device)
                outputs = self.model(data.flatten(1), target)
                self.test_loss += F.cross_entropy(outputs.logits.view(-1, self.vocab_size), target.view(-1), reduction='sum').item()  # sum up batch loss
                # calcul du nombre de bon mouvements sur l'ensemble des séquences de résolutions
                pred = outputs.logits.argmax(dim=-1)# get the index of the max log-probability
                correct_elmts += (pred == target).sum()
                total_elmts += len(torch.where(target != -100)[0])
                # calcul du nombre de séquences de résolution entièrement correctes
                pred[torch.where(target == -100)] = -100
                correct_seqs += ((pred == target).sum(dim=-1) == pred.size(-1)).sum()
                total_seqs += len(target)
        self.test_loss /= total_elmts

        print(f"\nTest set: Average loss: {self.test_loss:.4f}, " \
            f"Pred. Accuracy: {correct_elmts}/{total_elmts}: {correct_elmts / total_elmts * 100:.2f}%, " \
            f"Seq. Accuracy: {correct_seqs}/{total_seqs}: {correct_seqs / total_seqs * 100:.2f}%\n")

        if self.test_loss < self.min_val_loss:
            print("Saving model...")
            torch.save(self.model.state_dict(), '../../models/nn2.pt')
            self.min_val_loss = self.test_loss
    
    def fit (self, train_loader, test_loader):
        for epoch in range(1, self.num_epochs):
            self.training_epochs(epoch, train_loader)
            self.test(test_loader)
            self.scheduler.step()
     
    def predict (self, predict_loader):
        self.model.eval()
        with torch.no_grad():
            for predict_batch in predict_loader:
                data = predict_batch['rubik_str'].to(self.device)
                output = self.model(data).logits.argmax(dim=-1)
                output = output.cpu().numpy().tolist()
                       
                float2mov = {
                    6:"U",
                    7:"D",
                    8:"F",
                    9:"B",
                    10:"R",
                    11:"L",
                    12:"u",
                    13:"d",
                    14:"f",
                    15:"b",
                    16:"r",
                    17:"l",
                    18:"uu",
                    19:"dd",
                    20:"ff",
                    21:"bb",
                    22:"rr",
                    23:"ll",
                }
                
                for i in range (len(output)):
                    mouvement = [float2mov[elmt] for elmt in output[i] if elmt>5 and elmt<24]
                print("Prediction", mouvement)
        return mouvement