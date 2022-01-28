import cv2
import numpy as np
import random
import albumentations as A
import os.path
import os

fotolar = os.scandir("/home/gursel/Desktop/pygurs")    # fotoğraflarımızın olduğu klasörümüzü ekledik


    
    
num_files = len([f for f in os.listdir("/home/gursel/Desktop/pygurs")if os.path.isfile(os.path.join("/home/gursel/Desktop/pygurs", f))])
eklenilen_foto = 0    

while True:
    
    foto_sayi = input("foto sayisini gir: ")            
    image = cv2.imread("/home/gursel/Desktop/pygurs/{}.jpg".format(foto_sayi)) # fotoğrafları tek tek for döngüsü sayesinde okuttuk
   # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # cv2.imshow("img{}".format(foto_sayi),image)
    eklenilen_foto += 1

    transform = A.Compose(
    [A.RandomRain(brightness_coefficient=0.9, drop_width=1, blur_value=5, p=1)],
    )
    random.seed(7)
    transformed = transform(image=image)



    
    cv2.imwrite("/home/gursel/Desktop/efektli/efektli_{}.jpg".format(foto_sayi),transformed['image'])
    
    if eklenilen_foto == num_files:
        break
    

    print(eklenilen_foto)

cv2.waitKey(0)
cv2.destroyAllWindows()

