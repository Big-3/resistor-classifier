#!/usr/bin/env python3

import numpy as np
import pandas as pd
import utils
from numba import jit, cuda
from datasets import get_train_dataset_directory
from models import Image, Thresholds

# neural network
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
import pickle

@jit
def fit_and_predict(model, X, y, X_test):
    model.fit(X,y)
    predict = model.predict(X_test)
    return model, predict

resistors = pd.read_csv(get_train_dataset_directory() + '/concat_QJBOXBRZQV.csv')
resistors['label'] = resistors['label'].astype('category')
resistors['label'] = resistors['label'].cat.codes
print('loaded dataset', resistors.shape)

X = resistors[resistors.columns[0:-1]]
y = resistors['label']
print('X shape y shape', X.shape, y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)
print(f'trained Xtrain {X_train.shape} Xtest {X_test.shape} ytrain {y_train.shape} ytest {y_test.shape}')


neural_net = MLPClassifier(solver='adam', max_iter=1000, random_state=1)

bag = BaggingClassifier(
    base_estimator=neural_net,
    n_estimators=10,
    max_samples=1.0,
    max_features=1.0,
    bootstrap=False,
    n_jobs=2,
    random_state=1)
model, y_pred = fit_and_predict(bag, X_train, y_train, X_test)

test = []
predictions = []
for predict in y_pred:
	predictions.append(predict)

for t in y_test:
	test.append(t)

for i in range(len(test)):
	print(f'Got: {predictions[i]}; Expected: {test[i]}; Deviation: {test[i] - predictions[i]}')

print('Misclassified samples: %d' % (y_test != y_pred).sum())
print('Accuracy: %.2f%%' % (100.0 * model.score(X_test, y_test)))


with(open("model.pkl", "wb") as f):
    pickle.dump(model, f)
