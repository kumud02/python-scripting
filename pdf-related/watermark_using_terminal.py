import sys
import getopt
import PyPDF2

file_to_be_watermarked = "super_duper.pdf"
watermark_file = "./pdf/wtr.pdf"
output_file = "watermarked_file.pdf"

argvs = sys.argv[1:]
# print(argvs)

try:
    opts, args = getopt.getopt(argvs, "f:w:o:")
    for opt, arg in opts:
        if opt in "-f":
            file_to_be_watermarked = arg
        elif opt in "-w":
            watermark_file = arg
        elif opt in "-o":
            output_file = arg
        else:
            print("invalid arguments")
            sys.exit
except(Exception):
    print("invalid arguments")
    sys.exit

try:
    template = PyPDF2.PdfFileReader(file_to_be_watermarked, "rb")
    watermark = PyPDF2.PdfFileReader(watermark_file, "rb")
    output = PyPDF2.PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)
except FileNotFoundError as e:
    print(str(e))
    sys.exit()

try:
    with open(output_file, "wb") as file:
        output.write(file)
        print("Please check the file", output_file)
except(OSError):
    print("Please check if if the file is open. Close the file and try again")
except FileNotFoundError as e:
    print(str(e))
