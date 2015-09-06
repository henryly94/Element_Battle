__author__ = 'Administrator'
import math
import numpy as np
import cv2
img = cv2.imread("./img/default.jpg")
rows, cols, channels = img.shape
print channels
pts1 = np.float32([[0,0],[451,0],[0,460],[451,460]])
pts2 = np.float32([[0,100],[200,0],[0,300],[200,200]])
M = cv2.getPerspectiveTransform(pts1,pts2)
img2 = cv2.warpPerspective(img,M,(200,300))

for i in img2:
    for j in i:
        if j[0]==j[1]==j[2]==0:
            #print "haha"
            j = [255,255,255]
cv2.imwrite("./img/dd2.jpg",img2)
cv2.namedWindow("Image")

cv2.imshow("Image", img2)
cv2.waitKey (0)
cv2.destroyAllWindows()

a = [1,2,3]
b = [5,10,15]
c = [0,0,0]
for i in range(3):
    c[i] = b[i]-a[i]
print pow(b[1],2)
print c

a.append("abc")
a.append((a,3,2))
n = 0
print a
for i in a:
    n = n + 1
    if n == 2:
        a.remove(i)
print a[0:2]
