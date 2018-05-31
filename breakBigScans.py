import minecart
import PyPDF2
import cv2

#write a method "getPDFPage Color that iterates through the bigPDF and outputs the 
#color of each page, making the association between index and the page color (looking for a way to 
#flag PDF pages by color.
filePath=r"C:/Users/ericm/Desktop/bigScans/bigScan1.pdf"
pdfFileObj = open(filePath, 'rb')
imageObj = cv2.imread(filePath)
cv2.imshow('image', imageObj)
pdfReader = PyPDF2.PdfFileReader(filePath, "rb")
pdfLength = pdfReader.getNumPages()
pageObj = pdfReader.getPage(0)
print(pageObj)
doc = minecart.Document(open(filePath,  'rb'))
i=0
pageList = []
while i <=pdfLength:
    page = doc.get_page(i)
    pageList.append(page)
    i=i+1





    
  

    
   
