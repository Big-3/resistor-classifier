from classifierlib import models
import pandas as pd
import glob
import os
import utils

IMG_INPUT_PATH='./Imatges_retallades'
NAMES=['negre', 'negre2', 'marro', 'roig', 'roig2', 'taronja', 'groc', 'verd', 'blau', 'lila', 'gris', 'blanc']

thresh_lower = []
thresh_upper = []
for thresh in models.Thresholds.thresh:
    if 'LOWER' in thresh:
        thresh_lower.append(models.Thresholds.thresh[thresh])
    else:
        thresh_upper.append(models.Thresholds.thresh[thresh])

def merge_csv(csv_list):
    return pd.concat(map(pd.read_csv, csv_list), ignore_index=True)

def packet_size(nelements):
    possible = [2,3,4,5,6,7,8,9,10]
    for packet_size in possible:
        if nelements%packet_size == 0:
            return packet_size
    return 1

def get_csv_numbert():
    nelements=0
    for fil in glob.iglob('*.csv'):
        nelements+=1
    return nelements

def remove_file_from_list(files_to_delete):
    for file in files_to_delete:
        os.remove(file)

def process_img(img_path):
    img = models.Image()
    img.set_img(img_path)
    img.set_areas(thresh_lower, thresh_upper, NAMES)
    return img.areas

def main():
    """
    for img_path in glob.iglob('{}/*.png'.format(IMG_INPUT_PATH)):
        df = pd.DataFrame()
        print('PROCESSING IMAGE ' + img_path)
        areas = process_img(img_path)
        areas['label'] = img_path.split('/')[-1].split('-')[0]
        df = df.append(areas, ignore_index=True)
        df.to_csv(img_path.split('/')[-1].split('.')[0] + '.csv')
    """
    nelements = get_csv_numbert()
    size = packet_size(nelements)
    while(size != 1):
        files = []
        for file in glob.iglob('*.csv'):
            files.append(file)

        i=1
        to_merge=[]
        for csv_file in files:
            to_merge.append(csv_file)

            if i==size:
                print('merging ', to_merge)
                merge_csv(to_merge).to_csv('concat_' + utils.rand_string()+ '.csv')
                remove_file_from_list(to_merge)
                to_merge=[]
                i=0
            i+=1
        size = packet_size(get_csv_numbert())

    exit(1)

if __name__ == '__main__':
    main()
