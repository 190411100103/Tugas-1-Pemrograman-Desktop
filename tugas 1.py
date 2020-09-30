#rumus rumus
def persegi() :
    print (' ' )
    x = float(input ('panjang sisi : '))
    luasp= x*x
    keliling = 2*luasp
    print (' ')
    print ('luas perseginya adalah : ' , luasp , 'cm2')
    print ('keliling perseginya adalah: ', keliling, 'cm')

def persegi_panjang():
    print (' ' )
    x= float(input('masukkan panjangnya : '))
    print (' ' )
    y= float(input ('masukkan lebarnya : '))
    c = x*y
    d = 2*(x+y)
    print (' ' )
    print ('luas persegi panjangnya adalah : ' , c , 'cm2')
    print ('keliling persegi panjangnya adalah :', d, 'cm')

def segitiga():
    print (' ' )
    p= float(input('masukan sisi ke satu:'))
    q= float(input('masukan sisi ke dua:'))
    r= float(input('masukan sisi ke tiga:'))
    x= float(input('masukkan alas segitiga : '))
    y= float(input('masukkan tinggi segitiga :'))
    a=0.5*x*y
    keliling= p+q+r
    print (' ' )
    print ('luas segitiganya adalah : ' , a, 'cm2')
    print ('keliling segitiga adalah :',keliling, 'cm')

def lingkaran():
    print (' ' )
    x = float(input('masukkan jari-jari lingkaran : '))
    luas = 22/7*x*x
    keliling = 2*22/7*x
    print ('')
    print ('luas lingkarannya adalah : ' , luas , 'cm2')
    print ('keliling lingkarannya adalah :', keliling, 'cm')

def jajar():
    print (' ' )
    x= float(input('masukkan tinggi jajaran genjang : '))
    y= float (input('masukkan alas jajaran genjang :' ))
    z= float (input('masukan panjang sisi miring jajaran genjang :'))
    luas = x*y
    keliling = 2*(y+z)
    print ('')
    print ('luas jajaran genjang adalah : ' , luas , 'cm2')
    print ('keliling jajaran genjang adalah :', keliling, 'cm')

def trapesium():
    print (' ')
    w= float (input('masukkan sisi atas trapesium : '))
    x= float(input('masukkan sisi bawah trapesium : '))
    y= float (input('masukkan tinggi trapesium : '))
    z= float (input('masukan sisi miring trapesium :'))
    luas = (w+x)*y/2
    keliling = w+x+z+z
    print ('')
    print ('luas trapesiumnya adalah : ' , luas, 'cm2')
    print ('keliling trapesium adalah :', keliling, 'cm')
    
def belah_ketupat():
    print (' ' )
    x= float(input('masukkan diagonal 1 : '))
    y= float(input('masukkan diagonal 2 : ' ))
    z= float(input('masukan sisi belah ketupat :'))
    luas = 0.5*x*y
    keliling= 4*z
    print ('')
    print ('luas belah ketupatnya adalah : ', luas, 'cm2')
    print ('keliling belah ketupat adalah :', keliling, 'cm')





print ("1) menghitung rata rata 5 variabel")
a=12
print ("a =",a)
b=10
print ("b =",b)
c=20
print ("c =",c)
d=90
print ("d =",d)
e=210
print ("e =",e)
mean= (a+b+c+d+e)/5
print ("rata-rata 5 variabel di atas adalah =",mean)

print('')
print ("2) Menghitung luas dan keliling bangun datar")
print ("1. Persegi")
print ("2. Persegi Panjang")
print ("3. Segitiga")
print ("4. Lingkaran")
print ("5. Jajar Genjang")
print ("6. Trapesium")
print ("7. Belah Ketupat")
tanya = int(input("Ingin menghitung bangun datar yang mana :"))
if tanya == 1:
    persegi()
elif tanya == 2:
    persegi_panjang()
elif tanya == 3:
    segitiga()
elif tanya == 4:
    lingkaran()
elif tanya == 5:
    jajar()
elif tanya == 6:
    trapesium()
elif tanya == 7:
    belah_ketupat()

print ('')
print ("3) Menghitung BMI")
f = float(input("Masukan Tinggi Anda (cm):"))
print (f,"cm")
g = float(input("Masukan Berat Badan Anda (kg):"))
print (g,"cm")
h = f/100.00
i = g/(h*h)
print ("Hasilnya :", i)
if i < 18.5:
    print ("Berat Badan Anda Kurang Nih Kak")
elif i <= 22.9:
    print ("Selamat Berat Badan Anda Normal")
elif i <= 29.9:
    print ("Waduh Sepertinya Berat Badan Kakak Berlebihan nih")
elif i >= 30:
    print ("Aduh Berat Badan Kakak Obesitas nih Harus Mulai Diet ya Kak")

print ('')
print ("4) Mencari Nilai Minimum dan Maksimum")
n = int(input("Mau Memasukan Berapa Nilai/Angka ?:"))
nilai=[]
for i in range (n):
    nip= int(input("masukan nilainya :"))
    nilai.append(nip)

kecil = nilai[0]
besar = nilai[len(nilai)-1]
for j in nilai:
    if kecil > j:
        kecil=j
    if besar < j:
        besar=j
nilai.sort()
print (nilai)
print ("nilai terbesar adalah :", besar)
print ("nilai terkecil adalah :", kecil)

username = "190411100103"
password = "arjuna"
print ('')
l = 0
z=True
loop=[]
while l <3:
    cekuser = input("Masukan Username :")
    cekpas = input ("Masukan Password :")
    if cekuser == username and cekpas == password:
        z=True
    else:
        loop.append(l+1)
        z=False
    l += 1
    print ('')

if z==True:
    print ("Anda Berhasil Masuk")
else:
    print ("Maaf Username atau Password Anda Salah Saat Looping Ke-", loop)


