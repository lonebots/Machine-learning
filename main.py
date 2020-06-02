"""
Implement the linear regression model using python and numpy in the following class.
The method fit() should take inputs like,
x = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]

"""

import numpy as np
b0=0.0
b1=0.0
class LinearRegression(object):

#function for variance
  def variance(self,values,mean):
    return sum([(x-mean)**2 for x in values])
#function for covariance
  def covariance(self,x,mean_x,y,mean_y):
    covar=0
    for i in range(len(x)):
      covar+=((x[i]-mean_x)*(y[i]-mean_y))
      return covar

  def fit(self,_input, _output):
    global b1,b0
    x=_input
    y=_output
    x_mean,y_mean=np.mean(x),np.mean(y)
    b1 =self.covariance(x,x_mean,y,y_mean)/self.variance(x,x_mean)
    b0 =y_mean-b1*x_mean
    print (b0,b1)
    

    
    
  def predict(self,_input):
    global b0,b1
    y=b0+b1*_input
    return y
    pass
    
    
