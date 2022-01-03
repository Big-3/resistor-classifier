#!/usr/bin/env python3

import numpy as np
import pandas as pd
import utils
from datasets import get_train_dataset_directory
from models import Image, Thresholds

# neural network
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

resistors = pd.read_csv(get_train_dataset_directory() + '/concat_BABITNYPLF.csv')
resistors['label'] = resistors['label'].astype('category')
resistors['label'] = resistors['label'].cat.codes
print('loaded dataset', resistors.shape)

X = resistors[resistors.columns[0:-1]]
y = resistors['label']
print('X shape y shape', X.shape, y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)
print(f'trained Xtrain {X_train.shape} Xtest {X_test.shape} ytrain {y_train.shape} ytest {y_test.shape}')


neural_net = MLPClassifier(max_iter=1000000, random_state=1)
neural_net.fit(X_train, y_train)

test = []
predictions = []
y_pred = neural_net.predict(X_test)

for predict in y_pred:
	predictions.append(predict)

for t in y_test:
	test.append(t)

for i in range(len(test)):
	print(f'Got: {predictions[i]}; Expected: {test[i]}; Deviation: {test[i] - predictions[i]}')

print('Misclassified samples: %d' % (y_test != y_pred).sum())
print('Accuracy: %.2f%%' % (100.0 * neural_net.score(X_test, y_test)))
