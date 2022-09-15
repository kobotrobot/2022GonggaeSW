import cv2
import numpy as np
import time
import datetime
import sys
import argparse
from tkinter import *
from pynput.keyboard import Controller
import os
import threading
import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound

agec = [0,0,0]
menu = {"아메리카노":3000, "라떼":3500, "아이스티":3000}
tmpli = []
price=0
class voiceloop(threading.Thread):
    mykeyboard = Controller()

    def run(self) -> None:
        cost =0
        a = 1
        cnt=0
        while True:
            voice = self.CollectVoice()
            tmpli.append(voice)
            print(tmpli)
            if voice != False and myThread.rflag == True:
                print(voice)
                self.Pasting(voice)

            if myThread.rflag == False:
                break


            if "추천해 줘" == tmpli[-1]:
                print("추천해줘")
                if(max(agec)==agec[0]):
                    speak("청소년 추천메뉴로는 아이스티를 추천합니다.", a)
                    a = a + 1
                if (max(agec) == agec[1]):
                    speak("대학생 직장인 추천 메뉴로는 아이스아메리카노를 추천합니다", a)
                    a = a + 1
                if (max(agec) == agec[2]):
                    speak("어르신분들 추천 메뉴로는 라떼를 추천합니다.", a)
                    a = a + 1
            elif "아메리카노" == tmpli[-1]:
                print("아메리카노")

                speak("아이스로 하시겠습니까? 뜨거운걸로 하시겠습니까?",a)
                a=a+1
                voice = self.CollectVoice()
                tmpli.append(voice)
                print(tmpli)
                if voice != False and myThread.rflag == True:
                    print(voice)
                    self.Pasting(voice)
                if "아이스" ==tmpli[-1]:
                    print("아이스 아메리카노")
                    speak("더 주문하실건 없으십니까", a)
                    a = a + 1
                    cost += menu["아메리카노"]
                    voice = self.CollectVoice()
                    tmpli.append(voice)
                    print(tmpli)
                    if voice != False and myThread.rflag == True:
                        print(voice)
                        self.Pasting(voice)
                    if "예" ==tmpli[-1]:
                        speak("요금 {0}원 결제 도와드리겠습니다.".format(cost), a)
                        a = a + 1
                        on_closing()
                    elif "아니오" ==tmpli[-1]:
                        continue
                elif "뜨거운거" ==tmpli[-1]:
                    print("뜨거운 아메리카노")
                    speak("더 주문하실건 없으십니까", a)
                    a = a + 1
                    cost += menu["아메리카노"]
                    if "네" in tmpli:
                        speak("요금 {0}원 결제 도와드리겠습니다.".format(cost), a)
                        a = a + 1
                        on_closing()
                    elif "아니오" ==tmpli[-1]:
                        continue
            elif "라떼" ==tmpli[-1]:
                print("라떼")
                speak("아이스로 하시겠습니까? 뜨거운걸로 하시겠습니까?",a)
                a = a + 1
                voice = self.CollectVoice()
                tmpli.append(voice)
                print(tmpli)
                if voice != False and myThread.rflag == True:
                    print(voice)
                    self.Pasting(voice)
                if "아이스" ==tmpli[-1]:
                    print("아이스 라떼")
                    speak("더 주문하실건 없으십니까", a)
                    a = a + 1
                    cost += menu["라떼"]
                    voice = self.CollectVoice()
                    tmpli.append(voice)
                    print(tmpli)
                    if voice != False and myThread.rflag == True:
                        print(voice)
                        self.Pasting(voice)
                    if "예" ==tmpli[-1]:
                        speak("요금 {0}원 결제 도와드리겠습니다.".format(cost), a)
                        on_closing()
                        a = a + 1
                    elif "아니오" ==tmpli[-1]:
                        continue
                elif "뜨거운거" ==tmpli[-1]:
                    print("뜨거운 라떼")
                    speak("더 주문하실건 없으십니까", a)
                    a = a + 1
                    cost += menu["라떼"]
                    voice = self.CollectVoice()
                    tmpli.append(voice)
                    print(tmpli)
                    if voice != False and myThread.rflag == True:
                        print(voice)
                        self.Pasting(voice)
                    if "예" ==tmpli[-1]:
                        speak("요금 {0}원 결제 도와드리겠습니다.".format(cost), a)
                        on_closing()
                        a = a + 1
                    elif "아니오" ==tmpli[-1]:
                        continue
            elif "아이스티" ==tmpli[-1]:
                print("아이스티")
                speak("더 주문하실건 없으십니까", a)
                a = a + 1
                cost += menu["아이스티"]
                voice = self.CollectVoice()
                tmpli.append(voice)
                print(tmpli)
                if voice != False and myThread.rflag == True:
                    print(voice)
                    self.Pasting(voice)
                if "예" ==tmpli[-1]:
                    speak("요금 {0}원 결제 도와드리겠습니다.".format(cost), a)
                    a = a + 1
                    on_closing()
                elif "아니오" ==tmpli[-1]:
                    continue
            else:
                print("없는 메뉴 입니다")
                tmpli.pop()
                speak("없는 메뉴 입니다.", a)
                a = a + 1
                speak("무엇을 주문하시겠습니까", a)
                a = a + 1

    def Pasting(self, myvoice):
        for character in myvoice:
            self.mykeyboard.type(character)
        self.mykeyboard.type(" ")

    def CollectVoice(self):
        # get microphone device on notebook or desk top
        listener = sr.Recognizer()
        voice_data = ""

        with sr.Microphone() as raw_voice:

            try:

                img_frm.config(image=mic3_img)
                print("Adjusting")
                listener.adjust_for_ambient_noise(raw_voice)

                # adjust setting values
                listener.dynamic_energy_adjustment_damping = 0.2
                listener.pause_threshold = 0.6
                listener.energy_threshold = 600

                img_frm.config(image=mic1_img)

                print("Say something!")
                audio = listener.listen(raw_voice)
                img_frm.config(image=mic2_img)

                voice_data = listener.recognize_google(audio, language='ko')



            except UnboundLocalError:
                pass

            except sr.UnknownValueError:
                print("could not understand audio")
                return False

            return str(voice_data)


