#Fonksiyonlar
#def_fonksiyon adi(parametre):
#    """fonksiyon açıklaması"""
#    islemler
#    return s
#ilk_fonksiyon() tanımlanmadan önce çağırılmaz
def ilk_fonksiyon():
    """Bu fonksiyon bizim ilk fonksiyonumuz"""
    print("Fonksiyon tanımlandı")

ilk_fonksiyon()  #tanımlamadan sonra çağırılır
print(ilk_fonksiyon.__doc__)

def merhaba(isim):
    print("Merhaba",isim)
merhaba("Hakan")

def topla(a,b):
    return  a + b
print(topla(8,9))

