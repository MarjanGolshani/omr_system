from tkinter import *
import os

class CreateMenu:

    def __init__(self):
        pass



    def creatMenu(self, root, tbs, openPic , openAns, showPic, interface, savePicture, makePicPath):
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Open New Answer Sheet", command= lambda :openPic.openFile(self, showPic, interface))
        filemenu.add_command(label="Select Answer Key", command= lambda :openAns.select(root , interface))

        filemenu.add_command(label="Save as", command= lambda :savePicture.saveAs(root, makePicPath.new_fileName, showPic.image_1))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)

        taskmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label = "Task", menu = taskmenu)
        
        taskmenu.add_command(label = "Show correct form", command = lambda :tbs.setTask(1))
        taskmenu.add_command(label = "Show correct form(Scan)", command = lambda :tbs.setTask(3))
        taskmenu.add_command(label = "Show correct form in a file", command = lambda :os.startfile (r'styled.xlsx'))
        taskmenu.add_command(label = "Show Answer Key!", command = lambda : os.startfile((openAns.file_answer)))
        taskmenu.add_command(label = "Score", command = lambda :tbs.setTask(2))




        root.config(menu=menubar)
