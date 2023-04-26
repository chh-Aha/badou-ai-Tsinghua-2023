import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lenna.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray_img',gray)

# 直方图均衡化
dst = cv2.equalizeHist(gray)

hist = cv2.calcHist([dst],[0],None,[256],[0,256])
plt.figure()
plt.hist(dst.ravel(), 256)
plt.show()

cv2.imshow('equallizeHist',np.hstack([gray,dst]))

(b,g,r) = cv2.split(img)
B = cv2.equalizeHist(b)
G = cv2.equalizeHist(g)
R = cv2.equalizeHist(r)
result = cv2.merge([B,G,R])
cv2.imshow('dst_rgb',result)

cv2.waitKey(0)

