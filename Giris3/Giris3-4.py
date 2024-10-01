def emeklilik():
    isim = input("İsminizi giriniz: ")
    dogum_yili = int(input("Doğum yılınızı giriniz: "))
    
    def yas_hesabi(dogum_yili):
        yas = 2024 - dogum_yili
        
        if yas >= 65:
            print("Emekli oldunuz!")
        else:
            kalan_yil = 65 - yas
            print("{} emekliliğine {} yıl var. ".format(isim, kalan_yil))
    
    yas_hesabi(dogum_yili)
    
emeklilik()
