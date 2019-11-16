import time
# Project by B&R
class otobus():
    def __init__(self,koltuk=48):
        self.koltuk=koltuk

    def bos_koltuk(self):
        print(self.koltuk)
    def yolcu_bindir(self,binenyolcu):
        if self.koltuk>=binenyolcu:
            self.koltuk-=binenyolcu
            print("Yolcu Biniyor...")
            time.sleep(1)
        else:
            print("Max bukadar yolcu alabilir:",self.koltuk)
    def yolcu_indir(self,inenyolcu):
        if binenyolcu>=inenyolcu:
            time.sleep(1)
            print("Yolcu İniyor...")
            self.koltuk+=inenyolcu
        else:
            print("Min Bukadar yolcu  inebilir",binenyolcu)

koltukgir=int(input("Koltuk Sayısı Gir:"))
otobus1=otobus(koltukgir)

print("""
Boş Koltuk Sayısını Görmek İçin '1'
Yolcu Bindirmek İçin '2'
Yolcu İndirmek İçin '3'
Çıkmak İçin 'q' 
""")
while True:
    tus=input("Seçim Yapınız:")
    if tus=="1":
        otobus1.bos_koltuk()
    elif tus=="2":
        binenyolcu = int(input("Binen Yolcu:"))
        otobus1.yolcu_bindir(binenyolcu)
    elif tus=="3":
        inenyolcu = int(input("İnen Yolcu:"))
        otobus1.yolcu_indir(inenyolcu)
