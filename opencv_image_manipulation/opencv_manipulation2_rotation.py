import cv2
import numpy as np

image = cv2.imread("images/mikoto.jpg")
height, width = image.shape[:2]

# rotation matrix
# cv2.getRotationMatrix2D(centroid, degree, direction) 
# -1: clockwise, 1: counterclockwise
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, -1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

cv2.imshow("Image Rotation", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# method 2 to rotate image
image = cv2.imread("images/mikoto.jpg")
rotated_image = cv2.transpose(image)

cv2.imshow("Image Rotation 2", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

