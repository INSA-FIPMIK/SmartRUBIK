import torch
import torch.optim as optim
import torch.nn.functional as F

from models.model import Net

class Trainer ():
    def __init__(self, model, optimizer, scheduler, num_epochs, device, load_from_checkpoint=None):
        self.model = model
        if load_from_checkpoint:
            print("Loading checkpoint...")
            self.model.load_state_dict(torch.load(load_from_checkpoint))
        self.optimizer = optimizer
        self.scheduler = scheduler
        self.num_epochs = num_epochs
        self.device = device
        self.model.to(self.device)
        self.min_val_loss = 100
        self.test_loss = 0
        
    def training_epochs (self, epoch, train_loader):
        self.model.train()
        for batch_idx, train_batch in enumerate(train_loader):
            self.optimizer.zero_grad()
            data, target = train_batch['rubik_str'].to(self.device), train_batch['target'].to(self.device)
            output = self.model(data.flatten(1))
            loss = F.nll_loss(output, target) #loss est un torch.Tensor
            loss.backward()
            if batch_idx % 10 == 0:
                print(f"Train Epoch: {epoch} [{batch_idx * len(data)}/{len(train_loader.dataset)}" \
                      f"({100. * batch_idx / len(train_loader):.0f}%)]\tLoss: {loss.item():.6f}")
            self.optimizer.step()
    
    
    def test (self, test_loader):
        self.model.eval()
        correct = 0
        with torch.no_grad():
            for test_batch in test_loader:
                data, target = test_batch['rubik_str'].to(self.device), test_batch['target'].to(self.device)
                output = self.model(data.flatten(1))
                self.test_loss += F.nll_loss(output, target, reduction='sum').item()  # sum up batch loss
                pred = output.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
                correct += pred.eq(target.view_as(pred)).sum().item()

        self.test_loss /= len(test_loader.dataset)

        print(f"\nTest set: Average loss: {self.test_loss:.4f}, Accuracy: {correct}/{len(test_loader.dataset)}" \
              f"({100. * correct / len(test_loader.dataset):.0f}%)\n")
    
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
                output = torch.exp(self.model(data.flatten(1)))
                print("Probas: ", output)
                output = output.argmax(dim=1, keepdim=True)
                print("Prediction: ", output)