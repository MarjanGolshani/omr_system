
from copy import copy
import random
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

import matplotlib
from PIL import ImageTk, Image
import os
import tkinter.constants
import cv2
import matplotlib.image as matImg
import numpy as np
import matplotlib.pyplot as plt
#matplotlib.use('Agg')
from TopButtonSelect import TopButtonSelect
from CreateMenu import CreateMenu
from ShowPicture import ShowPicture
from OpenPicture import OpenPicture
from OpenAnswer import OpenAnswer
from Buttons import Buttons
from MakePicPath import MakePicPath
from SavePicture import SavePicture


class Interface:

    def __init__(self):

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


def page1():
    self.fileName = "C:\\Users\\ANDISHASAZAN\\PycharmProjects\\optical\\venv\\Include\\images_test\\test1.jpg"
    self.file_answer = "Answer_key.xlsx"
    self.new_fileName = "C:\\Users\\ANDISHASAZAN\\PycharmProjects\\optical\\venv\\Include\\images_test\\sample.jpg"

    self.cv = Canvas (root, bg='white')
    self.cv.pack (side="left", fill="both", expand="yes")

    image = Image.open (self.fileName)
    image = image.resize ((450, 450), Image.ANTIALIAS)
    self.img_0 = ImageTk.PhotoImage (image)
    self.def_image_0 = self.cv.create_image (50, 300, image=self.img_0, anchor='w')


root = Tk()
var = IntVar()
root.geometry("1400x650")

interface = Interface()
createMenu = CreateMenu()
tbs = TopButtonSelect()
showPic = ShowPicture()
openPic = OpenPicture(interface.fileName, interface.new_fileName)
openAns = OpenAnswer(interface.file_answer)
#openPic = OpenPicture(interface.fileName)
makePicPath = MakePicPath(interface.new_fileName)
#makePicPath = MakePicPath(interface.fileName)
savePic = SavePicture()
createMenu.creatMenu(root, tbs, openPic , openAns, showPic, interface, savePic, makePicPath)
buttons = Buttons(root, tbs, interface, makePicPath, showPic, openPic, var , openAns)
buttons.topButton()
buttons.nextButton()
#buttons.botButton()
#buttons.continueButton()


root.mainloop()






