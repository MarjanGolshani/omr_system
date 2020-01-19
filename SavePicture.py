import os
from tkinter.filedialog import asksaveasfilename


class SavePicture:


    def saveAs(self, root, new_fileName, image):
        global options
        file_opt = options = {}
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt'), ('pix files', '.jpg'), ('pix files', '.jpeg'), ('pix files', '.png')]
        self.new_filePath =os.path.split(new_fileName)
        options['initialfile'] = self.new_filePath[1]
        options['parent'] = root
        filename = asksaveasfilename(**file_opt)

        if filename:
            image.save(filename)
