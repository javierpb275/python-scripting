import PyPDF2
import sys

inputs = sys.argv[1:]#grab all we write in the console into a list of inputs

if __name__ == '__main__':
    def pdf_combiner(pdf_list):
        merger = PyPDF2.PdfFileMerger()
        for pdf in pdf_list:
            print(pdf)
            merger.append(pdf)
            merger.write('super.pdf')

    pdf_combiner(inputs)

