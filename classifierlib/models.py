#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 11:48:36 2021

@author: swaglot
@coauthor: Albert
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt
import utils
import statistics

class Image():
    def __init__(self, path=''):
        self.path = path
        if self.path != '' and self.path != None:
            img = cv2.imread(self.path)
            imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        else:
            img = None
            imgHSV = None
        self.img = img
        self.imgHSV = imgHSV
        self.areas = dict()

    def set_img(self, path):
        self.path = path
        self.img = cv2.imread(self.path)
        self.imgHSV = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

    def set_areas(self, areas_lower, areas_upper, names, kernel=np.ones((5,5), np.uint8), iterations=1):
        if self.imgHSV.all() == None: raise Exception('No image was declared. HSV is NONE and probably img is also')
        if len(areas_lower) is len(names) and len(areas_upper) is len(areas_lower):
            for i in range(len(names)):
                area = cv2.inRange(self.imgHSV, areas_lower[i], areas_upper[i])
                self.areas[names[i]] = statistics.mean(utils.flatten_ndim(cv2.dilate(cv2.erode(area, kernel, iterations), kernel, iterations)).tolist())
        else:
            raise Exception("Lists do not have same length. Expect an N length lists containing the differents areas.")

class Thresholds():
    thresh = dict()
    """
    thresh["NEGRE_LOWER"]=np.array([0, 0, 0], np.uint8)
    thresh["NEGRE_UPPER"]=np.array([27, 5, 51], np.uint8)
    thresh["NEGRE2_LOWER"]=np.array([0, 250, 0], np.uint8)
    thresh["NEGRE2_UPPER"]=np.array([27, 255, 51], np.uint8)
    thresh["MARRO_LOWER"]=np.array([0, 200, 0], np.uint8)
    thresh["MARRO_UPPER"]=np.array([9, 255, 102], np.uint8)
    thresh["ROIG_LOWER"]=np.array([0, 50, 51], np.uint8)
    thresh["ROIG_UPPER"]=np.array([1, 255, 165], np.uint8)
    thresh["ROIG2_LOWER"]=np.array([176, 254, 51], np.uint8)
    thresh["ROIG2_UPPER"]=np.array([179, 255, 165], np.uint8)
    thresh["TARONJA_LOWER"]=np.array([2, 250, 76], np.uint8)
    thresh["TARONJA_UPPER"]=np.array([8, 255, 204], np.uint8)
    thresh["GROC_LOWER"]=np.array([14, 220, 64], np.uint8)
    thresh["GROC_UPPER"]=np.array([22, 255, 196], np.uint8)
    thresh["VERD_LOWER"]=np.array([53, 50, 0], np.uint8)
    thresh["VERD_UPPER"]=np.array([72, 255, 102], np.uint8)
    thresh["BLAU_LOWER"]=np.array([98, 50,0], np.uint8)
    thresh["BLAU_UPPER"]=np.array([119, 255, 127], np.uint8)
    thresh["LILA_LOWER"]=np.array([157, 100, 0], np.uint8)
    thresh["LILA_UPPER"]=np.array([179, 255, 140], np.uint8)
    thresh["GRIS_LOWER"]=np.array([0, 0, 0], np.uint8)
    thresh["GRIS_UPPER"]=np.array([36, 153, 102], np.uint8)
    thresh["BLANC_LOWER"]=np.array([9, 18, 64], np.uint8)
    thresh["BLANC_UPPER"]=np.array([32, 102, 204], np.uint8)
    """
    thresh["NEGRE_LOWER"]=np.array([0, 0, 0], np.uint8)
    thresh["NEGRE_UPPER"]=np.array([179, 255, 50], np.uint8)
    thresh["MARRO_LOWER"]=np.array([0, 75,10], np.uint8)
    thresh["MARRO_UPPER"]=np.array([15,255, 100], np.uint8)
    thresh["ROIG_LOWER"]=np.array([0, 180, 110], np.uint8)
    thresh["ROIG_UPPER"]=np.array([10, 255, 255], np.uint8)
    thresh["TARONJA_LOWER"]=np.array([7, 127, 127], np.uint8)
    thresh["TARONJA_UPPER"]=np.array([15, 255, 255], np.uint8)
    thresh["GROC_LOWER"]=np.array([17, 100, 112], np.uint8)
    thresh["GROC_UPPER"]=np.array([35, 255, 255], np.uint8)
    thresh["VERD_LOWER"]=np.array([45, 70, 20], np.uint8)
    thresh["VERD_UPPER"]=np.array([100, 255, 255], np.uint8)
    thresh["BLAU_LOWER"]=np.array([85, 50, 60], np.uint8)
    thresh["BLAU_UPPER"]=np.array([125, 255, 255], np.uint8)
    thresh["LILA_LOWER"]=np.array([130, 64, 10], np.uint8)
    thresh["LILA_UPPER"]=np.array([179, 255, 255], np.uint8)
    thresh["GRIS_LOWER"]=np.array([0, 0, 50], np.uint8)
    thresh["GRIS_UPPER"]=np.array([179, 50, 80], np.uint8)
    thresh["BLANC_LOWER"]=np.array([0, 0, 63], np.uint8)
    thresh["BLANC_UPPER"]=np.array([179, 15, 140], np.uint8)
