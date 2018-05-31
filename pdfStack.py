class PdfStack(): 
    """Represents a stack of pages that are saved in the PDF Format. An instance of this class would have attributes describing its
    path, the number of pages in the stack, and """
    def __init__(self,  filePath, numPages):
       """initialize attributes of the parent class"""
       self.filePath = filePath
       self.numPages = numPages
       
       
        
