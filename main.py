# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

try:
    import Image
except ImportError:
    from PIL import Image

import pytesseract
import cv2
import time
from matplotlib import pyplot as plt
import numpy as np

import os

directory = "D:\point2tablet\Pictures"
directory2 = "D:\point2tablet"

file1 = open(os.path.join(directory2, "results.txt"), "w")
#file1.write("sdfasfdasdfasdfasdfasdfasdf")
file1.close

counter = 0
for file in os.listdir(directory):
    filename = os.path.join(directory, file)
    #hey = Image.open("D:\point2tablet\Pictures\\" + "2021-09-11T110559.709.png")
    #filename = " " + "2021-09-11T110559.709.png"
    image = cv2.imread(filename)

#    b,g,r = cv2.split(image)           # get b,g,r
#    rgb_img = cv2.merge([r,g,b])     # switch it to rgb

    # Denoising
    #dst = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)

#    b,g,r = cv2.split(dst)           # get b,g,r
#    rgb_dst = cv2.merge([r,g,b])     # switch it to rgb



    # read image file
    #img = cv2.imread("Plate_images/plate14.jpg")
    #img = dst
    img = image
#    cv2.imshow("Image", img)
#    cv2.waitKey(0)

    # RGB to Gray scale conversion
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#    cv2.imshow("1 - Grayscale Conversion", gray)
#    cv2.waitKey(0)

    # Noise removal with iterative bilateral filter(removes noise while preserving edges)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
#    cv2.imshow("2 - Bilateral Filter", gray)
#    cv2.waitKey(0)

    # thresholding the grayscale image
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#    cv2.imshow("3 - Thresh Filter", gray)
#    cv2.waitKey(0)

    # Dilation adds pixels to the boundaries of objects in an image
    #kernel = np.ones((5,5),np.uint8)
    #gray = cv2.dilate(gray, kernel, iterations = 1)
    #cv2.imshow("4 - dilation Filter", gray)
    # cv2.waitKey(0)

        #Basic OCR

    file1.write(pytesseract.image_to_string(gray, lang="rus", config="--psm 1"))
    counter = counter + 1
    print("+" + str(counter))

file1.close()
