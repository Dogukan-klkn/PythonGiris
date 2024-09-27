
#Ödev-2: Kullanıcıdan kullanıcı adı ve şifre oluşturmasını istenir. 
# Şifrenin uzunluğu altı haneye ulaşmışsa hesabınız oluşturuldu mesajı alınır, 
# altı haneden azsa altı haneli şifre oluşturması gerektiğinin mesajı alınır. 


kullanici_adi = input("Kullanıcı adınızı oluşturun: ")
sifre = input("Şifrenizi oluşturun: ")


if len(sifre) >= 6:
    print("Hesabınız oluşturuldu.")
else:
    print("Şifreniz en az 6 karakter uzunluğunda olmalıdır.")