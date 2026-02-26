class Kapal:
  def __init__(self, kapal,berat , warna):
    self.kapal = kapal
    self.berat = berat
    self.warna = warna

  def kapal_baru(self):
        print("hai saya memiliki kapal" , self.kapal )
        
  def change_warna(self, news_warna):
        self.warna = news_warna
        print(f"warna kapal baru saya {news_warna}")

    
  def change_berat(self, news_berat):
        self.berat = news_berat
        print("berat kapal baru saya " + news_berat)
  
 
kapalSatu = Kapal("titanik","100","hijau")
kapalDua  =  Kapal("feri","500","merah")
kapalTiga  =  Kapal("nelayan","40","putih")

 #didalam kurung adalah properti

print(kapalSatu.kapal)
print(kapalSatu.berat)
print(kapalSatu.warna)
print(kapalDua.berat)

kapalSatu.change_warna("hitam")
kapalSatu.change_berat("1 ton")