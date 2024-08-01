import pandas as pd
import numpy as np
from sklearn import preprocessing
csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']
irisdata= pd.read_csv(csv_url,names=col_names)
pd.set_option('display.max_columns', 20)
x=irisdata.iloc[:,:4]
print(irisdata['Species'].unique())

labelencode=preprocessing.LabelEncoder()
irisdata['Species']=labelencode.fit_transform(irisdata['Species'])
print(irisdata['Species'].unique())
features_iris=irisdata.drop(columns=['Species'])