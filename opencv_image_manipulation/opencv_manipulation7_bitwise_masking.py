import cv2
import numpy as np

square = np.zeros((300, 300), np.uint8)
cv2.rectangle(square, (50, 50), (250, 250), 255, -2)
cv2.imshow("Square", square)
cv2.waitKey(0)

ellipse = np.zeros((300, 300), np.uint8)
cv2.ellipse(ellipse, (150, 150), (150, 150), 30, 0, 180, 255, -1)
cv2.imshow("Ellipse", ellipse)
cv2.waitKey(0)

cv2.destroyAllWindows()

img_and = cv2.bitwise_and(square, ellipse)
cv2.imshow("And", img_and)
cv2.waitKey(0)

img_or = cv2.bitwise_or(square, ellipse)
cv2.imshow("Or", img_or)
cv2.waitKey(0)

img_xor = cv2.bitwise_xor(square, ellipse)
cv2.imshow("Xor", img_xor)
cv2.waitKey(0)

img_not_sqr = cv2.bitwise_not(square)
cv2.imshow("Not Square", img_not_sqr)
cv2.waitKey(0)

img_not_ellipse = cv2.bitwise_not(ellipse)
cv2.imshow("Not ellipse", img_not_ellipse)
cv2.waitKey(0)

cv2.destroyAllWindows()
