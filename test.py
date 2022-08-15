from logging import root
import os
from tkinter import filedialog
import PyPDF2

root.directory = filedialog.askdirectory()

route = root.directory+'/'

constancias = os.listdir(route)

for constancia in constancias:
    pdfFileObject   = open(route+constancia,'rb')
    pdfReader       = PyPDF2.PdfFileReader(pdfFileObject)
    pageObject      = pdfReader.getPage(0)
    text            = pageObject.extractText()
    textLength      = len(text)
    accountNumber   = ""

    for letter in range(textLength):
        if text[letter]=="E" and text[letter+1]=="R" and text[letter+2]=="I" and text[letter+3]=="E":
            accountNumber = text[letter+4:letter+10]
            accountNumber = accountNumber.strip()
            pdfFileObject.close()

            os.rename(route+constancia,route+accountNumber+'.pdf')