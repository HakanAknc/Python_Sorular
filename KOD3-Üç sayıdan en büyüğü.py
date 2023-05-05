# 3 sayıdan en büyüğü

a = int(input("a sayı giriniz:"))
b = int(input("b sayı giriniz:"))
c = int(input("c sayı giriniz:"))
if a>b and a>c:
    print("En büyük sayı a =",a)
elif b>a and b>c:
    print("En büyük sayı b =",b)
else:
    print("En büyük sayı c =",c)

print("********************")

#sıfırdan büyük küçük işemi
sayi = int(input("Bir sayı giriniz:"))
while sayi >= 0:
    if sayi == 0:
        print("Sayı sıfıra eşittir.")
    elif sayi > 0:
        print("Sıfrdan büyük bir sayı.")
    else:
        print("Bir tam sayı giriniz")
    break
