import pyttsx3
import PyPDF2

class Read:
    def __init__(self,filename,page):

        self.filename=filename
        self.page=page
    
    def Page(self):
        book=open(self.filename,'rb')
        #we used imported module of pdf2 to read the file
        pdf=PyPDF2.PdfFileReader(book)
        #called the reading module by setting up its constructor
        speaker=pyttsx3.init()
        #here we used setProperty of rate with an integer value which tells python that how much words will it say per minute
        speaker.setProperty("rate", 150)
        #here we get the page no
        page=pdf.getPage(self.page)
        #now extracting the text from that particular page
        text=page.extractText()
        speaker.say('hello word i am python now i am reading your desired page...')
        speaker.say(text)
        speaker.runAndWait()


#-----DriverCode---------
def Test(filename,pageno):
    r=Read(filename,pageno)
    r.Page()