# python-motion-extractor
Motion extractor using Python and OpenCV

Motion extractor used for detect slight motion.

# How does it works?
Two identical frames with time difference, blended into a single frame to detect motion. So slight motion changes will appear clearly.

# Python and OpenCV
I am using Python and OpenCV to make this Motion Extractor.
```python
import cv2
import time
```
I also use 'time' library to create time difference between frames.

# Video Source
I make 2 Python files with different video source, [Live Feeds Input](https://github.com/danielwitansa/python-motion-extractor/blob/main/motionExtractorLive.py) and [Video Files Input](https://github.com/danielwitansa/python-motion-extractor/blob/main/motionExtractorVid.py)

For live feeds, the program use camera to get live feeds.
```python
cap = cv2.VideoCapture(0)
cap.set(3, 400)
cap.set(4, 300)
```
Set main camera as OpenCV live feeds. Or else, use video files as video source for the program.
```python
from tkinter import filedialog

def openVideo():
    filePath =  filedialog.askopenfilename(
        title="Select Video File", filetypes=[("Video files", "*.mp4")]
    )
    cv2path = str(filePath)

    return cv2path

cv2path = openVideo()

source = cv2.VideoCapture(cv2path)
```
I am using tkinter fledialog library to get file directory path.

# Frame Delay
```python
success, cam1 = cap.read()
time.sleep(delay)
success, cam2 = cap.read()
```
Create time difference between two frames using 'time.sleep()'

# Negative Filter
Negative filter is used to create contrast between frames.
```python
neg = abs(255 - rgb2)
```
To create negative filter, the 8-bit RGB color need to be inverted.

# Blend Frames
```python
blended = cv2.addWeighted(rgb1, 1.0, neg, 0.5, 0)
```
Blend original frame and negative filtered frame on top with 50% opacity.

# Binary Image
With the intention to increase the contrast of motion changes, I convert the frame to grayscale and change the threshold so the color output is only black and white.
```python
gray = cv2.cvtColor(blended, cv2.COLOR_RGB2GRAY)
_, binaryImage = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
invert = abs(255 - binaryImage)
```

# Final Result
The result show the slight motion in "original" window showed within "Blended" window
![image](https://github.com/danielwitansa/python-motion-extractor/assets/138917810/80b4ce66-691d-498c-8006-f7aee27db9e0)
