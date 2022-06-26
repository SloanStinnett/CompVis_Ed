import cv2 as cv
from cv2 import imread

img = imread('Photos/dolphin.jpg')

cv.imshow('Dolphin',img)
cv.waitKey(0)