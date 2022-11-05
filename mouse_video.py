import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np

cap = cv2.VideoCapture("Mouse1.mp4")
first_frame = cap.read()[1]
(w, h, c) = first_frame.shape
template = np.zeros(first_frame.shape[:2], dtype="uint8")
# cv2.imshow("template", template)
while True:
    frame = cap.read()[1]
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    h_min = (118, 86, 96)
    h_max = (144, 255, 255)
    thresh = cv2.inRange(hsv, h_min, h_max)
    cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, cnts, -1, (255, 0, 0), 2, cv2.LINE_AA, hierarchy, 1)
    for cnt in cnts:
        ellipse = cv2.fitEllipse(cnt)
        cv2.ellipse(frame, ellipse, (0, 255, 255), 2)
    template = cv2.bitwise_or(template, thresh)
    cv2.imshow("frame", frame)
#   cv2.imshow("thresh", thresh)
    cv2.imshow("track", template)
    cv2.waitKey(1)
