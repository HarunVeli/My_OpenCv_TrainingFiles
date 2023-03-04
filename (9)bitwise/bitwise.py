import cv2
import numpy as np

bitwise_1 = cv2.imread("(9)bitwise/bitwise_1.png")
bitwise_2 = cv2.imread("(9)bitwise/bitwise_2.png")

cv2.imshow("bitwise_1", bitwise_1)
cv2.imshow("bitwise_2", bitwise_2)

bit_and = cv2.bitwise_and(bitwise_2, bitwise_1)
cv2.imshow("bit_and", bit_and)
bit_or = cv2.bitwise_or(bitwise_2, bitwise_1)
cv2.imshow("bit_or", bit_or)
bit_xor = cv2.bitwise_or(bitwise_2, bitwise_1)
cv2.imshow("bit_xor", bit_xor)
bit_not = cv2.bitwise_not(bitwise_2) # tersini verir
cv2.imshow("bit_not", bit_not)

cv2.waitKey(0)
cv2.destroyAllWindows()