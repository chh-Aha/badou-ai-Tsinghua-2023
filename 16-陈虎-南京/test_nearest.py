import cv2
import numpy as np

def nearest(img,dhight,dwidth):
    hight,width,channels = img.shape
    print(channels)
    emptyImage = np.zeros((dhight,dwidth,channels),np.uint8)
    sh = dhight/hight
    sw = dwidth/width
    for c in range(channels):
        for i in range(dhight):
            for j in range( dwidth):
                x = int(i/sh+0.5)
                y = int(j/sw+0.5)
                emptyImage[i,j,c] = img[x,y,c]
    return emptyImage

img = cv2.imread('lenna.png')
# img1 = cv2.resize(img,(800,800),interpolation=cv2.INTER_NEAREST)
zoom = nearest(img,800,800)
cv2.imshow('nearest',zoom)
cv2.imshow('img',img)
# cv2.imshow('img1',img1)
cv2.waitKey(0)