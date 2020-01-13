import cv2

# read image
image = cv2.imread('images/shiki.jpg')
cv2.imshow('Shiki is beautiful!', image)
cv2.waitKey()

# convert full color image to black-white image
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey Shiki is beautiful!', grey_image)
cv2.waitKey()
cv2.destroyAllWindows()

# convert full color image to black-white image in simple way
image = cv2.imread('images/shiki.jpg', 0)
cv2.imshow('Shiki is beautiful!', image)
cv2.waitKey()
cv2.destroyAllWindows()