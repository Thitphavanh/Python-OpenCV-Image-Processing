# Create TrackBar
import cv2
import numpy as np


img = np.zeros((200, 250, 3), np.uint8)
cv2.namedWindow('Color TrackBar')


def display(value):
    pass


# ເລີ່ມຕົ້ນສ້າງ TrackBar
cv2.createTrackbar('B', 'Color TrackBar', 0, 255, display)
cv2.createTrackbar('G', 'Color TrackBar', 0, 255, display)
cv2.createTrackbar('R', 'Color TrackBar', 0, 255, display)

while True:
    cv2.imshow('Color TrackBar', img)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

    # ດຶງຄ່າຈາກ TrackBar
    blue = cv2.getTrackbarPos('B', 'Color TrackBar')
    green = cv2.getTrackbarPos('G', 'Color TrackBar')
    red = cv2.getTrackbarPos('R', 'Color TrackBar')

    img[:] = [blue, green, red]


cv2.destroyAllWindows()
