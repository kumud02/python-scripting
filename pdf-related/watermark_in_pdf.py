import PyPDF2
import os

template = PyPDF2.PdfFileReader("super_duper.pdf", "rb")
watermark = PyPDF2.PdfFileReader("./pdf/wtr.pdf", "rb")
output = PyPDF2.PdfFileWriter()


for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

try:
    with open("watermarked_file.pdf", "wb") as file:
        output.write(file)
except(OSError):
    print("Please check if if the file is open. Close the file and try again")
