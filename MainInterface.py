from copy import copy
import random
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import font  as tkfont
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

class Interface(tk.Frame):
    def __init__ (self, parent, controller):
        tk.Frame.__init__ (self, parent)
        self.controller = controller
        label = tk.Label (self, text="This is page 1", font=controller.title_font)
        label.pack (side="top", fill="x", pady=10)
        button = tk.Button (self, text="Go to the start page",
                            command=lambda: controller.show_frame ("StartPage"))

        self.fileName = "C:\\Users\\ANDISHASAZAN\\PycharmProjects\\optical\\venv\\Include\\images_test\\test1.jpg"
        self.file_answer = "Answer_key.xlsx"
        self.new_fileName = "C:\\Users\\ANDISHASAZAN\\PycharmProjects\\optical\\venv\\Include\\images_test\\sample.jpg"

        self.cv = Canvas (self, bg='white')
        self.cv.pack (side="left", fill="both", expand="yes")

        image = Image.open (self.fileName)
        image = image.resize ((450, 450), Image.ANTIALIAS)
        self.img_0 = ImageTk.PhotoImage (image)
        self.def_image_0 = self.cv.create_image (50, 300, image=self.img_0, anchor='w')

        image_1 = Image.open (self.new_fileName)
        image_1 = image_1.resize ((450, 450), Image.ANTIALIAS)
        self.img_1 = ImageTk.PhotoImage (image_1)
        self.def_image_1 = self.cv.create_image (1300, 300, image=self.img_1, anchor='e')

        button.pack ()

class SampleApp (tk.Tk):

    def __init__ (self, *args, **kwargs):
        tk.Tk.__init__ (self, *args, **kwargs)

        self.title_font = tkfont.Font (family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame (self)
        container.pack (side="top", fill="both", expand=True)
        container.grid_rowconfigure (0, weight=1)
        container.grid_columnconfigure (0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo ,Interface):
            page_name = F.__name__
            frame = F (parent=container, controller=self)
            self.frames [page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid (row=0, column=0, sticky="nsew")
        page_name = Interface.__name__
        interface = Interface (parent=container, controller=self)

        createMenu = CreateMenu ()
        tbs = TopButtonSelect ()
        showPic = ShowPicture ()
        openPic = OpenPicture (interface.fileName, interface.new_fileName)
        openAns = OpenAnswer (interface.file_answer)
        # openPic = OpenPicture(interface.fileName)
        makePicPath = MakePicPath (interface.new_fileName)
        # makePicPath = MakePicPath(interface.fileName)
        savePic = SavePicture ()
        createMenu.creatMenu (self, tbs, openPic, openAns, showPic, interface, savePic, makePicPath)
        var = IntVar ()
        buttons = Buttons (self, tbs, interface, makePicPath, showPic, openPic, var, openAns)
        buttons.topButton ()
        buttons.nextButton ()

        self.show_frame ("StartPage")

    def show_frame (self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames [page_name]
        frame.tkraise ()




class StartPage (tk.Frame):

    def __init__ (self, parent, controller):
        tk.Frame.__init__ (self, parent)
        self.controller = controller
        label = tk.Label (self, text="This is the start page", font=controller.title_font)
        label.pack (side="top", fill="x", pady=10)

        button1 = tk.Button (self, text="Go to Page One",
                             command=lambda: controller.show_frame ("Interface"))
        button2 = tk.Button (self, text="Go to Page Two",
                             command=lambda: controller.show_frame ("PageTwo"))

        button1.pack ()
        button2.pack ()


class PageOne (tk.Frame):

    def __init__ (self, parent, controller):
        tk.Frame.__init__ (self, parent)
        self.controller = controller
        label = tk.Label (self, text="This is page 1", font=controller.title_font)
        label.pack (side="top", fill="x", pady=10)
        button = tk.Button (self, text="Go to the start page",
                            command=lambda: controller.show_frame ("StartPage"))

        button.pack ()


class PageTwo (tk.Frame):

    def __init__ (self, parent, controller):
        tk.Frame.__init__ (self, parent)
        self.controller = controller
        label = tk.Label (self, text="This is page 2", font=controller.title_font)
        label.pack (side="top", fill="x", pady=10)
        button = tk.Button (self, text="Go to the start page",
                            command=lambda: controller.show_frame ("StartPage"))
        button.pack ()









#root = Tk()
#var = IntVar()
#root.geometry("1400x650")
app = SampleApp ()
app.mainloop ()
