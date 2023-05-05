# 0 VE 50 ARASINDA 10 SAYI ÜRETSİN BUNLARI BİR DİZİYE ATSIN İÇİNDEKİ SAYILARI 5'E BÖLÜNENLERİ FARKLI
#BİR DİZİYE ATSIN 4'E BÖLÜNENLERİ BİR DİZİYE ATSIN SONRA BU DİZİLERİ TOPLANICAK

# 1'inci çözüm
import random
dizi = [random.randint(0,50) for i in range(10)]
print(dizi)
dort = list(filter(lambda x:x%4==0,dizi))
bes = list(filter(lambda x:x%5==0,dizi))
print(dort)
print(bes)
print(sum(dort))
print(sum(bes))


#2'inci çözüm
print("")
dizi = []
for i in range(10):
    dizi.append(random.randint(0,50))
print(dizi)
dort = list(filter(lambda x:x%4==0,dizi))
bes = list(filter(lambda x:x%5==0,dizi))
print(dort)
print(bes)
print(sum(dort))
print(sum(bes))
