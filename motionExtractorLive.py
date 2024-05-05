import cv2
import matplotlib.pyplot as plt
import numpy as np
import time

cap = cv2.VideoCapture(0)
cap.set(3, 400)
cap.set(4, 300)

delay = float(0.1)

while True:
    success, cam1 = cap.read()
    time.sleep(delay)

    success, cam2 = cap.read()
    
    rgb1 = cv2.cvtColor(cam1, cv2.COLOR_BGR2RGB)
    rgb2 = cv2.cvtColor(cam2, cv2.COLOR_BGR2RGB)

    neg = abs(255 - rgb2)

    blended = cv2.addWeighted(rgb1, 1.0, neg, 0.5, 0)

    gray = cv2.cvtColor(blended, cv2.COLOR_RGB2GRAY)
    _, binaryImage = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    invert = abs(255 - binaryImage)
    
    cv2.imshow( "Detected", cam1)
    cv2.imshow("Blended", invert)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break