baslangic = int(input("Başlangıç sayısını giriniz:"))
bitis = int(input("Bitiş sayısını giriniz:"))

tektoplam = cifttoplam = 0
teksayac = ciftsayac = 0

while baslangic<bitis:
    if baslangic%2==0:
        cifttoplam += baslangic
        ciftsayac += 1
    else:
        tektoplam += baslangic
        teksayac += 1
    baslangic += 1

ciftort = cifttoplam / ciftsayac
tekort = tektoplam / teksayac

print("çift toplam",cifttoplam)
print("çift adet",ciftsayac)
print("çift ortalama",ciftort)
print("tek toplam",tektoplam)
print("tek adat",teksayac)
print("tek ortalam",tekort)
