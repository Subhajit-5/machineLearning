import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


train = pd.read_csv('titanic_train.csv')

a=sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
print(a)