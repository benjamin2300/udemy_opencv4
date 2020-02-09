import cv2

image = cv2.imread("images/ere.jpg")
height, width = image.shape[:2]

s_row = int(height * .1)
s_col = int(width * .5)
e_row = int(height * .45)
e_col = int(width * .8)

cropped = image[s_row:e_row, s_col:e_col]

cv2.imshow("Original", image)
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()