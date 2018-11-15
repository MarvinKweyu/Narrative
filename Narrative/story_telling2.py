#!/bin/python3

#takes user input,changes content in an existing file
# to match input and makes a new file of it saving it as a pdf and displaying it with
# an option to send to the otehr game participants

import PyPDF2
import fileinput
import subprocess

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image

class Application(object):
    'This is for a story'

    def __init__(self,play_file,name):
        self.play_file = play_file
        self.name = name
        self.get_information()

    def get_information(self):
        '''Open the pdf file ,edit and write edited work to a new file
        Has two text files; intermediate_txt(has words extracted) and final_text(has words changed)'''

        self.replacement_words = {'Sakura':self.name,
                                 'SAKURA':self.name.upper(),
                                 'Melvin':'Emmanuel'
                            }

        self.file =  PyPDF2.PdfFileReader(open(self.play_file,'rb'))
        self.pdf_writer = PyPDF2.PdfFileWriter()#create blank pdf

        print("Creating intermediate text...")
        self.intermediate_txt = open('intermediate.txt','a')
        print("Extracting text...")

        for current_page in range(1,self.file.numPages):
            self.page_obj = self.file.getPage(current_page)
            self.content = self.page_obj.extractText() #file name
            self.intermediate_txt.write(self.content)

        self.intermediate_txt.close()

        # self.pdf_writer.addPage(self.page_obj)

        #open text file to write into and append content
        print("Creating new file...")
        self.new_output_file = open('final_text.txt','w')
        # takes file name as self.content
        print("Adding new content...")
        for line in fileinput.input('intermediate.txt',inplace=False):
            line=line.rstrip()
            if not line:
                continue
            for key in self.replacement_words.keys():
                if key in line:
                    line=line.replace(key,self.replacement_words[key])
            self.new_output_file.write(line+"\n")
        self.new_output_file.close()
        print("Your file has been written successfully")
        self.convert_to_pdf()

    def display(self):
        'Show the information to user with default application on PC'
        print("Opening file...")
        subprocess.Popen(['dolphin','OurGameStory.pdf'])


    def convert_to_pdf(self):
        'take the final text and convert to pdf'

        print("Generating PDF...")
        self.text_file = open("final_text.txt", "r")  # text file I need to convert
        self.lines = self.text_file.readlines()
        self.text_file.close()
        self.i = 750
        self.num_of_lines = 0
        self.my_pdf = canvas.Canvas('OurGameStory.pdf') #the pdf created

        while self.num_of_lines < len(self.lines):
            if self.num_of_lines - len(self.lines) < 65: # I'm gonna write every 65 lines because I need it like that
                self.i=750
                for self.line in self.lines[self.num_of_lines:self.num_of_lines+65]:
                    self.my_pdf.drawString(15, self.i, self.line.strip())
                    self.num_of_lines += 1
                    self.i -= 12
                self.my_pdf.showPage()
            else:
                self.i = 750
                for self.line in self.lines[self.num_of_lines:]:
                   canvas.drawString(15, self.i, self.line.strip())
                   self.num_of_lines += 1
                   self.i -= 12
                self.my_pdf.showPage()
        print("Saving...")
        self.my_pdf.save()
        print("Done...")
        self.display()


#main
def main():
    internal_file = 'Romance/A_Secret_Kiss.pdf'
    name = input("Enter your name: ").lower().capitalize()
    new_user = Application(internal_file,name)
    return
main()
