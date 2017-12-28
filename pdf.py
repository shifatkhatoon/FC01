from fpdf import FPDF
import cv2
import glob
import os
pdf = FPDF()

print(os.path.dirname(os.path.abspath(__file__)))
filenames = glob.glob(os.path.dirname(os.path.abspath(__file__))+'/Stldakash/*')
print(filenames)
i=1
for f in sorted(filenames):
    gray = cv2.imread(f,0)
    retval, thresh_gray = cv2.threshold(gray, thresh=120, maxval=255, type=cv2.THRESH_BINARY)
    cv2.imwrite('{}.png'.format(i),thresh_gray)
    pdf.add_page("L")
    pdf.image('{}.png'.format(i), x=0, y=0, h=210, w=297, type = '', link = '')
    i+=1
for i in glob.glob("*.png"):
    os.remove(i)
pdf.output('stldakash.pdf', 'F')