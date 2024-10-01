dogum_yılı = int(input("Doğum yılınızı giriniz: "))

def yas_hesabi(dogum_yılı):
    yas = 2024- dogum_yılı
    return yas


print("Yaşınız: {} ".format(yas_hesabi(dogum_yılı)) )