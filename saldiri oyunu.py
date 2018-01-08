class dusman:
    can = 100;
    ad = '';
    soyad ='';
    def kimlik(self,ad,soyad):
        self.ad =ad
        self.soyad=soyad
    def saldiri(self,dusman):
        dusman.can = dusman.can-10


dusman1 = dusman()
dusman2 = dusman()

dusman1.kimlik('tolunay','guduk')
dusman2.kimlik('evren','ay')



print(dusman2.can)
dusman1.saldiri(dusman2)
print(dusman2.can)

