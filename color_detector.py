import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np

cap = cv2.VideoCapture("Mouse1.mp4")
first_frame = cap.read()[1]
# cv2.imwrite("first_frame.jpg", first_frame)
img = Image.open("first_frame.jpg")
I = cv2.imread("first_frame.jpg")
# cv2.imshow("fist_frame", first_frame)
hsv = cv2.cvtColor(I, cv2.COLOR_RGB2HSV)
h_min = (118,86,96)
h_max = (144, 255, 255)
thresh = cv2.inRange(hsv, h_min, h_max)
img2 = Image.fromarray(np.uint8(thresh))

window = tk.Tk()
window.geometry("1800x960")

photo = ImageTk.PhotoImage(img)
photo2 = ImageTk.PhotoImage(img2)
frame_img = tk.Frame(window)
frame_img.pack(side = tk.LEFT, anchor = tk.E)
lbl_img = tk.Label(frame_img, text = "Loren ipsum img", relief = tk.RAISED)
lbl_img.pack()

frame_prop = tk.Frame(window)
frame_prop.pack(side = tk.BOTTOM, anchor = tk.W)
lbl_prop = tk.Label(frame_prop, text = "slider", relief = tk.RAISED)
lbl_prop.pack()

frame_img2 = tk.Frame(window)
frame_img2.pack(side = tk.LEFT, anchor = tk.E)
lbl_img2 = tk.Label(frame_img2, text = "Loren ipsum img", relief = tk.RAISED)
lbl_img2.pack()

lbl_img.configure(image = photo)
lbl_img.image = photo

lbl_img2.configure(image = photo2)
lbl_img2.image = photo2

window.mainloop()