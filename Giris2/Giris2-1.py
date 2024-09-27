#Ödev-1: Kullanıcıdan maaş bilgisini istenir ve 
# bu bilgiye göre maaşından ne kadar vergi kesileceğini hesaplanır.

maas = float(input("Maaşınızı girin: "))

if maas <= 10000:
    vergi_orani = 0.05
elif maas <= 25000:
    vergi_orani = 0.10
elif maas <= 45000:
    vergi_orani = 0.25
else:
    vergi_orani = 0.30


vergi_miktari = maas * vergi_orani
yeni_maas = maas - vergi_miktari

print(f"Vergi kesintisi: {vergi_miktari} TL")
print(f"Yeni maaşınız: {yeni_maas} TL")