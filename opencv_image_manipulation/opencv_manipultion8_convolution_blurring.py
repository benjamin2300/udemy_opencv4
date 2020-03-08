import cv2
import numpy as np

image = cv2.imread("images/alone_person.jpeg")
cv2.imshow("Original image", image)
cv2.waitKey(0)


# creating 3 x 3 kernel
k_3 = np.ones((3, 3), np.float32) / 9
blurred = cv2.filter2D(image, -1, k_3)
cv2.imshow("3 x 3 Kernel Blurring", blurred)
cv2.waitKey(0)

# creating 7 x 7 kernel
k_7 = np.ones((7, 7), np.float32) / 9
blurred2 = cv2.filter2D(image, -1, k_7)
cv2.imshow("7 x 7 Kernel Blurring", blurred)
cv2.waitKey(0)

cv2.destroyAllWindows()


import cv2
import numpy as np

image = cv2.imread("images/mikoto2.jpg")

blur = cv2.blur(image, (7, 7))
cv2.imshow("Averag blur", blur)
cv2.waitKey(0)

gaussian_blur = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow("Gaussian blur", gaussian_blur)
cv2.waitKey(0)

median_blur = cv2.medianBlur(image, 7)
cv2.imshow("Median blur", median_blur)
cv2.waitKey(0)

bilateral = cv2.bilateralFilter(image, 7, 75, 75)
cv2.imshow("Bilateral blur", bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()


# image de-noising
import cv2
import numpy as np

image = cv2.imread("images/crist2.jpg")
dst = cv2.fastNlMeansDenoisingColored(image, None, 6, 6, 7, 21)

cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.imshow("Fast Means Denoising", dst)
cv2.waitKey(0)

cv2.destroyAllWindows()