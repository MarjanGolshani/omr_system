import os
import random
import cv2
from tkinter import Button, Toplevel, Canvas
import numpy as np
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import test_grader
import subprocess


class Buttons:
    def __init__(self, root, tbs, interface, makePicPath, showPic, openPic, var , openAns):
        self.root = root
        self.tbs = tbs
        self.interface = interface
        self.makePicPath = makePicPath
        self.showPic = showPic
        self.openPic = openPic
        self.openAns=openAns
        self.var = var


    def topButton(self):

        self.tb = Button(self.root, text = "Correct!", font=("Arial",11,"bold"),command=lambda :self.topButtonClick(), height = 2, width = 12)
        self.tb.place(x= 620, y=220)
    def nextButton(self):

        self.tb = Button(self.root, text = "Next!", font=("Arial",11,"bold"),command=lambda :self.nextButtonClick(self.root), height = 2, width = 12)
        self.tb.place(x= 1120, y=550)

    def topButtonClick(self):
        #print(self.tbs.getTask())
        self.fileName = self.openPic.fileName

        self.file_answer = self.openAns.file_answer
        print(self.file_answer)

        if(self.tbs.getTask() == 1):
            str = test_grader.correct(self.fileName , self.file_answer)
            print("dd")

            #image = cv2.imread(self.fileName)
            #max_row= image.shape[0]
            #no = random.randint(1, max_row)
            #print("Random Row Number:",no)
            #self.new_fileName = self.makePicPath.make(self.fileName, "_new.jpg")
            #row_no_profile.q52(image, no, self.new_fileName)
            self.showPic.showNewPix(str, self.interface)




        elif (self.tbs.getTask() ==2):
            print("22")


        else:
            print("KKK")

    def nextButtonClick(self, root):


        self.fileName = "C:\\Users\\ANDISHASAZAN\\PycharmProjects\\optical\\venv\\Include\\images_test\\test1.jpg"
        self.file_answer = "Answer_key.xlsx"
        self.new_fileName = "C:\\Users\\ANDISHASAZAN\\PycharmProjects\\optical\\venv\\Include\\images_test\\sample.jpg"


        self.cv = Canvas(root, bg='white')
        self.cv.pack(side="left", fill="both", expand="yes")


        image = Image.open(self.fileName)
        image = image.resize((450, 450), Image.ANTIALIAS)
        self.img_0 = ImageTk.PhotoImage(image)
        self.def_image_0 = self.cv.create_image(50, 300, image=self.img_0, anchor= 'w')

        image_1 = Image.open(self.new_fileName)
        image_1 = image_1.resize((450, 450), Image.ANTIALIAS)
        self.img_1 = ImageTk.PhotoImage(image_1)
        self.def_image_1 = self.cv.create_image(1300, 300, image=self.img_1, anchor= 'e')

