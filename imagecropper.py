from ast import Str
import cv2
from pdf2image import convert_from_path
import argparse


parser = argparse.ArgumentParser(description='python3 imagecropper.py pdfname.pdf')
parser.add_argument('name')
args = parser.parse_args()
print(args.name)
pdfname = args.name
images = convert_from_path(f'./pdf/{pdfname}.pdf',150)

for i in range(len(images)):
	images[i].save(f'./png/{pdfname}.png', 'PNG')

img = cv2.imread(f'./png/{pdfname}.png')
cv2.imshow('image', img)
cv2.waitKey(0)

cropped = img[220:632, 810:1355]
cv2.imshow('image', cropped)
cv2.waitKey(0)

cv2.imwrite(f'./cropped-img/{pdfname}-cropped.png', cropped)
cv2.destroyAllWindows()