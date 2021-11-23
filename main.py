import PyPDF2

if __name__ == '__main__':
    with open('dummy.pdf', 'rb') as file:
        print(file)#<_io.TextIOWrapper name='dummy.pdf' mode='r' encoding='cp1252'>
        reader = PyPDF2.PdfFileReader(file)
        print(reader.numPages)#1
        page = reader.getPage(0)
        print(page)#{'/Type': '/Page', '/Parent': IndirectObject(4, 0)...
        page.rotateCounterClockwise(90)
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        with open('tilt.pdf', 'wb') as new_file:
            writer.write(new_file)


