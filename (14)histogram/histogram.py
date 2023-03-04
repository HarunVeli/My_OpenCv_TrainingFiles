import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = np.zeros((500, 500), np.uint8) + 50
img = cv2.imread("(14)histogram/klon.jpg")

b, g, r = cv2.split(img)

cv2.imshow("Original", img)

# plt.hist(img.ravel(), 256, [0, 256])
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()