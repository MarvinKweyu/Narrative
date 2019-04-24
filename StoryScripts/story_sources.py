#!/bin/python3

"""
Takes user input,changes content in an existing file
to match input and makes a new file of it saving it as a pdf and displaying it with
an option to send to the other game participants.
"""
import os
import fileinput
from typing import Union, Dict, Any

import PyPDF2
from reportlab.pdfgen import canvas


class NewStory(object):
    """Backend for story mania GUI."""

    def __init__(self):
        """Initialize the genre and one character for now."""
        # self.genre = genre
        # self.main_character = main_character
        # self.get_information()

    def get_information(self,genre,main_character):
        """Open the pdf file ,edit and write edited work to a new txt file
        Has two text files; intermediate_txt(has words extracted) and
        final_text(has words changed)
        :rtype: file called final_text"""

        replacement_words: Dict[str, Any] = {'Alaina': main_character}  # local
        # genres paths
        adventure = os.path.join('..', 'Genre', 'Adventure', 'adventure.pdf')
        romance = '../Genre/Adventure/romance.pdf'
        thriller = '../Genre/Thriller/thriller.pdf'
        # get path of genre
        if genre == 'adventure':
            play_file = adventure
        elif genre == 'romance':
            play_file = romance
        else:
            play_file = thriller

        self.file = PyPDF2.PdfFileReader(open(play_file, 'rb'))
        self.pdf_writer = PyPDF2.PdfFileWriter()  # create blank pdf

        # Creating intermediate text
        self.intermediate_txt = open((os.path.join('..', 'Programfiles', 'Intermediates', 'intermediate.txt')), 'a')

        # Extracting text from after cover page to the last
        for current_page in range(1, self.file.numPages):
            self.page_obj = self.file.getPage(current_page)
            self.content = self.page_obj.extractText()  # file name
            self.intermediate_txt.write(self.content)

        self.intermediate_txt.close()

        # self.pdf_writer.addPage(self.page_obj)

        # open text file to write into and append content
        self.new_output_file = open('../Programfiles/Finaltexts/final_text.txt', 'w')
        # takes file name as self.content
        # print("Adding new content...")
        for line in fileinput.input('../Programfiles/Intermediates/intermediate.txt', inplace=False):
            line = line.rstrip()
            if not line:
                continue
            for key in replacement_words:
                if key in line:
                    line = line.replace(key, replacement_words[key])
            self.new_output_file.write(line + "\n")
        self.new_output_file.close()
        # print("Your file has been written successfully")
        # self.convert_to_pdf()
        self.new_output_file = open('../Programfiles/Finaltexts/final_text.txt', 'r')
        return self.new_output_file


    def convert_to_pdf(self):
        """Take the final text and convert to pdf for saving."""
        print("Generating PDF...")
        # text file I need to convert
        self.text_file = open("../Programfiles/Finaltexts/final_text.txt", "r")
        self.lines = self.text_file.readlines()
        self.text_file.close()
        self.i = 750
        self.num_of_lines = 0
        self.my_pdf = canvas.Canvas('../UserPdfFiles/OurGameStory.pdf')  # the pdf created

        while self.num_of_lines < len(self.lines):
            # I'm gonna write every 65 lines because I need it like that
            if self.num_of_lines - len(self.lines) < 65:
                self.i = 750
                for self.line in self.lines[self.num_of_lines:self.num_of_lines + 65]:
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
        # self.display()
