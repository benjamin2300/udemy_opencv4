import cv2
import numpy as np

image = cv2.imread('images/shiki.jpg')

height, width = image.shape[:2]
quater_height = height / 4
quater_width = width / 4
# translation matrix, 2 x 3 matrix
T = np.float32([[1, 0, quater_width], [0, 1, quater_height]])
# cv2.wrapAffine(image, T matrix, (width, height))
img_transition = cv2.warpAffine(image, T, (width, height))
cv2.imshow("Image Transition", img_transition)
cv2.waitKey(0)
cv2.destroyAllWindows()

print (T)