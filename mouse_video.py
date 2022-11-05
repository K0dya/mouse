import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np

cap = cv2.VideoCapture("Mouse1.mp4")
first_frame = cap.read()[1]
(w, h, c) = first_frame.shape
template = np.zeros(first_frame.shape[:2], dtype="uint8")
matrix = np.ones(first_frame.shape)*255
#cv2.imshow("template", template)
#cv2.imshow("matrix", matrix)
my_list =[]
while True:
    frame = cap.read()[1]
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    h_min = (118, 86, 96)
    h_max = (144, 255, 255)
    thresh = cv2.inRange(hsv, h_min, h_max)
    cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, cnts, -1, (255, 0, 0), 2, cv2.LINE_AA, hierarchy, 1)
    for cnt in cnts:
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
        if len(approx) > 5:
            ellipse = cv2.fitEllipse(cnt)
            (x, y), (MA, ma), angle = cv2.fitEllipse(cnt)
            c = (int(x), int(y))
            cv2.ellipse(frame, ellipse, (0, 255, 255), 2)
            cv2.circle(matrix, c, 1, (0, 0, 255), 2)
            my_list.append(c)

    my_list=my_list
    template = cv2.bitwise_or(template, thresh)
    cv2.imshow("frame", frame)
    cv2.imshow("matrix", matrix)
    # with open('test.txt', 'w') as f:
    #     for line in my_list:
    #         f.write(f"{line}\n")
    #cv2.imwrite("plot2.jpg", matrix)
    cv2.waitKey(1)
