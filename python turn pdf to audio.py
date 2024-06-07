import PyPDF3
import pyttsx3
import pdfplumber

file = 'the-dictionary-of-body-language.pdf'
book = open(file, 'rb')
pdfreader = PyPDF3.PdfFileReader(book)

pages = pdfreader.numPages

finaltext = ""

with pdfplumber.open(file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        finaltext += text
        
engine = pyttsx3.init()        
engine.save_to_file(finaltext, 'body luaguge.mp3')
engine.runAndWait()