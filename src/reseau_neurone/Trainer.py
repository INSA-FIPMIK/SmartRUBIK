import torch
import torch.optim as optim
import torch.nn.functional as F

from src.Net import Net

class Trainer ():
    def __init__(self, use_cuda):

        if use_cuda:
            self.device = torch.device("cuda")
        else:
            self.device = torch.device("cpu")
            
        self.model = Net().to(self.device)
        
        self.optimizer = optim.Adadelta(self.model.parameters(), lr=1.0)
        self.epoch = 0
        self.test_loss = 0
        
    def training_epochs (self, train_loader,epoch):
        self.model.train()

        for batch_idx, train_batch in enumerate(train_loader):
            self.optimizer.zero_grad()
            data, target = train_batch['rubik_str'].to(self.device), train_batch['mvt'].to(self.device)
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
                data, target = test_batch['image'].to(self.device), test_batch['label'].to(self.device)
                output = self.model(data.flatten(1))
                self.test_loss += F.nll_loss(output, target, reduction='sum').item()  # sum up batch loss
                pred = output.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
                correct += pred.eq(target.view_as(pred)).sum().item()

        self.test_loss /= len(test_loader.dataset)

        print(f"\nTest set: Average loss: {self.test_loss:.4f}, Accuracy: {correct}/{len(test_loader.dataset)}" \
              f"({100. * correct / len(test_loader.dataset):.0f}%)\n")


    
    def fit (self, train_loader, test_loader):
        a = train_loader
        
        
        
    def predict (self, predict_loader):
        a = predict_loader 