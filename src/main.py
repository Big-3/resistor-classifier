#!/usr/bin/env python3
import classifierlib
import glob
import pickle
import pandas as pd
from classifierlib import models

INPUT_FOLDER='./input_images/'

NAMES=[]
resistencies=['100k', '120k', '150k', '180k', '220k', '270k', '330k', '390k', '470k', '560k', '680k', '820k']

thresh_lower = []
thresh_upper = []
for thresh in models.Thresholds.thresh:
    if 'LOWER' in thresh:
        thresh_lower.append(models.Thresholds.thresh[thresh])
    else:
        NAMES.append(thresh.split('_')[0])
        thresh_upper.append(models.Thresholds.thresh[thresh])


if __name__ == '__main__':
	with open(classifierlib.get_model_path(), "rb") as f:
		model = pickle.load(f)

	for img_path in glob.iglob(f'{INPUT_FOLDER}/*.jpg'):
		print(img_path)
		image = models.Image()
		image.set_img(img_path)
		image.set_areas(thresh_lower, thresh_upper, NAMES)

		resistor = pd.DataFrame()
		resistor = resistor.append(image.areas, ignore_index=True)
		print(resistor)
		res = model.predict(resistor)
		print('got', resistencies[res[0]])
