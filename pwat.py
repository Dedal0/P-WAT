#import find_pdfrw
from pdfrw import PdfReader, PdfWriter
from pdfminer.pdfparser import PDFParser, PDFDocument    
import sys
import os


END = "\033[0m"
blue = "\033[0;34m"
red = "\033[1;91m"
green = "\033[1;32m"



def readpdf():
	fp = open(pdf, 'rb')
	parser = PDFParser(fp)
	doc = PDFDocument()
	parser.set_document(doc)
	doc.set_parser(parser)
	doc.initialize()
	print blue + "Info Extraida del PDF:" + "\n" + END
	print green
	print str(doc.catalog) + "\n"
	print str(doc.info)
	print END

def writepdf():
	outfn = 'pwat.' + os.path.basename(pdf)
	trailer = PdfReader(pdf)
	trailer.Info.Creator = 'NOT'
	trailer.Info.Author = 'NOT'
	trailer.Info.Title = 'NOT'
	trailer.Info.Producer = 'NOT'
	trailer.Info.CreationDate = '6/6/6'
	trailer.Info.ModDate = '6/6/6'
	writer = PdfWriter()
	writer.trailer = trailer
	writer.write(outfn)


def accion():
	if action == "read":
		readpdf()
	elif action == "write":
		writepdf()
	else:
		print red + "Escoja una accion conocida" + END


def existef():
	if existe == True:
		accion()
	else:
		print red + "Ese archivo no existe" + END

def helppdf():
	print red
	print "======= Modo de uso: =======" + END
	print green + "python pwat.py file.pdf" + END + blue + " opcion" + END
	print red + "opciones:" + END
	print blue + "read:" + END + " leer la metadata del pdf"
	print blue + "write:" + END + " sobreescribir la metadata en un nuevo archivo con prefijo pwat."


if len(sys.argv) < 3:
	helppdf()
else:
	pdf = sys.argv[1]
	action = sys.argv[2]
	existe = os.path.isfile(pdf)
	existef()
