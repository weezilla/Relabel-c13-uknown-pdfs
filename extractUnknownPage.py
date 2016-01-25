import PyPDF2
import sys
pagesToPull = sys.argv[2:]
nameOfOutput = 'C:/Users/weezy/Dropbox/Lab Stuff/Che344/c13/'+ sys.argv[1]

#pdf1 = open('C:\Users\weezy\Dropbox\Lab Stuff\Che344\c13 unknown list and spectra(2014).pdf','rb')
pdf1 = open('C:\Users\weezy\Dropbox\MESA STAR\TeX\V2\heburning_ma.pdf','rb')

pdf1Read=PyPDF2.PdfFileReader(pdf1)
pdfWrite = PyPDF2.PdfFileWriter()


for pageNum in pagesToPull:
	i=1
	pageObj=pdf1Read.getPage(int(pageNum)-1)
	pdfWrite.addPage(pageObj)
	pdfOutputFile=open(nameOfOutput+str(i)+'.pdf','wb')
	pdfWrite.write(pdfOutputFile)
	i = i+1
	pdfOutputFile.close()
#optional functionality: if file size is less than 75kb, delete it because it's blank page
pdf1.close()

#https://automatetheboringstuff.com/chapter13/
#https://www.binpress.com/tutorial/manipulating-pdfs-with-python/171