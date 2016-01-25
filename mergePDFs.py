import PyPDF2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.rl_config import defaultPageSize
from reportlab.platypus import SimpleDocTemplate, Image
import sys
import getpass

pageHeight=defaultPageSize[1]; pageWidth=defaultPageSize[0]
user = getpass.getuser()
dirPath = 'C:/Users/'+ user + '/Dropbox/Lab Stuff/Che344/c13/'

can = canvas.Canvas(dirPath + 'overlay.pdf')
def drawOverlay(aCanvas):
	#aCanvas.translate(inch,inch)
	aCanvas.setFont('Helvetica',14)
	aCanvas.setFillColorRGB(1,1,1)
	aCanvas.setStrokeColorRGB(0,0,0)
	aCanvas.rect(0,0,pageWidth*0.2,pageHeight*.5, fill=1)
	aCanvas.rotate(90)
	aCanvas.setFillColorRGB(0,0,0)
	aCanvas.setStrokeColorRGB(0,0,0)
	aCanvas.drawString(1*inch,1*-inch, "link to unknown input from excel list")
	aCanvas.showPage()
	aCanvas.save()	
drawOverlay(can)

pyObjPDF = open(dirPath + '1-hexene1.pdf','rb')
pyObjPDF2 = open(dirPath + 'overlay.pdf','rb')
pyPDF2File1 =PyPDF2.PdfFileReader(pyObjPDF)
pyPDF2File2 =PyPDF2.PdfFileReader(pyObjPDF2)
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