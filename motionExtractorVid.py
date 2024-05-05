import cv2
import time
from tkinter import filedialog

def openVideo():
    filePath =  filedialog.askopenfilename(
        title="Select Video File", filetypes=[("Video files", "*.mp4")]
    )
    cv2path = str(filePath)

    return cv2path

cv2path = openVideo()

source = cv2.VideoCapture(cv2path)

delay = float(0.1)

while True:
    ret, cam1 = source.read()
    time.sleep(delay)

    ret, cam2 = source.read()
    
    rgb1 = cv2.cvtColor(cam1, cv2.COLOR_BGR2RGB)
    rgb2 = cv2.cvtColor(cam2, cv2.COLOR_BGR2RGB)

    neg = abs(255 - rgb2)

    blended = cv2.addWeighted(rgb1, 1.0, neg, 0.5, 0)

    gray = cv2.cvtColor(blended, cv2.COLOR_RGB2GRAY)
    _, binaryImage = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    invert = abs(255 - binaryImage)

    resizedDetected = cv2.resize(cam1, (640, 480))
    resizedInvert = cv2.resize(invert, (640, 480))
    
    cv2.imshow( "Detected", resizedDetected)
    cv2.imshow("Blended", resizedInvert)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()