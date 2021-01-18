import cv2 as cv
import pyttsx3           
import googletrans
import pytesseract

img = cv.imread('test.png', 0)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

ret, img_binary = cv.threshold(img,100, 255, cv.THRESH_BINARY)

text = pytesseract.image_to_string(img_binary)

p = googletrans.Translator()                       
k = p.translate(text,src='tr', dest='en') 
translated = str(k.text)

with open('translate.txt',mode ='w') as file:    
    file.write("Türkçe:\n"+text)
    print("\nTürkçe:\n")
    print(text)
    file.write("\nEnglish:\n"+translated)
    print("\nEnglish:\n")
    print(translated)


engine = pyttsx3.init() 
engine.say(translated) 
engine.runAndWait()

cv.imshow("Resim",img)
cv.waitKey(0)
cv.destroyAllWindows()
