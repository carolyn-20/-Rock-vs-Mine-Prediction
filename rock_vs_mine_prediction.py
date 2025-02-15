# -*- coding: utf-8 -*-
"""Rock vs Mine Prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1o12EhzvLbtr-UTlmpaISfEFRWahb7z-B
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

sonar_data = pd.read_csv('/content/Copy of sonar data.csv', header = None)

sonar_data.head()

sonar_data.shape

sonar_data.describe()

sonar_data[60].value_counts()

sonar_data.groupby(60).mean()

X = sonar_data.drop([60], axis = 1)
y = sonar_data[60]

print(X)

print(y)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.1, stratify = y, random_state = 1) #stratify is used for inbalanced datasets

print(y_train.shape, y_test.shape)

model = LogisticRegression()

model.fit(X_train, y_train)

X_train_prediction = model.predict(X_train)
predicted = accuracy_score(X_train_prediction, y_train)
print(predicted)

X_test_predicted = model.predict(X_test)
predicted_test = accuracy_score(X_test_predicted, y_test)
print(predicted_test)

input_data = (0.0164,0.0173,0.0347,0.0070,0.0187,0.0671,0.1056,0.0697,0.0962,0.0251,0.0801,0.1056,0.1266,0.0890,0.0198,0.1133,0.2826,0.3234,0.3238,0.4333,0.6068,0.7652,0.9203,0.9719,0.9207,0.7545,0.8289,0.8907,0.7309,0.6896,0.5829,0.4935,0.3101,0.0306,0.0244,0.1108,0.1594,0.1371,0.0696,0.0452,0.0620,0.1421,0.1597,0.1384,0.0372,0.0688,0.0867,0.0513,0.0092,0.0198,0.0118,0.0090,0.0223,0.0179,0.0084,0.0068,0.0032,0.0035,0.0056,0.0040)

input_data_as_numpy_array = np.asarray(input_data)
reshaped_data = input_data_as_numpy_array.reshape(1, -1) #reshape is used to reshape the array according to the rows, if the 1d contains 30 values it is converted to 5rows x 6 columns(changes the layout)

predict = model.predict(reshaped_data)
print(predict)

if (predict[0] == 'R'):
  print('The object is a Rock')
else:
  print('The object is a Mine')

