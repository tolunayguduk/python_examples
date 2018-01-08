liste = [1,2,3,4,5,6,7,8,9,13,14,15,16,17,18,19]




def binarySearch(liste,aranan):
    altSinir = 0
    ustSinir = len(liste)
    while altSinir < ustSinir:
        x = altSinir + (ustSinir - altSinir) // 2
        val = liste[x]
        if aranan == val:
            return x
        elif aranan > val:
                altSinir = x
        elif aranan < val:
            ustSinir = x

while(1):
    aranan = int(input("ARANAN DEĞER : "))
    print("ARANAN DEĞERİN İNDİSİ : ")
    print(binarySearch(liste, aranan))




