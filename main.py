"""
Implement the linear regression model using python and numpy in the following class.
The method fit() should take inputs like,
x = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]

"""

import numpy as np

class LinearRegression(object):
#function for variance
  def variance(values,mean):
    return sum([(x-mean)**2 for x in values])
#function for covariance
  def covariance(x,mean_x,y,mean_y):
    covar=0
    for i in range(len(x)):
      covar+=((x[i]-mean_x)*(y[i]-mean_y))
      return covar


  def fit(self,_input, _output):
    x=_input
    y=_output
    x_mean,y_mean=np.mean(x),np.mean(y)
    b1=covariance(x,x_mean,y,y_mean)/variance(x,x_mean)
    b0=y_mean-b1*x_mean
    return[b0,b1]

    
    
  def predict(_input):
    b0,b1=
    pass
    
    