def on_closing():
    myThread.rflag = False
    print("finish work")
    # myThread.join()
    os._exit(1)


def speak(text,i):

     tts = gTTS(text=text, lang='ko')
     filename='voice'+str(i)+'.mp3'
     tts.save(filename)

     time.sleep(1)

     playsound.playsound(filename)


def highlightFace(net, frame, conf_threshold=0.7):
    frameOpencvDnn=frame.copy()
    frameHeight=frameOpencvDnn.shape[0]
    frameWidth=frameOpencvDnn.shape[1]
    blob=cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections=net.forward()
    faceBoxes=[]
    for i in range(detections.shape[2]):
        confidence=detections[0,0,i,2]
        if confidence>conf_threshold:
            x1=int(detections[0,0,i,3]*frameWidth)
            y1=int(detections[0,0,i,4]*frameHeight)
            x2=int(detections[0,0,i,5]*frameWidth)
            y2=int(detections[0,0,i,6]*frameHeight)
            faceBoxes.append([x1,y1,x2,y2])
            cv2.rectangle(frameOpencvDnn, (x1,y1), (x2,y2), (0,255,0), int(round(frameHeight/150)), 8)
    return frameOpencvDnn,faceBoxes


parser=argparse.ArgumentParser()
parser.add_argument('--image')

args=parser.parse_args()
count =0
faceProto="opencv_face_detector.pbtxt"
faceModel="opencv_face_detector_uint8.pb"
ageProto="age_deploy.prototxt"
ageModel="age_net.caffemodel"
genderProto="gender_deploy.prototxt"
genderModel="gender_net.caffemodel"

MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)
#ageList=['1', '1', '1', '1', '1', '2', '2', '2']
ageList = ['1', '1', '1', '2',
            '2', '2', '3', '3']
genderList=['Male','Female']

faceNet=cv2.dnn.readNet(faceModel,faceProto)
ageNet=cv2.dnn.readNet(ageModel,ageProto)
genderNet=cv2.dnn.readNet(genderModel,genderProto)

video=cv2.VideoCapture(0)
padding=20
while cv2.waitKey(1)<0:
    hasFrame,frame=video.read()
    if not hasFrame:
        cv2.waitKey()
        break

    resultImg,faceBoxes=highlightFace(faceNet,frame)
    if not faceBoxes:

        print("No face detected")
        cv2.imshow("Detecting age and gender", resultImg)

    for faceBox in faceBoxes:
        face=frame[max(0,faceBox[1]-padding):
                   min(faceBox[3]+padding,frame.shape[0]-1),max(0,faceBox[0]-padding)
                   :min(faceBox[2]+padding, frame.shape[1]-1)]

        blob=cv2.dnn.blobFromImage(face, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)
        genderNet.setInput(blob)
        genderPreds=genderNet.forward()
        gender=genderList[genderPreds[0].argmax()]
        print(f'Gender: {gender}')

        ageNet.setInput(blob)
        agePreds=ageNet.forward()
        age=ageList[agePreds[0].argmax()]

        print(f'Age: {age[1:-1]} years')

        cv2.putText(resultImg, f'{gender}, {age}', (faceBox[0], faceBox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2, cv2.LINE_AA)
        cv2.imshow("Detecting age and gender", resultImg)

        count=count+1
        if(age == '1'):
            agec[0]=agec[0]+1
        elif(age == '2'):
            agec[1]=agec[1]+1
        elif(age == '3'):
            agec[2]=agec[2]+1
        if(count >10):
            print('detect')
            speak("무엇을 주문하시겠습니까",0)
            root = Tk()
            root.title("Voice Collector")
            root.geometry("200x200+50+50")

            mic1_img = PhotoImage(file="mic1.png")
            mic2_img = PhotoImage(file="mic2.png")
            mic3_img = PhotoImage(file="mic3.png")

            img_frm = Label(root, image=mic2_img)
            img_frm.pack();

            myThread = voiceloop()
            myThread.rflag = True
            myThread.start()
            root.protocol("WM_DELETE_WINDOW", on_closing)
            root.wm_attributes("-topmost", 1)
            root.mainloop()


