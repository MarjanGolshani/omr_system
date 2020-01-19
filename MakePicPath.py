import os


class MakePicPath:
    def __init__(self, new_fileName):
        self.new_fileName = new_fileName

    def make(self, fileName, newSufix):
        filePath =os.path.split(fileName)
        str = os.path.splitext(filePath[1])
        new_pixname = str[0] + newSufix
        self.new_fileName = os.path.join(filePath[0], new_pixname).replace("\\","/")
        return self.new_fileName
