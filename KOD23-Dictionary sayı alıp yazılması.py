#Dictionary - Sözlük
#kullanıcıdan iki basamaklı sayı alınıp yazı ile yazılıması

dict_b = {1:"bir",2:"iki",3:"üç",4:"dört",5:"beş",6:"altı",7:"yedi",8:"sekiz",9:"dokuz",0:""}
dict_o = {1:"on",2:"yirmi",3:"otuz",4:"kırk",5:"elli",6:"altmış",7:"yetmiş",8:"seksen",9:"doksan",0:""}

sayi = input("İki basamaklı sayı giriniz:")

birler = int(sayi[1])   #35 --> 5
onlar = int(sayi[0])    #35 --> 3

print(dict_o[onlar],dict_b[birler])
