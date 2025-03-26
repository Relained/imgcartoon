import cv2
import numpy as np

SOURCE = "/Users/relained/MEGA/work/univ/ComputerVision/imgcartoon/123.png"

img = cv2.imread(SOURCE)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
color = cv2.bilateralFilter(img, 9, 75, 75)

# 노이즈 감소 (택 1)
gray = cv2.medianBlur(gray, 5)
# gray = cv2.bilateralFilter(gray, 9, 75, 75)

edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite("cartoon_image.jpg", cartoon)