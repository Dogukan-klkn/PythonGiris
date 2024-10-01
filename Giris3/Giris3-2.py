numara = int(input("sayı giriniz: "))

def fak(numara):
    faktoryel = 1
    for i in range(1, numara + 1):
        faktoryel = faktoryel*numara
        numara -=1
        
    print("Girilen sayının faktoryeli:  {}".format(faktoryel) )    
    
    
fak(numara)    