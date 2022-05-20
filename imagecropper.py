import cv2
from pdf2image import convert_from_path, convert_from_bytes


pdfname = 'BMW118D' 
images = convert_from_path(f'./pdf/{pdfname}.pdf',150)

for i in range(len(images)):

	# Save pages as images in the pdf
	images[i].save(f'{pdfname}.png', 'PNG')

img = cv2.imread(f'{pdfname}.png')
cv2.imshow('image', img)
cv2.waitKey(0)

cropped = img[220:632, 810:1355]
cv2.imshow('image', cropped)
cv2.waitKey(0)

cv2.imwrite(f'./{pdfname}-cropped.png', cropped)
cv2.destroyAllWindows()