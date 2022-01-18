



print("""
#####################################################################
###                    KULLANICI GİRİŞ EKRANI                     ###
###                                                               ###
###                         (1171604024)                          ###
###                                                               ###
###                   (İREM YALÇIN PROJE ÖDEVİ)                   ###
#####################################################################
""")

input("\nProgramımıza hoş geldiniz. Giriş İçin Lütfen ENTER'a Basınız...")

print("\nGiriş yapıldı! Teşekkürler")

while True:
#x değerini float olarak kullanıcıdan alırız

    x=float(input("#######################################\nKullanım Miktarınızı GB Olarak Giriniz: \n---\n"))

    i=int(input("---\nİşlemci hızlarımız; Lütfen CPU hızı tercihi yapınız...\n---\n1) 2 - 4 çekirdekler için	0.00416 €\n2) 5 - 8 çekirdekler için	0.00486 €\n3) 9 – 12 çekirdekler için	0.00555 €\n4) 13 – 16 çekirdekler için	0.00625 €\n*Kullanmak istediğiniz işlemci hızını seçiniz;\n---\n "))

#y değeri birim fiyat olarak hesaplanır ve sabit bir değerdir
    y=float(0.04)

#z değeri birim fiyat olarak alınır ve belli bir miktar üstündeyse indirimli fiyat uygulanır 
    z=float(0.05)

#a,b,c,d sabit CPU fiyat değerlerimiz

    a=float(0.0041)

    b=float(0.0048)

    c=float(0.0055)

    d=float(0.0062)

    if i==1:
        y=y+a

    if i==2:
        y=y+b

    if i==3:
        y=y+c

    if i==4:
        y=y+d

    if i==1:
        z=z+a

    if i==2:
        z=z+b

    if i==3:
        z=z+c

    if i==4:
        z=z+d    

#ilk 20 GB ücretsiz olduğu için girilen GB değerinden 20 GB çıkardık
    toplam = (x-20) * y
    toplam1 = (x-20) * z

#Maliyet olarak çıkan ondalıklı sayının virgülden sonra 2 basamaklı olmasını sağlamaktadır.
    toplam = round(toplam,2)
    toplam1 = round(toplam1,2)

#Hesaplamalar sonucunda şartlı olarak ödenmesi gereken meblağ kullanıcıya yansıtılır...
    if 0<=x<=20:
        print("---\n*Ödemeniz gereken herhangi bir ücret yok...")

    if 21<=x<=500:
        print("---\n*Ödemeniz gereken: ", toplam1 ,"€ Bizi tercih ettiğiniz için teşekkür eder yine bekleriz...")

    if x>501:
        print("---\n*Ödemeniz gereken: ", toplam ,"€ Bizi tercih ettiğiniz için teşekkür eder yine bekleriz...")

g=input("\n\n##Lütfen tekrar giriş için 1'ye çıkış için 2'ye basınız...##")

if g==1:
    pass

if g==2:
    print("Tekrar görüşmek üzere iyi günler dileriz...")
    exit()


