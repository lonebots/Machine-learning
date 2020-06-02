import numpy as np

def variance(values,mean):
    return (sum((x-mean)**2 for x in values))

def covariance(x,mean_x,y,mean_y):
    covar=0
    for i in range(len(x)):
      covar+=((x[i]-mean_x)*(y[i]-mean_y))
    return covar    
x = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_mean,y_mean=np.mean(x),np.mean(y)
print(x_mean,y_mean)
x_new=[i[0] for i in x]
print (variance(y,y_mean))
print(covariance(x,x_mean,y,y_mean))