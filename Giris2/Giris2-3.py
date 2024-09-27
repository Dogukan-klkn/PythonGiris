
#Ödev-3: Bir önceki örnek geliştirilir.


kullanici_adi = input("Kullanıcı adınızı oluşturun: ")


while True:
    sifre = input("Şifrenizi oluşturun (5 ile 10 karakter arasında olmalı): ")
    

    if len(sifre) < 6:
        print("Şifreniz en az 6 karakter uzunluğunda olmalıdır.")
    elif 5 <= len(sifre) <= 10:
        print("Hesabınız oluşturuldu.")
        break
    else:
        print("Lütfen şifreniz 5 haneden az, 10 haneden fazla olmasın!")