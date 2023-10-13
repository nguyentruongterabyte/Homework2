"""
  MSSV     : N20DCCN083
  Họ và tên: Nguyễn Thái Trưởng
"""

import cv2

J1 = cv2.imread('lenagray.jpg', cv2.IMREAD_COLOR)

J2 = 255 - J1
cv2.imshow('Photographic Negative', J2)

cv2.imwrite('photographic_negative.jpg', J2)

cv2.waitKey(0)
cv2.destroyAllWindows()





