#!/usr/bin/env python3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datasets import get_train_dataset_directory


resistor = pd.read_csv(get_train_dataset_directory() + '/concat_VFUMLNDDGU.csv')
resistor['label'] = resistor['label'].astype('category')
resistor['label'] = resistor['label'].cat.codes

resistor.hist(figsize=(8,10))

f, ax = plt.subplots(figsize=(6,4))
resistor_corr = resistor.corr()
sns.heatmap(resistor_corr, vmax=1.0, vmin=-1.0, annot=True)

plt.show()
