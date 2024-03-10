import matplotlib.pyplot as plt 

plot_x = []
plot_y = []

data_x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data_y = [3, 5, 7, 9, 11, 13, 15, 17, 19]

data_count = len(data_x)
alpha = 0.0001
h = 0.0000001

def j_wb(w, b):
    sq_err = 0
    for i in range(data_count):
        sq_err += ((w * data_x[i]) + b - data_y[i]) * ((w * data_x[i]) + b - data_y[i])
    mean_sq_err = sq_err / (2 * data_count)
    return mean_sq_err

def derv_w_j_wb(w, b):
    delta_sum = 0;
    for i in range(data_count):
        delta_sum += ((((w * data_x[i]) + b) - data_y[i]) * data_x[i])
    return (delta_sum / data_count)

def derv_b_j_wb(w, b):
    delta_sum = 0;
    for i in range(data_count):
        delta_sum += (((w * data_x[i]) + b) - data_y[i])
    return (delta_sum / data_count)

def minimise_j_wb():
    w = 0
    b = 0
    err_w = 1
    err_b = 1
    count = 0
    while(abs(err_w) > 0.00000000001 and abs(err_b) > 0.00000000001):
        err_w = alpha * derv_w_j_wb(w, b)
        err_b = alpha * derv_b_j_wb(w, b)
        w = w - err_w
        b = b - err_b
        #print(f"{err_w} {err_b}")
        count+=1
        if count%2000 == 0:
            plot_x.append(count)
            plot_y.append(j_wb(w, b))
    print(f"w: {w}\nb: {b}")
    plt.plot(plot_x, plot_y)
    plt.title("cost vs iteration")
    plt.ylabel("cost(j_wb)")
    plt.xlabel("iteration")
    plt.show()

minimise_j_wb()
