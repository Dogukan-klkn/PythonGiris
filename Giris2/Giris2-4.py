
#Ödev-4: Kullanıcıdan isim ve şifre isteyeceğiz ve 
# şifre girişi için üç hak verilir.

dogru_sifre = "123456"


hak = 3

while hak > 0:
    girilen_sifre = input("Şifrenizi girin: ")

    
    if girilen_sifre == dogru_sifre:
        print("Giriş yapıldı.")
        break
    else:
        hak -= 1
        print(f"Yanlış şifre! Kalan hakkınız: {hak}")

    
    if hak == 0:
        print("Hakkınız doldu. Program sona erdi.")