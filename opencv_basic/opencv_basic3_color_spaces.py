import cv2
import numpy as np

# read image
image = cv2.imread('images/shiki.jpg')
# show image pixel r g b
B, G, R = image[100, 0]
print (B, G, R)
# show grey image pixel
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print (grey_image.shape)
print (grey_image[100, 0])

# 
image = cv2.imread('images/shiki.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV image', hsv_image)
cv2.imshow('Hue channel', hsv_image[:, :, 0])
cv2.imshow('Saturation channel', hsv_image[:, :, 1])
cv2.imshow('Value channel', hsv_image[:, :, 0])

cv2.waitKey()
cv2.destroyAllWindows()



image = cv2.imread('images/shiki.jpg')

B, G, R = cv2.split(image)
print (B.shape)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)
cv2.destroyAllWindows()

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

merged = cv2.merge([B+100, G, R])
cv2.imshow("Merged with B plus 100", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()




image = cv2.imread('images/shiki.jpg')

B, G, R = cv2.split(image)
# print (B.shape)
zeros = np.zeros(image.shape[:2], dtype="uint8")

cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))

cv2.waitKey(0)
cv2.destroyAllWindows()
