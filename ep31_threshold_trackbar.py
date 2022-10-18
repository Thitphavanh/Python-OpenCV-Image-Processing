# Function Threshold Trackbar
import cv2
import matplotlib.pyplot as plt


def display(value):
    pass


cv2.namedWindow('Output')
cv2.createTrackbar('Value', 'Output', 128, 255, display)

while True:
    gray_img = cv2.imread('images/ant.jpg', 0)
    thresh_value = cv2.getTrackbarPos('Value', 'Output')
    thresh, result = cv2.threshold(gray_img, thresh_value, 255, cv2.THRESH_BINARY)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
    cv2.imshow('Output', result)

cv2.destroyAllWindows()
