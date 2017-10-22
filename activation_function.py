import matplotlib.pyplot as plt
import numpy as np

def sigmoid(x):
    y = 1 / (1 + np.exp(-x))
    return y

def relu(x):
    y = x * (x > 0)
    return y

def softmax(x):
    x_exp = [np.exp(i) for i in x]
    sum_x_exp = sum(x_exp)
    y = [round(i / sum_x_exp, 3) for i in x_exp]
    return y
    
x = np.arange(-10,10,0.2)
y = softmax(x)

plt.plot(x, y)
plt.show()