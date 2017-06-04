#%% 모듈, 패키지

from src.mod import mymodule as md
from src.mod.mymodule import stopwatch as sw


tmp = md.stopwatch()
tmp = sw()


from src.op import int_operators, float_operators


#%% Numpy

# Start
import numpy
import numpy as np

myarray = np.array([[1,2,3], [4,5,6], [7,8,9]])
myarray

np.identity(3) # 단위행렬
np.eye(2) # 단위행렬
np.zeros((3,2)) # 영행렬
np.empty((2,3)) # 영행렬
np.ones((2,2)) # 값이 1인 행렬
np.random.rand(2,3) # Random 행렬 

np.matrix(myarray) # Matrix
np.arange(9)


# Calculation
print(myarray.shape)
print(myarray.dtype)

myarray * 10
myarray + 10

xarray = np.array([[1,2,3], [4,5,6], [7,8,9]])
yarray = np.array([1,0,1])

xarray * yarray
xarray.dot(yarray)
np.dot(xarray, yarray)


# Subsetting
myarray[0][2]
myarray[0,2]

myarray[:2]
myarray[:2,:]
myarray[:,:2]


#%% Pandas

# Series
myarray = np.arange(9)
myseries = pd.Series(myarray)

myseries myseries.add(2)
myseries.multiply(2)
pd.Series(map(lambda x: x*2, myseries))

myseries[2]
strSeries = myseries.astype(str)
strSeries[2] 


# DataFrame
myarray = np.array([[1,2,3],
                    [4,5,6]])
mydf = pd.DataFrame(myarray)
mydf

mydf.columns
mydf.columns = ['a', 'b', 'c']
mydf

mydf = pd.DataFrame({'a':[1,2,3],
              'b':[4,5,6]})
mydf.T
mydf.transpose()

mydf.iloc[:2,1]
mydf.loc[:2, 'a'] 

mydf[‘a’] # pd.Series
mydf[['a']] # pd.DataFrame
mydf[mydf['a'] < 2]['b'] 
