import os
path = '/home/gursel/Desktop/2022/sola_donulmez'        # dosya yolunu ekle
files = os.listdir(path)


for index, file in enumerate(files):       # klasördeki dosyların sayısal değerlerleri kadar for döngüsünü çalıştır
    os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.jpg'])))         # dosyaların adını 0dan 1e kadar değiştir 
