import cv2
import numpy as np

image = cv2.imread("images/ere.jpg")

# cv2.resize(image, None, fx, fy)
# shrink to 3/4 of original size
image_scaled = cv2.resize(image, None, fx=0.5, fy=0.5)

cv2.imshow("Scale - Linear Interpolation", image_scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()

# double the image
image_scaled = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow("Scale - CUBIC Interpolation", image_scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()


# skew size resize to exact size
image_scaled = cv2.resize(image, (900, 400), interpolation=cv2.INTER_AREA)
cv2.imshow("Scale - Skew size Interpolation", image_scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()
