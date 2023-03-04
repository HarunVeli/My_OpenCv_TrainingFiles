import cv2
import numpy as np

#+255 ile tüm matrisleri 0'dan 255'e çekerek beyaz olmasını sağladık
canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

#print(canvas)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()