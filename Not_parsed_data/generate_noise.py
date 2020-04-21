import numpy as np
import random
import cv2
import os
import shutil
import xml.etree.ElementTree as ET

def sp_noise(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

classes = os.listdir('data/')
for cls in classes:
    files = os.listdir('data/' + str(cls) + "/")

    for fl in files:
        image = cv2.imread('data/' + str(cls) + "/" + fl ,0)

        for i in range(5):
            noise_img = sp_noise(image,0.01*(i+1))
            cv2.imwrite('data/' + str(cls) + "/" + fl + "-modified-" + ".jpg", noise_img)
