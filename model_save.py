import torch
import torch.nn as nn
import torch.optim as optim

PATH = "best_s_6classes.pt"

# Load
model = torch.load(PATH)

