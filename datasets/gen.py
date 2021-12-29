from classifierlib import models
import pandas as pd
import numpy as np
import utils
import os
import glob

INPUT_PATH='./Imatges_retallades'
NAMES=['negre', 'negre2', 'marro', 'roig', 'roig2', 'taronja', 'groc', 'verd', 'blau', 'lila', 'gris', 'blanc']

def process_img(img_path):
    img = models.Image()
    img.set_img(img_path)
    thresh_lower = []
    thresh_upper = []
    for thresh in models.Thresholds.thresh:
        if 'LOWER' in thresh:
            thresh_lower.append(models.Thresholds.thresh[thresh])
        else:
            thresh_upper.append(models.Thresholds.thresh[thresh])
    img.set_areas(thresh_lower, thresh_upper, NAMES)
    return img.areas

if __name__ == '__main__':
    df = pd.DataFrame()
    for img_path in glob.iglob('{}/*.png'.format(INPUT_PATH)):
        print('PROCESSING IMAGE ' + img_path)
        areas = process_img(img_path)
        areas['label'] = img_path.split('/')[-1].split('-')[0]
        df = df.append(areas, ignore_index=True)
    df.to_csv('resistors.csv')
    exit(1)
