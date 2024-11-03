import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'


img=cv2.imread('car1.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gray,170,200)
cv2.imshow('frame',canny)
contours,new=cv2.findContours(canny.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
contours=sorted(contours,key=cv2.contourArea,reverse=True)[:30]

for contour in contours:
    perimeter=cv2.arcLength(contour,True)
    approx=cv2.approxPolyDP(contour,0.01*perimeter,True)
    print(len(approx))
    if len(approx)== 4:
        x,y,w,h = cv2.boundingRect(contour)
        license_plate=gray[y:y+h,x:x+w]
        cv2.imshow('frame2',license_plate)
        break

    
license_plate=cv2.threshold(license_plate,127,255,cv2.THRESH_BINARY)[1]
cv2.imshow('frame1',license_plate)
bilateral=cv2.bilateralFilter(license_plate,11,17,17)
text=pytesseract.image_to_string(bilateral)



image=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
image = cv2.putText(img, text, (x-100,y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
print('licensePlate',text)
cv2.waitKey(0)


        
