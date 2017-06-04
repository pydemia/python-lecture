# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 17:54:49 2017

@author: dawkiny
"""


import numpy as np
import pandas as pd
import scipy as sp
import scipy.stats as st
import sklearn as sl

import matplotlib.pyplot as plt

from unipy.sample.datasets import dataManager as dm
dm.init()
dm.datalist()
data = dm.load(dm.datalist()[0])
#%%

# Mean
data.columns

col = data['age']
col.mean()
np.mean(col)
sp.mean(col)
np.nanmean(col)

# Median
col.median()
np.median(col)
sp.median(col)
np.nanmedian(col)

# Max(Min)
max(col)
col.max()
np.max(col)
np.maximum(col, col) # Returns an NDarray with Element-wise Max elements
sp.maximum(col, col) # Returns an NDarray with Element-wise Max elements
np.nanmax(col)  # Returns an NDarray with 
                # fmax amax maximum

doc = np.nanmax.__doc__

#%%

dfn, dfd = 29, 18
mean, var, skew, kurt = st.f.stats(dfn, dfd, moments='mvsk')


x = np.linspace(st.f.ppf(0.01, dfn, dfd), st.f.ppf(0.99, dfn, dfd), 100)
fig, ax = plt.subplots(1, 1)
ax.plot(x, st.f.pdf(x, dfn, dfd), 'r-', lw=5, alpha=0.6, label='f pdf')


#%%

ndata = dm.load('nutrients')
ndata.columns
grouped = ndata.groupby(['nutrients'])
for key, value in grouped['value']:
    print(key, value.max())
    
#%%


idata = dm.load('iris')
idata.columns
x, y = idata['sepal_length'], idata['petal_width']
arrX = idata.iloc[:, :3]

tstat, pval = st.ttest_1samp(x, 0)
tstat, pval = st.ttest_ind(x, y)

wstat, pval = st.wilcoxon(x, y, zero_method='wilcox', correction=False)


ustat, pval = st.mannwhitneyu(x, y, use_continuity=True, alternative=None)


#%%

from statsmodels.formula.api import ols

model = ols('petal_width ~ sepal_length', idata).fit()
print(model.summary()) 

print(model.f_test([0, 1, -1, 0]))

#%%
import statsmodels.api as sm
model = sm.OLS(y, x).fit()
print(model.summary())

x2 = sm.add_constant(x)
model = sm.OLS(y, x2).fit()
print(model.summary())

from sklearn.linear_model import LinearRegression as linreg
tmp = linreg(fit_intercept=True).fit(arrX, y)
tmp.coef_

st.linregress(x, y)

#%% Stepwise Regression (F-score)


tmp = linreg(fit_intercept=True).fit(arrX, y)
tmp.coef_
tmp = linreg(fit_intercept=True).fit(arrX.iloc[:,1:], y)
tmp.coef_

import sklearn.feature_selection as fs
fs.mutual_info_regression(arrX, y)
fscore, pval = fs.f_regression(arrX, y)
fs.mutual_info_regression(arrX, y)

#%%
fs.SelectKBest()
res = fs.SelectKBest(fs.f_regression, k=1).fit_transform(arrX, y)
res = fs.SelectKBest(fs.mutual_info_regression, k=1).fit_transform(arrX, y)

x2 = sm.add_constant(x)
est = sm.OLS(y, x2)
est2 = est.fit()
print(est2.summary())

st.linregress(x, y)
model.summary()


#%%

test = dm.load('adult')
y = test['capital_gain']

list(filter(lambda col: col not in ['capital_gain'], set(test.columns)))
[member for member in set(test.columns) if member not in ['capital_gain']]
arrX = test[list(filter(lambda col: col not in ['capital_gain'], test.columns))]

res = fs.SelectKBest(fs.f_regression, k=1).fit_transform(arrX, y)
model = ols('capital_gain ~ age + workclass + education + marital_status + occupation + relationship + sex + native_country', test).fit()
model.summary()
