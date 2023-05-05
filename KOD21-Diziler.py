dizi = [0,1,2,3,4,5,6,7,8,9]

dizi[0] = 5

print(dizi)
print(dizi[0],dizi[2])
print(dizi[1])
print(dizi[0:5])
print(dizi[3:7])
print(dizi[:3])  #başlangıçdan 3'e kadar yazar
print(dizi[4:])  #5'den sonuncuya kadar yazaz
print(dizi[-1])  #en sonuncu sayıyı yazdırır
print(dizi[-2])

print(len(dizi))  #dizi uzunluğu (len=uzunluk)

#string diziler
sdizi = ["elma","armut","portakal","muz"]
print(sdizi[0])

sdizi.append("üzüm")  #yazdığınız değeri listeye ekler
print(sdizi)

del sdizi[1]  #armut elamanı siliniyor
print(sdizi)

sdizi.remove("portakal")  #elemanı kaldırma
print(sdizi)

sdizi.pop(2)  #indis numarası ile silme
print(sdizi)

sdizi += ["armut","üzüm","portakal"]  #diziye geri ekleme
print(sdizi)

sdizi *= 2   #bütün elelmanları ikiyle çarpar
print(sdizi)

sayilar = [21,34,56,78,23,15,49,62,21]

sayilar.sort()  #dizideki sayıları küçükten büyüğe sıralar
print(sayilar)

sayilar.reverse()  #dizideki sayıları büyükten küçüğe sıralar
print(sayilar)

a = sayilar.count(21)  #dizideki aynı eleman kaç kere tekrar etmiş
print(a)

sayilar.clear()  #dizideki bütün elemanları siliyor
print(sayilar)

sayilar.insert(0,12)  #dizinin içine ekleme yapar
sayilar.insert(1,34)
sayilar.insert(1,23)
print(sayilar)

#2 boyutlu dizler (matris)
matris = [[1,3,6],[0,3,2],[2,7,3]]   # 1 3 6
print(matris)                        # 0 3 2
print(matris[0])                     # 2 7 3
print(matris[0][2])
