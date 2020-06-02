"""
Implement the linear regression model using python and numpy in the following class.
The method fit() should take inputs like,
x = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

import numpy

class LinearRegression(object):
  
  
  def fit(_input, _output):
    x=_input
    y=_output
    x_mean,y_mean=numpy.mean(x),numpy.mean(y)
    b1=numpy.cov(x,x_mean,y,y_mean)/numpy.var(x,x_mean)
    b0=y_mean-b1*x_mean
    

    
    
  def predict(_input):
    pass
    
    
