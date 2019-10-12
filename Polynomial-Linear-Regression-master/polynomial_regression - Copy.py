# Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
#dataset = pd.read_csv('Position_Salaries.csv')
dataset = pd.read_csv('Social_Network_Ads.csv')
print(dataset.head())
X = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:,4].values

#splitting the data into test and training set
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=0)





 #data preprocessing..
#feature Scaling


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

#this code will scale all the values from -2 to 2

print(X_train) 
