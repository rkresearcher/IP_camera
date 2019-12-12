import tkinter
import cv2
from PIL import Image,ImageTk
root = tkinter.Tk()
root.geometry("1000x600+200+0")
w = 1350
h = 640
capture = tkinter.Canvas(root, bd=2, bg="black", height=h, width=w)
capture.grid(column = 1, row = 0)

'''cam = tkinter.Entry(root)
cam.grid(column=1, row=2)
capture.create_window(200,400,window=cam)
iteam=cam.get()
print(iteam)'''

video = None
frame = None


img=None
show=None
begin = False
def start_record(event):
	global begin,frame,img,root,show,capture,video #,iteam    
#        print(type(iteam))
 #       print (iteam)
	'''cam = tkinter.Entry(root)
	capture.create_window(200,140,window=cam)
	iteam=cam.get()
	iteam = int(iteam)'''
	cap = cv2.VideoCapture()
      # cap1 = cv2.VideoCapture() 
#        cap.open("rtsp://admin:Abc.12345@192.168.1.64/Streaming/Channels/2")   
#cap.open("rtsp://admin:Abc.12345@192.168.1.65/Streaming/Channels/1")
	cap.open("rtsp://admin:Abc.12345@192.168.1.65/Streaming/Channels/101")

	fram_wid = int(cap.get(3))
	fram_hei = int(cap.get(4))
	out = cv2.VideoWriter('record.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10 , (fram_wid,fram_hei))
	begin = True
	while begin:
		check, frame = cap.read()
		out.write(frame)
		frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
		img = Image.fromarray(frame)
		w,h = img.size
		img = img.resize((w*1,h*1))
		show = ImageTk.PhotoImage(img)
		capture.create_image(0,0,anchor=tkinter.NW,image=show)
		root.update()

def start_capture(event):
	global begin,frame,img,root,show,capture,video    
	#video = cv2.VideoCapture()
	cap = cv2.VideoCapture()
  #      cap1 = cv2.VideoCapture() 
	cap.open("rtsp://admin:Abc.12345@192.168.1.64/Streaming/Channels/2")   
#cap.open("rtsp://admin:Abc.12345@192.168.1.65/Streaming/Channels/1")
#	cap.open("rtsp://admin:Abc.12345@192.168.1.65/Streaming/Channels/101")

	begin = True
	while begin:
		check, frame = cap.read()
		frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
		img = Image.fromarray(frame)
		w,h = img.size
		img = img.resize((w*1,h*1))
		show = ImageTk.PhotoImage(img)
		capture.create_image(0,0,anchor=tkinter.NW,image=show)
		root.update()
def stop_capture(event):
	global video,begin
	begin = False
	video.release()


start = tkinter.Button(root, text='Record')
start.grid(column = 1, row = 3)
start.bind('<Button-1>', start_record) 


start = tkinter.Button(root, text='Start')
start.grid(column = 1, row = 4)
start.bind('<Button-1>', start_capture)  
stop = tkinter.Button(root, text='Stop')
stop.grid(column = 1, row = 5)
stop.bind('<Button-1>', stop_capture)  
root.mainloop()
