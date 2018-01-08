class tasit:
    uzunluk = 0
    renk = ""
    agirlik = 0
    yakitTipi =""

class otomobil(tasit):
    kapiSayisi = 0
    airbagSayisi = 0
    vitesSayisi = 0
    farModeli = ""

    def __init__(self, kapiSayisi,airbagSayisi,vitesSayisi,farModeli):
        self.kapiSayisi = kapiSayisi
        self.airbagSayisi = airbagSayisi
        self.vitesSayisi = vitesSayisi
        self.farModeli = farModeli


otomobil = otomobil(4,5,6,"zenon")
print(otomobil.uzunluk)
print(otomobil.renk)
print(otomobil.agirlik)
print(otomobil.yakitTipi)
print(otomobil.kapiSayisi)
print(otomobil.airbagSayisi)
print(otomobil.farModeli)

