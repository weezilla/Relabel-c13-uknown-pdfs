import PyPDF2
import pyexcel as pe
import pyexcel.ext.xlsx
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.rl_config import defaultPageSize
from reportlab.platypus import SimpleDocTemplate, Image
import StringIO,  sys
import getpass
pageHeight=defaultPageSize[1]; pageWidth=defaultPageSize[0]
user = getpass.getuser()
dirPath = 'C:/Users/'+ user + '/Dropbox/Lab Stuff/Che344/c13/'
nameOfOutput = dirPath + sys.argv[1]
pagesToPull = sys.argv[2:]

packet = StringIO.StringIO()
can = canvas.Canvas(packet,pagesize=letter)

unknownList = pe.get_sheet(file_name=dirPath + "unknowns2016spring.xlsx")
#print(unknownList[3,1])
index=0
while unknownList[index,1]:
	print unknownList[index,1]
	drawOverlay(can,unknownList[index,1],unknownList[index,0])
	
	index=index+1


#Takes sample name and excel sheet and returns the unknown number
def resolveUnknownNumber():
	pass

def drawOverlay(aCanvas,fileName,unknownNumber):
	aCanvas.setFont('Helvetica',14)
	aCanvas.setFillColorRGB(1,1,1)
	aCanvas.setStrokeColorRGB(0,0,0)
	aCanvas.rect(0,0,pageWidth*0.2,pageHeight*.5, fill=1)
	aCanvas.rotate(90)
	aCanvas.setFillColorRGB(0,0,0)
	aCanvas.setStrokeColorRGB(0,0,0)
	aCanvas.drawString(1*inch,1*-inch, unknownNumber)
	aCanvas.showPage()
	aCanvas.save()
	packet.seek(0)
drawOverlay(can)

pyObjPDF = open(dirPath + '/c13 unknown list and spectra(2014).pdf','rb')
pyPDF2File1 =PyPDF2.PdfFileReader(pyObjPDF)
pyPDF2File2 =PyPDF2.PdfFileReader(packet)
pageObj=pyPDF2File1.getPage(0)
pageObj2=pyPDF2File2.getPage(0)
pageObj.mergePage(pageObj2)
pyPDF2write = PyPDF2.PdfFileWriter()
pyPDF2write.addPage(pageObj)
pyObjTargetPDF=open(dirPath + 'mergePath.pdf','wb')
pyPDF2write.write(pyObjTargetPDF)
pyObjTargetPDF.close()
pyObjPDF.close()


#https://automatetheboringstuff.com/chapter13/
#https://www.binpress.com/tutorial/manipulating-pdfs-with-python/171
#https://www.reportlab.com/docs/reportlab-userguide.pdf
#http://stackoverflow.com/questions/1180115/add-text-to-existing-pdf-using-python
#http://www.tylerlesmann.com/2009/jan/28/writing-pdfs-python-adding-images/
#https://www.binpress.com/tutorial/manipulating-pdfs-with-python/167
#
