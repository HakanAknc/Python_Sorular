sayi1 = int(input("Sayi1:"))
sayi2 = int(input("Sayi2:"))
print(sayi1,"ile",sayi2,"arasındaki asal sayılar:")
for sayi in range(sayi1,sayi2 + 1):
    if sayi > 1:
        for i in range(2,sayi):
            if (sayi % i) == 0:
                break
        else:
            print(sayi)