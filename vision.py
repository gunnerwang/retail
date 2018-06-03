import cv2
import datetime
import os
from face import *
import threading
import time
import upload
import random
from PIL import Image

flag = False
record = 900000
image = None
start_time = None
last_faces = None
delay = 0
dthreshold = 5
best_img = None
#wait for the data-mining of the database
pop_items = [['shaver','steamwater','beer'], ['tobacoo','tie', 'shoe'], ['oil', 'beer', 'fish'], ['umbrella', 'skincare', 'sunglass'], ['coffee', 'bag', 'jewelry'], ['glass', 'vegetable' ,'clothes']]

def deal_img(img):
    global best_img
    # best_img = img
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    global flag
    global record
    global start_time
    global image
    global last_faces
    global delay
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) > 0:
        delay = 0
        last_faces = faces
        if not flag:
            flag = True
            start_time = time.time()
        for (x,y,w,h) in faces:

            center_x = x + w//2
            center_y = y + h//2
            center = img.shape
            if pow((center[0]-center_x),2)+pow((center[1]-center_y),2)< record:
                best_img = img
                record = pow((center[0]-center_x),2)+pow((center[1]-center_y),2)

            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    elif flag == True and delay < dthreshold:
        faces = last_faces
        delay += 1
        for (x,y,w,h) in faces:
            center_x = x + w//2
            center_y = y + h//2
            center = img.shape
            if pow((center[0]-center_x),2)+pow((center[1]-center_y),2)< record:
                best_img = img
                record = pow((center[0]-center_x),2)+pow((center[1]-center_y),2)

            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    else:
        if flag:
            flag = False
            record = 900000
            span = int(time.time() - start_time)
            if span > 1:
                print("trigger: {time}".format(time=span))
                img_path = "image/" + str(start_time) + ".jpg"
                cv2.imwrite(img_path, best_img)
                threading.Thread(target=face_detect, args=(img_path, span)).start()
                # face_detect(img_path)
    cv2.rectangle(img, (0,img.shape[0] - 25),(270, img.shape[0]), (255,255,255), -1)
    cv2.putText(img, "Number of faces detected: " + str(len(faces)), (0,img.shape[0] - 10), cv2.FONT_HERSHEY_TRIPLEX,
                0.5,  (0,0,0), 1)
    image = img
    return img

def face_detect(output_dir, span):
    information = face(output_dir)
    if len(information) > 0:
        print(information)
        for person in information:
            gender = 0 if person["gender"] == "MALE" else 1
            if (person["age"] > 0 and person["age"] < 25 and person["gender"] == "MALE"):
                os.system("say hi guy! would you like to look at %s" %pop_items[0][random.randint(0,2)])
            if (person["age"] >= 25 and person["age"] < 50 and person["gender"] == "MALE"):
                os.system("say hi sir! would you like to look at %s" % pop_items[1][random.randint(0, 2)])
            if (person["age"] >= 50 and person["age"] < 75 and person["gender"] == "MALE"):
                os.system("say hi senior! would you like to look at %s" % pop_items[2][random.randint(0, 2)])
            if (person["age"] > 0 and person["age"] < 25 and person["gender"] == "FEMALE"):
                os.system("say hi girl! would you like to look at %s" % pop_items[3][random.randint(0, 2)])
            if (person["age"] >= 25 and person["age"] < 50 and person["gender"] == "FEMALE"):
                os.system("say hi madam! would you like to look at %s" % pop_items[4][random.randint(0, 2)])
            if (person["age"] >= 50 and person["age"] < 75 and person["gender"] == "FEMALE"):
                os.system("say hi lady! would you like to look at %s" % pop_items[5][random.randint(0, 2)])

            #go to the database
            upload.upload_to_server(gender, person["age"], span, "奥利奥", "16", output_dir)



