from tkinter.filedialog import askopenfilename
import os
from PIL import Image, ImageTk


class OpenPicture:

    def __init__(self, fileName , fileName_1):
        self.fileName = fileName
        self.fileName_1 = fileName_1

    def openFile(self, root, showPic, interface):
        self.fileName = askopenfilename()
        showPic.showOrgPix(self.fileName, interface)
#        root.mainloop()


    def openFileAgain(self, root, showPic, interface):
        self.fileName_1 = askopenfilename()
        showPic.showNewPix(self.fileName_1, interface)
#        root.mainloop()
