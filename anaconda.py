import numpy as np
import matplotlib.pyplot as plt
X_train=np.array([1.0,2.0])
Y_train=np.array([300.0,500.0])
print(f"X.shape :{X_train.shape[0]}")
m=len(X_train)
print(f"Length of X_train is {m}")
print()
i=1
print(f"(x^{i} , y^{i}) : ({X_train[i]}, {Y_train[i]})")
# plt.scatter(X_train, Y_train, marker='x', c='r')
f_wb= np.zeros(m)
print(f_wb)

