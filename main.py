import cv2
import sys
#cv2 ve sys kütüphaneleri içe aktarılır.
if sys.platform =='win32':
    deltax = 0
    deltay = 0
else:
    deltax = 50
    deltay = 105
#İşletim sistemi kontrolü yapılır.
#Eğer işletim sistemi Windows ise deltax ve deltay değerleri 0 olarak atanır.
#Eğer işletim sistemi Windows değilse deltax ve deltay değerleri 50 ve 105 olarak atanır.
kamera = cv2.VideoCapture(0)
#Kamerayı başlatır ve video akışını alır.
#Kamera numarası olarak 0 kullanılır, yani varsayılan kamera kullanılır.
kamera.set(3,640)
kamera.set(4,480)
#Kamera ayarları yapılır (genişlik: 640, yükseklik: 480).
while True:
    _, kare = kamera.read()
#Kameradan bir kare alır ve _ ve kare değişkenlerine atanır.
#_ değişkeni, kamera.read() işlevinden dönen başarı durumunu temsil eder.
    gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
#Alınan kareyi gri tonlamalı görüntüye dönüştürür.
    blur = cv2.GaussianBlur(gri, (7, 7), 0)
#Gri tonlamalı görüntüye Gauss bulanıklığı uygular.
#(7, 7) boyutlu bir bulanıklık çekirdeği kullanılır.
    canny = cv2.Canny(blur, 30, 50)
#Gauss bulanıklığı uygulanan görüntüye kenar algılama (Canny) uygular.
#30 ve 50 parametreleri, kenar tespiti için eşik değerleridir.
    canny = cv2.bitwise_not(canny)
#Kenar algılama sonucunu tersine çevirir.
#Beyaz kenarlara sahip siyah bir arka plan oluşturur.
    imaj = cv2.bitwise_and(kare,kare, mask=canny)
#Orijinal kareyi kenar görüntüsüyle maskeleme işlemi yapar.
#Kenarlar dışındaki pikselleri siyah yapar.
    cv2.imshow('imaj', imaj)
    cv2.moveWindow('imaj', 10,10)
#İmajı görüntüler.
#'imaj' penceresini (10, 10) konumuna taşır.
    cv2.imshow('canny', canny)
    cv2.moveWindow('canny',imaj.shape[1]+deltax,10)
#Kenar görüntüsünü 'canny' adında bir pencerede görüntüler.
#'canny' penceresini (imaj.shape[1] + deltax, 10) konumuna taşır.
#imaj.shape[1] görüntünün genişliğini temsil eder.
    k = cv2.waitKey(1)
#Kullanıcının bir tuşa basmasını bekler.
#1 milisaniye boyunca bekler ve kullanıcının tuşa basması durumunda tuşun değerini k değişkenine atar.
    if k == 27 or k == ord('q'):
        break
#Eğer kullanıcı Escape (27) tuşuna veya 'q' tuşuna basarsa döngüyü sonlandırır.
kamera.release()
#Kamera kaynağını serbest bırakır.
#Kamera kullanımı tamamlandığında kaynakların serbest bırakılması önemlidir.
cv2.destroyAllWindows()
#Tüm açık OpenCV pencerelerini kapatır ve bellekten temizler.
#Kod çalışması tamamlandığında pencereleri kapatmak önemlidir.
