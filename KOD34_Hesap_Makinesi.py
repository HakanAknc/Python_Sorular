#Python: Eval Formülü Nasıl Kullanılır? Basit Bir Hesap Makinesi Uygulaması.
print("""
Basit bir hesap makinesi uygulaması.
İşleçler:
+ toplama
- çıkarma
* çarpma
/ bölme
Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23 * 46 yazdıktan sonra
ENTER tuşuna basın.)
""")
while True:
    veri=input("Lütfen işleminizi giriniz. Eğer t yazarsanız işlemi bitirir.")
    if veri=="t":
        break
    hesap = eval(veri)
    print(hesap)