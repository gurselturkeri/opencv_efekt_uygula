import cv2
import random
import albumentations as A
import os

fotolar = os.scandir("/home/gursel/Desktop/pygurs")    # fotoğraflarımızın olduğu klasörümüzü ekledik


for i in fotolar: 

    adet = i.name        # klasördeki her dosyanin adini aldık                   
    image = cv2.imread("/home/gursel/Desktop/pygurs/{}".format(adet)) # fotoğrafları tek tek for döngüsü sayesinde okuttuk
    
    # cv2.imshow("img{}".format(adet),image)
    
    """
 
    Her adet dögüsü için farklı bir image değişkeni kaydetmek istiyorum.
    örneğin ilk fotoyu read ettikten sonra onu onu "image1" değişkeninde saklasın 

    """
    # rain effect kod kısmı
    transform = A.Compose(                                               
    [A.RandomRain(brightness_coefficient=0.9, drop_width=1, blur_value=5, p=1)],)
    random.seed(7)
    transformed = transform(image=image)

    cv2.imwrite("/home/gursel/Desktop/pygurs/with_effect/rain_{}".format(adet),image)



  
  
cv2.waitKey(0)
cv2.destroyAllWindows()

