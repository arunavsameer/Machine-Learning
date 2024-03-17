import numpy as np
import matplotlib.pyplot as plt

def z_score_normalize(x):
    mu = np.mean(x, axis=0)          
    sigma = np.std(x, axis=0)              
    x_norm = (x - mu) / sigma 
    return x_norm

def compute_cost(x, y, w, b):
    m = x.shape[0]
    cost = 0
    for i in range(m):
        f_wb = np.dot(x[i], w) + b
        cost += (f_wb - y[i]) * (f_wb - y[i])
    cost /= 2*m
    return cost

def compute_gradient(x, y, w, b):
    m, n = x.shape
    dj_dw = np.zeros(n)
    dj_db = 0
    for i in range(m):
        err= np.dot(x[i], w) + b - y[i]
        dj_dw += np.dot(err, x[i])
        dj_db += err
    dj_dw /= m
    dj_db /= m
    return dj_dw, dj_db

def run_gradient_descent(x, y, itr, alpha):
    w = np.zeros(x.shape[1])
    b = 0
    for i in range(itr):
        dj_dw, dj_db = compute_gradient(x, y, w, b)
        w -= np.dot(alpha, dj_dw)
        b -= alpha * dj_db
        if i % (itr/10) == 0:
            print(compute_cost(x, y, w, b))
    
    return w, b

x = np.arange(0, 20, 1)
y = np.cos(x/2)
X = np.c_[x, x**2, x**3, x**4, x**5, x**6, x**7, x**8, x**9, x**10, x**11, x**12, x**13]
X = z_score_normalize(X) 


model_w, model_b = run_gradient_descent(X, y, 100000, 1e-1)
plt.scatter(x, y, marker = 'x', c = 'r', label = "Actual Value"); plt.title("Added $x^2, x^3, ...x^13$ feature")
plt.plot(x, np.dot(X, model_w) + model_b, label = "Predicted Value"); plt.xlabel("x"); plt.ylabel("y");plt.legend(); plt.show()
plt.show
