# Kullanıcıdan pi değeri ve yarıçap bilgisi alarak dairenin alanını hesaplayan bir fonksiyon oluşturulur.

pi = 3.14

yaricap = float(input("Dairenin yarıçapını giriniz: "))

def alanHesabi(pi, yaricap):
    
    alan = pi*(yaricap*yaricap)
    
    print(f"Girilen yaıçapa ait dairenin alanı: {alan} m^2dir")
    
    

alanHesabi(pi, yaricap)    