#Kullanıcının girdiği iki sayı arasındaki sayların toplamını gösteren kodu yazınız

bir = int(input("ilk sayıyı giriniz:"))
iki = int(input("İkinci sayıyı giriniz:"))
dizi = []
for i in range(bir,iki):
    dizi.append(i)
print(sum(dizi))

