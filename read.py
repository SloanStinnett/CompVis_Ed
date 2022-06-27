import cv2 as cv
from cv2 import imread

img = imread('Photos/dolphin.jpg')

g_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)


subimg = g_img[300:325,0:300]

print(g_img[250,:])

cv.imshow('grayimage',g_img[250,:])
cv.waitKey(0)

cv.imshow('subimage',subimg)
cv.waitKey(0)