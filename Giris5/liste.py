#Bir sözlük oluşturulur ve bu sözlükte öğrencilerin isimleri ve Matematik, Fizik, Kimya notları tutulur.
#Kullanıcıdan isim ve ders ismi(Matematik, Fizik, Kimya) istenir ve bu bilgilere göre çıktı verilir.

#Sözlük üzerinde değerleri değiştirme, yeni değer ekleme, kullanıcıya ulaşmak istediği bilgileri sorma gibi işlemler yapılır.


ogrenciler = {
    
    "Dogukan":{"Matematik": 84, "Fizik": 76, "Kimya": 90},
    "Ali": {"Matematik": 79, "Fizik": 45, "Kimya": 95},
    "Ayse": {"Matematik": 65, "Fizik": 72, "Kimya": 82}   
}

while True:
    
    print("1- Not sorgusu yap \n 2- Not değiştir \n 3- Öğrenci ekle \n 4- öğrenci sil \n 5- Öğrenci Listesi ve  Notları \n 0- Sistemden Çık \n İşlem yapmak için birini seçin: ")
    secim = input()

    #1'e basıldığında not sorgusu yapılır.
    if(secim == "1"):
        ogrenci_adi = input("Öğrencinin ismini giriniz: ")
        ders_adi = input("Öğrenmek istediğiniz dersin adını giriniz(Matematik,Fizik,Kimya): ")

        if(ogrenci_adi in ogrenciler and ders_adi in ogrenciler[ogrenci_adi]):
            print("{} adlı öğrencinin {} dersinden aldığı not: {}" .format(ogrenci_adi, ders_adi, ogrenciler[ogrenci_adi][ders_adi]))
    
        else:
            print("Listede olmayan öğrenci veya ders. Lütfen tekrar deneyin")
        
    #2'ye bassıldığında not değiştire işlemi yapılır.      
    elif(secim == "2"): 
        ogrenci_adi = input("Öğrencinin ismini giriniz: ")
        ders_adi = input("Notunu değiştirmek istediğiniz dersin adını giriniz(Matematik,Fizik,Kimya): ")
    
        if(ogrenci_adi in ogrenciler and ders_adi in ogrenciler[ogrenci_adi]):
            yeni_not= int(input("{} adlı öğrencinin {} dersine yeni not girin: ".format(ogrenci_adi, ders_adi)))
            ogrenciler[ogrenci_adi][ders_adi] = yeni_not
            print(f"{ogrenci_adi} adlı öğrencinin {ders_adi} dersi notu güncellendi. Yeni not: {yeni_not}")
        else:
            print("Listede olmayan öğrenci veya ders. Lütfen tekrar deneyin")
            
    # 3'e basıldığında öğrenci ekleme işlemi yapılır.            
    elif(secim == "3"): 
        yeni_ogerenci = input("Listeye öğrenci eklemek için isim girin: ")
    
        if (yeni_ogerenci not in ogrenciler):
            ogrenciler[yeni_ogerenci] = {"Matematik": 0, "Fizik": 0, "Kimya": 0}
            print("{} adlı öğrenci listeye eklendi.Zorunlu dersler eklendi.".format(yeni_ogerenci))
        
        else:
            print("{} zaten listede mevcut.".format(yeni_ogerenci))    
    
    
    # 4'e basıldığında öğrenci silme işlemi yapılır 
    elif(secim == "4"):               
        silinen_ogrenci = input("Silmek istediğiniz öğrencinin adını giriniz: ")
    
        if(silinen_ogrenci in ogrenciler):
            del ogrenciler[silinen_ogrenci]
        else:
            print("Bu öğrenci zaten listede yok.")
    
    #5'e basıldığında öğrenci listesi ve notlarını yazdırır.
    elif(secim == "5"):
        for isim, dersler in ogrenciler.items():
            print(f"{isim}:")
            for ders, notu in dersler.items():
                print(f"  {ders}: {notu}")
            print()  # Her öğrenciden sonra boş bir satır ekler  
        
        
    # Sistemden çıkılır  
    elif(secim == "0"):
        print("Sistemden çıkılıyor...")
        break
        
    else:
        print("Yanlış bir sayı girdiniz. Tekrar deneyin")    
    
    





    
    