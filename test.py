import numpy as np 
import cv2
'''
for Hd_Cam
use cahnnels 1,2,3
for Thermal_cam
use channels 101..
'''

'''t = input("Press 1 for Thermal and 2 for HD: ")
if t =='1':
    print ('this is HD')
    cap = cv2.VideoCapture() 
    cap.open("rtsp://admin:Abc.12345@192.168.1.64/Streaming/Channels/2")   
elif t=='2':
   print("This is thermal")
   cap = cv2.VideoCapture() 
   cap.open("rtsp://admin:Abc.12345@192.168.1.65/Streaming/Channels/101")   
else:
   print ("error")
'''
#cap = cv2.VideoCapture()
cap1 = cv2.VideoCapture('/home/rksingh/Download/record_EDIT_00_middle_00.avi') 
#cap.open("rtsp://admin:Abc.12345@192.168.1.64/Streaming/Channels/2")   
#cap.open("rtsp://admin:Abc.12345@192.168.1.65/Streaming/Channels/1")
#cap1.open("rtsp://admin:Abc.12345@192.168.1.65/Streaming/Channels/101")
#print (cap1)
while(True):
    #ret, frame = cap.read()
    ret1, frame1 = cap1.read()
    #frame.shape
    # Display the resulting frame
    #cv2.imshow('HD_CAM',frame)
    cv2.imshow('IR_CAM',frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture 
cap.release()
cv2.destroyAllWindows()
