import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('images/shiki.jpg')

# cal image b number
histgram = cv2.calcHist([image], [0], None, [256], [0, 256])

# show image data as histgram by matplotlib
# plt.bar(range(256), histgram.ravel() )
B, G, R = cv2.split(image)
# plt.hist(B.ravel(), 256, [0, 256])
plt.show()

# show image data as plot by matplotlib
colors = ['b','g', 'r']
for i, color in enumerate(colors):
  histgram2 = cv2.calcHist([image], [i], None, [256], [0, 256])
  plt.plot(histgram2, color=color)
  plt.xlim([0, 256])

plt.show()