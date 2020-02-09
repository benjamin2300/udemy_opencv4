import cv2
import numpy as np

image = cv2.imread("images/mikoto.jpg")

M = np.ones(image.shape, dtype="uint8") * 75

added_image = cv2.add(image, M)
cv2.imshow("Original", image)
cv2.imshow("Added", added_image)

sub_image = cv2.subtract(image, M)
cv2.imshow("Subtract", sub_image)

cv2.waitKey(0)
cv2.destroyAllWindows()