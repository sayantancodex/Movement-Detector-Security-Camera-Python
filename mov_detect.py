#copyright SAYANTANPATRA68
#for Issues Contact sayantanpatra68@gmail.com

import sys
import cv2
import time
import pyautogui as pg
import ctypes
import pyttsx3 #pip install pyttsx3

print("copyright SAYANTANPATRA68")
print("Made by Sayantan Patra")
print("for issues email - sayantanpatra68@gmail.com")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

video = cv2.VideoCapture(0)

first_frame = None

while True:
    check,frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    threshold_frame = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]
    #threshold_frame = cv2.dilate(threshold_frame.copy(), cv2.RTR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    threshold_frame = cv2.dilate(threshold_frame, None, iterations = 100)

    (cntr,_)= cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cntr:
        if cv2.contourArea(contour)<1000:
            continue
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0), 3)

        
        #ctypes.windll.user32.LockWorkStation()
        
        speak("Security breach detected!, Locking your device")
        speak("Device Locked successfully!")
        
        ctypes.windll.user32.LockWorkStation()
        sys.exit()


        

    cv2.imshow("Sayantan Patra Security Camera", frame)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()        
