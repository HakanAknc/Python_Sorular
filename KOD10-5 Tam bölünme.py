#Kullanıcıdan 5'e tam bölünen bir sayı alıncaya kadar devam edecek sonsuz while döngüsünü yazınız
a = int(input("Bir sayı giriniz"))
while True:
    if a%5==0:
        print("5'in katıdır")
        break
    else:
        a = int(input("Bir sayı giriniz"))
        print(a)
