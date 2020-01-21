import cv2
import numpy as np

# Black 512 x 512 x 3 image (Color)
# Black 512 x 513 image (B&W)
image = np.zeros((512, 512, 3), np.uint8)
image_bw = np.zeros((512, 512), np.uint8)

cv2.imshow("Black Rectangle (Color)", image)
cv2.imshow("Blcak Rectangle (B&W)", image_bw)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Draw a line on black rectangle
image = np.zeros((512, 512, 3), np.uint8)
# cv2.line(image, start, end, color, stroke_width)
cv2.line(image, (0, 0), (511, 511), (255, 127, 0), 5)
cv2.imshow("Draw a line", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Draw a rectangle on black rectangle
image = np.zeros((512, 512, 3), np.uint8)
# cv2.rectangle(image, start, end, color, stroke_width)
cv2.rectangle(image, (100, 100), (300, 250), (127, 50, 127), 5)
cv2.imshow("Draw a rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Draw a circle on black rectangle
image = np.zeros((512, 512, 3), np.uint8)
# cv2.circle(image, centroid, radius, color, stroke_width)
cv2.circle(image, (350, 350), 100, (15, 75, 50), -1)
cv2.imshow("Draw a cicle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Draw a polygons on black rectangle
image = np.zeros((512, 512, 3), np.uint8)
pts = np.array([[10, 50], [400, 50], [90, 200], [50, 500]], np.int32)
#reshape points
pts = pts.reshape((-1, 1, 2))

# cv2.polylines(image, [pts], True, color, stroke_width)
cv2.polylines(image, [pts], False, (0, 0, 255), 3)
cv2.imshow("Draw a polyline", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Add text to image
image = np.zeros((512, 512, 3), np.uint8)
# cv2.putText(image, text, start_bl, font, font-size, color, stroke_width)
cv2.putText(image, "Hello World", (75, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (100, 170, 10), 4)
cv2.imshow("Hello World text!", image)
cv2.waitKey(0)
cv2.destroyAllWindows()