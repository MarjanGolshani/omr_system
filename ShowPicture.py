from PIL import Image, ImageTk


class ShowPicture:

    def showNewPix(self, fileName, interface):
        self.image_1 = Image.open(fileName)
        self.image_1 = self.image_1.resize((450, 450), Image.ANTIALIAS)
        self.img_1 = ImageTk.PhotoImage(self.image_1)
        interface.cv.itemconfigure(interface.def_image_1, image=self.img_1)


    def showOrgPix(self, fileName, interface):
        self.image_0 = Image.open(fileName)
        self.image_0 = self.image_0.resize((450, 450), Image.ANTIALIAS)
        self.img_0 = ImageTk.PhotoImage(self.image_0)
        interface.cv.itemconfigure(interface.def_image_0, image=self.img_0)
