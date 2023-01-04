import time

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.utils.rnn import pad_sequence
from transformers import BartConfig, BartForConditionalGeneration

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.config = BartConfig()
        self.config.max_position_embeddings = 256
        self.config.vocab_size = 27
        self.config.encoder_ffn_dim = 512
        self.config.encoder_layers = 6
        self.config.decoder_ffn_dim = 512
        self.config.decoder_layers = 6
        self.config.pad_token_id = 26
        self.config.eos_token_id = 25
        self.config.bos_token_id = 24
        self.config.d_model = 256
        self.tf = BartForConditionalGeneration(self.config)
        print(self.tf)
        def count_parameters(model):
            return sum(p.numel() for p in model.parameters() if p.requires_grad)
        print(f"Number of trainable parameters: {count_parameters(self.tf)}")

    def forward(self, x, y=None):
        attention_mask = x != self.config.pad_token_id
        outputs = self.tf(
            input_ids=x,
            attention_mask=attention_mask,
            labels=y
        )
        return outputs
