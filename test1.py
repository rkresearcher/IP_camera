from hikvisionapi import Client
import cv2
import time

cam = Client('http://192.168.1.65/doc/page/login.asp', 'admin', 'Abc.12345', timeout=30)
cam.count_events = 2 # The number of events we want to retrieve (default = 1)
response = cam.Streaming.channels[102].picture(method='get', type='opaque_data')

with open('screen.jpg', 'wb') as f:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)

time.sleep(1)
img = cv2.imread('screen.jpg')
cv2.imshow("show", img)
cv2.waitKey(0)
