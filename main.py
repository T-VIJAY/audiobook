import PyPDF2
import pyttsx3

book = open('DS notes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(4, pages):
    page =pdfReader.getPage(4)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
