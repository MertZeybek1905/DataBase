import sqlite3
con=sqlite3.connect("KütüphaneBilgi.db")
cursor=con.cursor()
def Tablo_Oluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Kitaplar (YazarAdı Text,KitapAd Text,Fiyat INT,KitapTür Text, Stok INT)")  
Tablo_Oluştur()
def Veri_Ekle(YazarAd,KitapAd,Fiyat,KitapTür,Stok):
    cursor.execute("Insert Into Kitaplar Values(?,?,?,?,?)",(YazarAd,KitapAd,Fiyat,KitapTür,Stok))
    con.commit()
def Veri_Sil(KitapAd):
    cursor.execute("Delete from kitaplar Where KitapAd = ?",(KitapAd,))
    con.commit()
def Veri_Güncelle(Eski_Stok,Yeni_Stok):
    cursor.execute("Update kitaplar set Stok=? where Stok=?",(Yeni_Stok,Eski_Stok))
    con.commit()
print("Kütüphane Projesi")
KullanıcıAdı="Mert.1905"
Şifre="270856"
KullanıcıAd=input("Lütfen Kullanıcı Adını Girin")
Parola=input("Lütfen Parola Girin")
if KullanıcıAdı==KullanıcıAd and Şifre==Parola:
    print("Kütüphaneye Hoşgeldiniz")
    print("Yapmak istediğiniz işlemi seçin(KitapEkleme(1),KitapSilme(2),KitapGüncelleme(3))")
    işlem=int(input("Lütfen İşlem Numarası Girin"))
    if işlem==1:
        YazarAd=input("Yazar Adı Girin:")
        KitapAd=input("Kitap Ad Girin")
        Fiyat=int(input("Kitap Fiyatı Girin"))
        KitapTür=input("Kitap Tür Girin")
        Stok=int(input("Stok Adedini Girin"))
        Veri_Ekle(YazarAd,KitapAd,Fiyat,KitapTür,Stok)
    elif işlem==2:
         Kitapİsim=input("Kitap ismini girin")
         Veri_Sil(Kitapİsim)
    elif işlem==3:
        Veri_Güncelle(250,100)
    else:
        print("Hatalı İşlem Seçtiniz")
con.close()