import csv
import cv2
import pandas as pd
import time
import numpy as np
import random
import os, glob, pickle
from sklearn.utils import shuffle


folder1 = "Indian"
folder2 = "Asian"

destfolder = "IA"



test1 = pd.read_csv(folder1+"/test.csv")
train1 = pd.read_csv(folder1+"/train.csv")


test2 = pd.read_csv(folder2+"/test.csv")
train2 = pd.read_csv(folder2+"/train.csv")


combtest = np.array(test1.iloc[:,:].append(test2.iloc[:,:]))

print(combtest)

#newtest = pd.DataFrame(test.iloc[:,:])


#print(np.array(a))