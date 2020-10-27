import PyPDF2
import getpass
import sys

def join(archivos, filename="final.pdf"):
    PDFwriter = PyPDF2.PdfFileWriter()
    for archivo in archivos:
        fhand = open(archivo,"rb")
        pdfhand = PyPDF2.PdfFileReader(fhand)
        if(pdfhand.isEncrypted):
            password = getpass.getpass("Introduce la contraseña del PDF: ")
            pdfhand.decrypt(password)
        for numpagina in range(pdfhand.numPages):
            PDFwriter.addPage(pdfhand.getPage(numpagina))
    OutPutfile = open(filename,"wb")
    PDFwriter.write(OutPutfile)
    return 0

if __name__ == "__main__":
    files = sys.argv[2:]
    filename = sys.argv[1]
    join(files, filename)

