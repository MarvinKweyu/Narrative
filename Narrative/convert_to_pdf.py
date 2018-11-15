#program reads content of a txt and converts to pdf


from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image

# .....
# ..... some exta code unimportant for this issue....
# ....


# here it is
text_file = open("Story.txt", "r")  # text file I need to convert
lines = text_file.readlines()
text_file.close()
i = 750
num_of_lines = 0
my_pdf = canvas.Canvas('Practice.pdf') #the pdf create

while num_of_lines < len(lines):
    if num_of_lines - len(lines) < 60: # I'm gonna write every 60 lines because I need it like that
        i=750
        for line in lines[num_of_lines:num_of_lines+60]:
            my_pdf.drawString(15, i, line.strip())
            num_of_lines += 1
            i -= 12
        my_pdf.showPage()
    else:
        i = 750
        for line in lines[num_of_lines:]:
           canvas.drawString(15, i, line.strip())
           num_of_lines += 1
           i -= 12
        my_pdf.showPage()
my_pdf.save()
