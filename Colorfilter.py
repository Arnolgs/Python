"""
File: colorfilter.py
Project 7.9

Defines and tests a function for color filtering.  Uses this
function to define functions for lightening and darkening images.
"""

from images import Image

def colorFilter(image, rgbTriple):
    def baseValue(value, offset):
        if offset == 0:
            return value
        elif offset < 0:
            return max(value + offset, 0)
        else:
            return min(value + offset, 255)

    (r, g, b) = rgbTriple
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (red, green, blue) = image.getPixel(x, y)
            (red, green, blue) = (baseValue(red, r), baseValue(green, g),baseValue(blue, b))
            image.setPixel(x, y, (red, green, blue))  

def lighten(image, amount):
    colorFilter(image, (amount, amount, amount))
        

def darken(image, amount):
    colorFilter(image, (-amount, -amount, -amount))   
            

def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    #lighten(image, 20) example
    #darken(image2, 64) example
    colorFilter(image3, (255, 0, 0)) #example
    image.draw()

if __name__ == "__main__":
   main()


