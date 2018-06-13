from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

x=np.array([1,2,3,4,5,6],dtype=np.float64)
y=np.array([5,4,6,5,6,7],dtype=np.float64)

def best_fit_slope_and_intercept(x,y):
	m=((mean(x)*mean(y))-mean(x*y))/((mean(x)*mean(x))-mean(x*x))
	b=(mean(y)-m*mean(x))
	m=round(m,2)	
	return m,b
m,b=best_fit_slope_and_intercept(x,y) 

reg_line=[(m*x)+b for x in x]
plt.scatter(x,y,color="blue")
plt.plot(x,reg_line)
plt.show()

