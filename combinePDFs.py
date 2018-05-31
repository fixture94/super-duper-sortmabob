import PyPDF2, os,  minecart
def get_1pagePDF(reader,  pageNum):
    pdfWriter = PyPDF2.PdfFileWriter()
    singlepagePDF = open('pdfpage' + str(pageNum)+ '.pdf',  'wb')
    pageObj = reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    pdfWriter.write(singlepagePDF)
    singlepagePDF.close()
    return singlepagePDF
#as is, this code opens a pdf as a pdfReader object, and I have selected a single PDF page. Next step will be to add multiple pages at a time to the smaller PDFs of interest. 
pdfFiles = [] #defines an array that will consist of all pdfs in a particular directory
#this code adds filenames to that array of pdfFiles IF the filename is a PDf
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
#now, we loop back through that array of fileames and define each named file as a pdfReader object, which can then be cycled through to look at each page individually.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #we cycle through the pdfReader object here, in a FOR loop that is bounded by the number of pages in our particular named file...
    #TODO: for each page object, convert into a JPEG to extract RGB values... ths
    for pageNum in range(pdfReader.numPages):
        get_1pagePDF(pdfReader, pageNum)
    
        

