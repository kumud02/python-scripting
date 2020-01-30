import PyPDF2
import os


merger = PyPDF2.PdfFileMerger()
try:
    for root, dirs, files in os.walk("./pdf"):
        for each_file in files:
            if each_file.endswith('.pdf'):
                print(each_file)
                merger.append("./pdf/"+each_file)
        merger.write("super_duper.pdf")
except(OSError):
    print("Please Check if the file is opened, close it and try again")
