import torch
import torch.nn as nn
from torchviz import make_dot
from torch.autograd import Variable
import numpy as np
import matplotlib.pyplot as plt

print(torch.__version__)

model = nn.Sequential()
model.add_module("W0", nn.Linear(8, 16))
model.add_module("tanh", nn.Tanh())
model.add_module("W1", nn.Linear(16, 1))

x = Variable(torch.randn(1, 8))
y = model(x)

make_dot(y.mean(), params=dict(model.named_parameters()), show_saved=True)
