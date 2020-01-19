from tkinter.filedialog import askopenfilename
import os
from PIL import Image, ImageTk


class OpenAnswer:

    def __init__(self, file_answer ):
        self.file_answer = file_answer


    def select(self, root, interface):
        self.file_answer = askopenfilename()

#        root.mainloop()
    def openFile(self, root, showPic, interface):
        self.fileName = askopenfilename()
        showPic.showOrgPix(self.fileName, interface)
#        root.mainloop()


    def openFileAgain(self, root, showPic, interface):
        self.fileName_1 = askopenfilename()
        showPic.showNewPix(self.fileName_1, interface)



