sayi = int(input("Bir sayı giriniz:"))
if sayi == 0:
    print("Sayı sıfıra eşit")
elif sayi == 1:
    print("Sayı bire eşit")
elif sayi == 2:
    print("Sayi ikiye eşit")
else :
    print("Sayi 0,1,2'den farklı")


h = input("Bir isim giriniz:")
if h == "hakan":
    print("İsim HAKAN girildi")
else :
    print("İsim HAKAN girilmedi")


a = int(input("a sayısı:"))
b = int(input("b sayısı:"))
if a>b:
    print("a büyüktür b")
elif b>a:
    print("b büyüktür a")
else :
    print("a eşit b")
