ePosta = "hakanakinci"
parola = "123abc"

girilenEposta = input("Lütfen E-postanızı giriniz: ")

if (girilenEposta == ePosta):
    girilenParola = input("Lütfen Parolanızı giriniz: ")
    if (parola == girilenParola):
        print("Giriş başarılı :)")
    else:
        print("Parola hatalı...")
else:
    print("E-posta hatalı")
