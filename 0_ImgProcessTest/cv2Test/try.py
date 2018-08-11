import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

img = cv2.imread('j.png',0)

for i in range(100):
    img[random.randrange(0,140),random.randrange(0,110)] = 255

 

kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img,kernel,iterations=1)

plt.figure()
plt.imshow(img)

plt.figure()
plt.imshow(erosion)

dilation = cv2.dilate(img,kernel,iterations=1)
plt.figure()
plt.imshow(dilation)

opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
plt.figure()
plt.imshow(opening)

closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
plt.figure()
plt.imshow(closing)


gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
plt.figure()
plt.imshow(gradient)
