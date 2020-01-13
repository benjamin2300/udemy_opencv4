"""
  read show write images
"""

import cv2
import numpy as np

# read image
image = cv2.imread('images/alone_person.jpeg')

# show image
cv2.imshow('Hello World!', image)
cv2.waitKey()
cv2.destroyAllWindows()
# image property data
print ('Height of image : ', image.shape[0], ' pixels.')
print ('Width of image : ', image.shape[1], ' pixels.')

# write image
cv2.imwrite('images/output_test.jpg', image)