import minecart

def get_main_color(img):
    width, height = img.size
    colors = img.getcolors(width * height) #put a higher value if there are many colors in your image
    max_occurence, most_present = 0, 0
    try:
        for c in colors:
            if c[0] > max_occurence:
                (max_occurence, most_present) = c
        return most_present
    except TypeError:
        raise Exception("Too many colors in the image")

pdffile = open("pdfpage0.pdf",  "rb")
doc = minecart.Document(pdffile)
page=doc.get_page(0)
image = page.images[0].as_pil()
main_color = get_main_color(image)
print(main_color)

#color=get_main_color(image)
#print(color)
#width,  height = image.size
#print(image.format_description  )
#image.save('pdfpage0.jpg')



#image.show()
#filename = "testimage1.jpeg"
#
#with open(filename, 'w') as file_object:
#    file_object.write(image)
