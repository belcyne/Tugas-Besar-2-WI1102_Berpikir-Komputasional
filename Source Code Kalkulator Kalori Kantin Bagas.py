#Program Kalkulator Kalori Kantin Bagas
#Deskripsi: Program memiliki 3 fungsi utama, yaitu:
#           1. Menerima input terkait data diri pengguna untuk menghitung BMI (Kondisi Tubuh) dan TDEE (Jumlah intake kalori per hari) dari pengguna
#           2. Memberi rekomendasi makanan secara random sesuai dengan kondisi jumlah kalori dan keinginan perubahan kondisi intake kalorinya
#           3. Menghitung total kalori yang dikonsumsi berdasarkan makanan - makanan yang dikonsumsi pengguna secara manual

#======================KAMUS======================
#nama, jk: string -> sebagai variabel untuk menyimpan nama dan jenis kelamin dari pengguna, data diri yang akan digunakan dalam perhitungan
#umur, tb, bb, aktivitas: int -> sebagai variabel untuk menyimpan umur, tinggi badan, dan berat badan dari pengguna, data diri yang akan dfigunakan dalam perhitungan
#bmi, bmr, tdee: int -> sebagai variabel untuk menyimpan hasil perhitungan bmi, bmr, dan tdee berdasarkan data diri pengguna
#maksi: int -> sebagai variabel untuk menyimpan total kalori yang dibutuhkan untuk makan siang pada umumnya sesuai dengan nilai TDEE
#opsi: int -> sebagai variabel untuk menentukan fungsi apa yang akan digunakan oleh pengguna


#import time digunakan dalam subprogram "loading", memanfaatkan fungsi flush dan time.sleep
#import random digunakan dalam subprogram "randomizerMakanan", memanfaatkan fungsi random.choice dan random.shuffle
import time
import random


#Database berupa makanan - makanan yang umumnya tersedia di Kantin Bagas, terbagi menjadi 4 array (nasi, karbo, serat, protein) serta 1 array utama yang berisi semua makanan
#Format dari setiap elemen array 2 dimensi ini adalah [Nama makanan, kalori minimum, kalori maksimum]
menu = [
    ["Nasi", 175, 225],
    ["Perkedel Jagung", 90, 140], 
    ["Perkedel Kentang", 120, 180], 
    ["Labu Tumis", 40, 90], 
    ["Buncis Tumis", 60, 120], 
    ["Terong Sambal", 180, 300], 
    ["Sosis Asam Manis", 70, 110], 
    ["Telur Dadar", 90, 120], 
    ["Kerang Tumis", 90, 150], 
    ["Kikil Tumis", 120, 200], 
    ["Telor Dadar Crispy", 125, 200], 
    ["Bakso Asam Manis", 180, 250], 
    ["Cumi Bumbu Hitam", 180, 260], 
    ["Ayam Bawang Putih", 200, 300], 
    ["Ayam Crispy", 250, 350], 
    ["Ayam Bumbu Rendang", 350, 450]
]

nasi = [175, 225]

karbo = [
    ["Perkedel Jagung", 90, 140], 
    ["Perkedel Kentang", 120, 180]
]
serat = [
    ["Labu Tumis", 40, 90], 
    ["Buncis Tumis", 60, 120], 
    ["Terong Sambal", 180, 300]
]
protein =  [
    ["Sosis Asam Manis", 70, 110], 
    ["Telur Dadar", 90, 120], 
    ["Kerang Tumis", 90, 150], 
    ["Kikil Tumis", 120, 200], 
    ["Telor Dadar Crispy", 125, 200], 
    ["Bakso Asam Manis", 180, 250], 
    ["Cumi Bumbu Hitam", 180, 260], 
    ["Ayam Bawang Putih", 200, 300], 
    ["Ayam Crispy", 250, 350], 
    ["Ayam Bumbu Rendang", 350, 450]
]


#Procedure Judul
def judul(title):
    #Membuat format header judul dengan teks sesuai variabel "title" dilengkapi dengan karakter '=' dan '-'

    print("=" * (30 + len(title)))
    print("-" * (15) + title + "-" * (15))
    print("=" * (30 + len(title)))
    return


#Procedure Skip
def skip():
    #Mengoutput enter sebanyak 3 kali, berfungsi memberikan jarak antara satu bagian dengan bagian lain agar tidak terlihat menumpuk

    print(); print(); print()
    return


#Function Hitung BMI
def hitungBMI(bb, tb):
    #Menghitung BMI pengguna, di mana rumus BMI dipengaruhi oleh berat badan dan tinggi badan

    #KAMUS LOKAL
    #tb_m: int -> sebagai variabel untuk menyimpan tinggi badan pengguna dalam meter (dari centimeter)
    #bmi: float -> sebagai variabel untuk menyimpan nilai dari perhitungan rumus BMI

    tb_m = tb / 100
    bmi = bb / (tb_m ** 2)
    return bmi


#Procedure Klasifikasi BMI
def klasifikasiBMI(bmi):
    #Mengoutput kondisi tubuh serta rekomendasi kepada pengguna berdasarkan nilai BMI yang didapat, mulai dari berat badan kurang hingga obesitas II

    print("Berdasarkan tinggi dan berat badan Anda, hasil BMI Anda: ", end="")
    if bmi < 18.5:
        print(f"Berat Badang Kurang [{bmi:.1f}]")
        print("Berat badan kurang bisa menjadi penanda bahwa Anda kekurangan asupan makanan.")
    elif bmi <= 22.9:
        print(f"Berat Badan Normal [{bmi:.1f}]")
        print("Berat badan Anda berada di rentang BMI normal.")
    elif bmi <= 24.9:
        print(f"Berat Badan Lebih [{bmi:.1f}]")
        print(f"Anda sebaiknya mencegah penambahan berat badan lebih lanjut.")
    elif bmi <= 29.9:
        print(f"Obesitas I [{bmi:.1f}]")
        print("Anda mengalami obesitas dan berisiko mengalami komplikasi terkait berat badan lainnya.")
    else:
        print(f"Obesitas II [{bmi:.1f}]")
        print("Anda mengalami obesitas dan berisiko mengalami komplikasi terkait berat badan lainnya yang lebih berbahaya.")
    return


#Function Hitung BMR
def hitungBMR(jk, bb, tb, umur):
    #Menghitung nilai BMR, di mana rumus BMR dipengaruhi oleh jenis kelamin, berat badan, tinggi badan, dan umur

    if jk.lower() == "pria": #Menggunakan rumus +5 di akhir jika Pria (Penggunaan .lower() untuk mencegah kesalahan karena huruf kapital dan nonkapital)
        bmr = (10 * bb) + (6.25 * tb) - (5 * umur) + 5
    elif jk.lower() == "wanita": #menggunakan rumus -161 di akhir jika Wanita (Penggunaan .lower() untuk mencegah kesalahan karena huruf kapital dan nonkapital)
        bmr = (10 * bb) + (6.25 * tb) - (5 * umur) - 161
    return bmr


#Function Hitung TDEE
def hitungTDEE(bmr, akt):
    #Menghitung nilai TDEE, di mana rumus TDEE dipengaruhi oleh hasil BMR dan tingkat aktivitas pengguna (1-5)

    if akt == 1:
        tdee = bmr * 1.2
    elif akt == 2:
        tdee = bmr * 1.375
    elif akt == 3:
        tdee = bmr * 1.55
    elif akt == 4:
        tdee = bmr * 1.725
    elif akt == 5:
        tdee = bmr * 1.9
    return tdee


#Procedure Loading
def loading(dots, delay):
    #Membuat semacam loading tepat sebelum output perhitungan TDEE, berfungsi memberikan efek perhitungan kompleks

    print(f"Kalkulasi TDEE", end="", flush=True) #flush=True berarti teks yang terdapat dalam fungsi print akan langsung dikeluarkan, tidak menunggu teks lain di baris yang sama
    for i in range(dots): #Perulangan sebanyak "dots" kali
        time.sleep(delay) #time.sleep berfungsi untuk memberi suatu delay sebelum dilakukannya perintah - perintah berikutnya, di mana dalam program ini nilai delay adalah 1
        print(".", end="", flush=True) #flush=True akan langsung mengoutput karakter "." secara langsung, tidak menunggu hingga perulangan selesai
    print()
    return


#Procedure Maintain
def maintain(maksi):
    #Memberikan rekomendasi kepada pengguna berupa jumlah kalori yang serupa (maintain) dengan opsi untuk mengganti rekomendasi apabila kurang sesuai dengan pilihan

    #KAMUS LOKAL
    #batasBawah, batasAkhir: int -> sebagai variabel penentu batasan agar kombinasi makanan yang diberikan berada di range yang sesuai 
    #minNasi, maxNasi: int -> sebagai variabel yang berisi kalori minimum dan maksimum nasi
    #porsi: 2D array of int -> sebagai array yang berfungsi untuk menyimpan semua kombinasi makanan dengan porsi antara 1 - 2
    #validRekomen: 2D array of string & int -> sebagai array yang berfungsi untuk menyimpan semua kombinasi makanan yang mungkin untuk range yang telah ditentukan,
    #                                          menyimpan data terkait nama setiap jenis makanan, minimum dan maksimum kalori, total minum dan maksimum kalori, serta
    #                                          jumlah porsi setiap makanan
    #k, s, p: int -> sebagai counter sekaligus array penampung untuk perulangan yang dilakukan
    #namaKarbo, namaSerat, namaProtein: string -> sebagai variabel untuk menyimpan nama dari setiap jenis makanan yang akan digunakan dalam pengoutputan kombinasi
    #minKarbo, minSerat, minProtein: int -> sebagai variabel untuk menyimpan kalori minimum dari setiap jenis makanan yang akan digunakan dalam pengoutputan kombinasi
    #maxKarbo, maxSerat, maxProtein: int -> sebagai variabel untuk menyimpan kalori maksimum dari setiap jenis makanan yang akan digunakan dalam pengoutputan kombinasi
    #totalMin, totalMax: int -> sebagai variabel untuk menyimpan total kalroi minimum dan maksimum dari semua jenis makanan yang akan digunakan dalam pengoutputan kombinasi
    #porsiK, porsiS, porsiP: int -> sebagai variabel untuk menyimpan jumlah porsi dari setiap jenis makanan yang akan digunakan dalam pengoutputan kombinasi

    batasBawah = maksi - 200
    batasAtas = maksi + 200
    minNasi = nasi[0]
    maxNasi = nasi[1]

    porsi = [
        [1, 1, 1],
        [2, 1, 1],
        [1, 2, 1],
        [1, 1, 2],
        [2, 2, 1],
        [2, 1, 2],
        [1, 2, 2],
        [2, 2, 2]
    ]
    validRekomen = []

    for k in karbo:
        for s in serat:
            for p in protein:
                    for porsiK, porsiS, porsiP in porsi:
                        totalMin = (k[1] * porsiK) + (s[1] * porsiS) + (p[1] * porsiP) + minNasi
                        totalMax = (k[2] * porsiK) + (s[2] * porsiS) + (p[2] * porsiP) + maxNasi

                        if batasBawah <= totalMin and batasAtas >= totalMax:
                            validRekomen.append([k, s, p, totalMin, totalMax, porsiK, porsiS, porsiP])

    if not validRekomen:
        print("Maaf, tidak ada rekomendasi yang cocok untuk kombinasi makanan dengan target kalori ini.")
        return

    random.shuffle(validRekomen)
    for rekomen in validRekomen:
        namaKarbo = rekomen[0][0]; minKarbo = rekomen[0][1]; maxKarbo = rekomen[0][2]
        namaSerat = rekomen[1][0]; minSerat = rekomen[1][1]; maxSerat = rekomen[1][2]
        namaProtein = rekomen[2][0]; minProtein = rekomen[2][1]; maxProtein = rekomen[2][2]
        totalMin = rekomen[3]; totalMax = rekomen[4]
        porsiK = rekomen[5]; porsiS = rekomen[6]; porsiP = rekomen[7]
        print("-" * 50)
        print(f"REKOMENDASI DITEMUKAN! Total Kalori: {totalMin} - {totalMax} kalori")
        print(f"1. nasi ({minNasi} - {maxNasi} kalori)")    
        print(f"2. {namaKarbo} {porsiK} Porsi ({minKarbo * porsiK} - {maxKarbo * porsiK} kalori)")
        print(f"3. {namaSerat} {porsiS} Porsi ({minSerat * porsiS} - {maxSerat * porsiS} kalori)")
        print(f"4. {namaProtein} {porsiP} Porsi ({minProtein * porsiP} - {maxProtein * porsiP} kalori)")
        print("-" * 50)

        ulang = input("Apakah ingin rekomendasi lain? (y/n): ").lower()
                         #Jika pengguna memilih y (yes), maka kondisi if tidak memenuhi, yang berarti perulangan akan terus berlanjut
        if ulang == "n": #Jika pengguna memilih n (no), maka kondisi if memenuhi, yang berarti subprogram akan mengoutput print terakhir dan kemudian return ke program awal
            return
    
    print("Tidak ada kombinasi makanan lain yang dapat direkomendasikan untuk target kalori ini.")
    return

def surplus(maksi):
    #Memberikan rekomendasi kepada pengguna berupa jumlah kalori yang serupa (maintain) dengan opsi untuk mengganti rekomendasi apabila kurang sesuai dengan pilihan

    #KAMUS LOKAL
    #batasBawah, batasAkhir: int -> sebagai variabel penentu batasan agar kombinasi makanan yang diberikan berada di range yang sesuai 
    #minNasi, maxNasi: int -> sebagai variabel yang berisi kalori minimum dan maksimum nasi
    #porsi: 2D array of int -> sebagai array yang berfungsi untuk menyimpan semua kombinasi makanan dengan porsi antara 1 - 2
    #validRekomen: 2D array of string & int -> sebagai array yang berfungsi untuk menyimpan semua kombinasi makanan yang mungkin untuk range yang telah ditentukan,
    #                                          menyimpan data terkait nama setiap jenis makanan, minimum dan maksimum kalori, total minum dan maksimum kalori, serta
    #                                          jumlah porsi setiap makanan
    #k, s, p: int -> sebagai counter sekaligus array penampung untuk perulangan yang dilakukan
    #namaKarbo, namaSerat, namaProtein: string -> sebagai variabel untuk menyimpan nama dari setiap jenis makanan yang akan digunakan dalam pengoutputan kombinasi
    #minKarbo, minSerat, minProtein: int -> sebagai variabel untuk menyimpan kalori minimum dari setiap jenis makanan yang akan digunakan dalam pengoutputan kombinasi
    #maxKarbo, maxSerat, maxProtein: int -> sebagai variabel untuk menyimpan kalori maksimum dari setiap jenis makanan yang akan digunakan dalam pengoutputan kombinasi
    #totalMin, totalMax: int -> sebagai variabel untuk menyimpan total kalroi minimum dan maksimum dari semua jenis makanan yang akan digunakan dalam pengoutputan kombinasi
    #porsiK, porsiS, porsiP: int -> sebagai variabel untuk menyimpan jumlah porsi dari setiap jenis makanan yang akan digunakan dalam pengoutputan kombinasi

    batasBawah = maksi + 200
    batasAtas = maksi + 400
    minNasi = nasi[0] + 50
    maxNasi = nasi[1] + 50

    porsi = [
        [1, 1, 1],
        [2, 1, 1],
        [1, 2, 1],
        [1, 1, 2],
        [2, 2, 1],
        [2, 1, 2],
        [1, 2, 2],
        [2, 2, 2]
    ]
    validRekomen = []

    for k in karbo:
        for s in serat:
            for p in protein:
                    for porsiK, porsiS, porsiP in porsi:
                        totalMin = (k[1] * porsiK) + (s[1] * porsiS) + (p[1] * porsiP) + minNasi
                        totalMax = (k[2] * porsiK) + (s[2] * porsiS) + (p[2] * porsiP) + maxNasi

                        if batasBawah <= totalMin and batasAtas >= totalMin:
                            validRekomen.append([k, s, p, totalMin, totalMax, porsiK, porsiS, porsiP])

    if not validRekomen:
        print("Maaf, tidak ada rekomendasi yang cocok untuk kombinasi makanan dengan target kalori ini.")
        return

    random.shuffle(validRekomen)
    for rekomen in validRekomen:
        namaKarbo = rekomen[0][0]; minKarbo = rekomen[0][1]; maxKarbo = rekomen[0][2]
        namaSerat = rekomen[1][0]; minSerat = rekomen[1][1]; maxSerat = rekomen[1][2]
        namaProtein = rekomen[2][0]; minProtein = rekomen[2][1]; maxProtein = rekomen[2][2]
        totalMin = rekomen[3]; totalMax = rekomen[4]
        porsiK = rekomen[5]; porsiS = rekomen[6]; porsiP = rekomen[7]
        print("-" * 50)
        print(f"REKOMENDASI DITEMUKAN! Total Kalori: {totalMin} - {totalMax} kalori")
        print(f"1. nasi ({minNasi} - {maxNasi} kalori)")    
        print(f"2. {namaKarbo} {porsiK} Porsi ({minKarbo * porsiK} - {maxKarbo * porsiK} kalori)")
        print(f"3. {namaSerat} {porsiS} Porsi ({minSerat * porsiS} - {maxSerat * porsiS} kalori)")
        print(f"4. {namaProtein} {porsiP} Porsi ({minProtein * porsiP} - {maxProtein * porsiP} kalori)")
        print("-" * 50)

        ulang = input("Apakah ingin rekomendasi lain? (y/n): ").lower()
                         #Jika pengguna memilih y (yes), maka kondisi if tidak memenuhi, yang berarti perulangan akan terus berlanjut
        if ulang == "n": #Jika pengguna memilih n (no), maka kondisi if memenuhi, yang berarti subprogram akan mengoutput print terakhir dan kemudian return ke program awal
            return
    
    print("Tidak ada kombinasi makanan lain yang dapat direkomendasikan untuk target kalori ini.")
    return

def defisit(maksi):
    #Memberikan rekomendasi kepada pengguna berupa jumlah kalori yang serupa (maintain) dengan opsi untuk mengganti rekomendasi apabila kurang sesuai dengan pilihan

    #KAMUS LOKAL
    #batasBawah, batasAkhir: int -> sebagai variabel penentu batasan agar kombinasi makanan yang diberikan berada di range yang sesuai 
    #minNasi, maxNasi: int -> sebagai variabel yang berisi kalori minimum dan maksimum nasi
    #porsi: 2D array of int -> sebagai array yang berfungsi untuk menyimpan semua kombinasi makanan dengan porsi antara 1 - 2
    #validRekomen: 2D array of string & int -> sebagai array yang berfungsi untuk menyimpan semua kombinasi makanan yang mungkin untuk range yang telah ditentukan,
    #                                          menyimpan data terkait nama setiap jenis makanan, minimum dan maksimum kalori, total minum dan maksimum kalori, serta
    #                                          jumlah porsi setiap makanan
    #k, s, p: int -> sebagai counter sekaligus array penampung untuk perulangan yang dilakukan
    #namaKarbo, namaSerat, namaProtein: string -> sebagai variabel untuk menyimpan nama dari setiap jenis makanan yang akan digunakan dalam pengoutputan kombinasi
    #minKarbo, minSerat, minProtein: int -> sebagai variabel untuk menyimpan kalori minimum dari setiap jenis makanan yang akan digunakan dalam pengoutputan kombinasi
    #maxKarbo, maxSerat, maxProtein: int -> sebagai variabel untuk menyimpan kalori maksimum dari setiap jenis makanan yang akan digunakan dalam pengoutputan kombinasi
    #totalMin, totalMax: int -> sebagai variabel untuk menyimpan total kalroi minimum dan maksimum dari semua jenis makanan yang akan digunakan dalam pengoutputan kombinasi
    #porsiK, porsiS, porsiP: int -> sebagai variabel untuk menyimpan jumlah porsi dari setiap jenis makanan yang akan digunakan dalam pengoutputan kombinasi

    batasBawah = maksi - 400
    batasAtas = maksi - 200
    minNasi = nasi[0] - 50
    maxNasi = nasi[1] - 50

    porsi = [
        [1, 1, 1],
        [2, 1, 1],
        [1, 2, 1],
        [1, 1, 2],
        [2, 2, 1],
        [2, 1, 2],
        [1, 2, 2],
        [2, 2, 2]
    ]
    validRekomen = []

    for k in karbo:
        for s in serat:
            for p in protein:
                    for porsiK, porsiS, porsiP in porsi:
                        totalMin = (k[1] * porsiK) + (s[1] * porsiS) + (p[1] * porsiP) + minNasi
                        totalMax = (k[2] * porsiK) + (s[2] * porsiS) + (p[2] * porsiP) + maxNasi

                        if batasAtas >= totalMax and batasBawah <= totalMax:
                            validRekomen.append([k, s, p, totalMin, totalMax, porsiK, porsiS, porsiP])

    if not validRekomen:
        print("Maaf, tidak ada rekomendasi yang cocok untuk kombinasi makanan dengan target kalori ini.")
        return

    random.shuffle(validRekomen)
    for rekomen in validRekomen:
        namaKarbo = rekomen[0][0]; minKarbo = rekomen[0][1]; maxKarbo = rekomen[0][2]
        namaSerat = rekomen[1][0]; minSerat = rekomen[1][1]; maxSerat = rekomen[1][2]
        namaProtein = rekomen[2][0]; minProtein = rekomen[2][1]; maxProtein = rekomen[2][2]
        totalMin = rekomen[3]; totalMax = rekomen[4]
        porsiK = rekomen[5]; porsiS = rekomen[6]; porsiP = rekomen[7]
        print("-" * 50)
        print(f"REKOMENDASI DITEMUKAN! Total Kalori: {totalMin} - {totalMax} kalori")
        print(f"1. nasi ({minNasi} - {maxNasi} kalori)")    
        print(f"2. {namaKarbo} {porsiK} Porsi ({minKarbo * porsiK} - {maxKarbo * porsiK} kalori)")
        print(f"3. {namaSerat} {porsiS} Porsi ({minSerat * porsiS} - {maxSerat * porsiS} kalori)")
        print(f"4. {namaProtein} {porsiP} Porsi ({minProtein * porsiP} - {maxProtein * porsiP} kalori)")
        print("-" * 50)

        ulang = input("Apakah ingin rekomendasi lain? (y/n): ").lower()
                         #Jika pengguna memilih y (yes), maka kondisi if tidak memenuhi, yang berarti perulangan akan terus berlanjut
        if ulang == "n": #Jika pengguna memilih n (no), maka kondisi if memenuhi, yang berarti subprogram akan mengoutput print terakhir dan kemudian return ke program awal
            return
    
    print("Tidak ada kombinasi makanan lain yang dapat direkomendasikan untuk target kalori ini.")
    return
    
#Procedure randomizerMakanan
def randomizerMakanan(maksi):
    #Memberikan rekomendasi makanan sesuai dengan pilihan yang diinginkan penggunanya, antara tetap, naik, atau turun

    #KAMUS LOKAL
    #kondisi: int -> sebagai variabel untuk menentukan kondisi perubahan kalori mana yang diinginkan pengguna

    judul("REKOMENDASI MAKANAN")
    print("Apa yang ingin Anda lakukan?")
    print("1. Maintain (Tetap)")
    print("2. Surplus (Naik)")
    print("3. Defisit (Turun)")
    kondisi = int(input("⇒ "))

    if kondisi == 1:
        maintain(maksi)
    elif kondisi == 2:
        surplus(maksi)
    elif kondisi == 3:
        defisit(maksi)

    input("Tekan ENTER untuk lanjut...")
    return


#Procedure listMakanan
def listMakanan():
    #Mengoutput semua makanan yang terdapat dalam array menu sebagai list makanan dari Kantin Bagas
    for i in range (16):
        print(f"{i + 1}. {menu[i][0]} ({menu[i][1]} - {menu[i][2]} kalori)")
    print("================================================")
    return


#Function jumlahMakanan
def jumlahMakanan():
    #Menghitung jumlah total kalori yang dikonsumsi pengguna sesuai banyak dan jumlah porsi

    #KAMUS LOKAL
    #minKal: int -> sebagai variabel yang berisi total kalori minimum dari setiap jenis makanan yang dipilih pengguna
    #maxKal: int -> sebagai variabel yang berisi total kalori maksimum dari setiap jenis makanan yang dipilih pengguna
    #no: int -> sebagai variabel untuk menunjukkan berapa jenis makanan yang telah dihitung
    #makan: int -> sebagai variabel penunjuk jenis makanan yang dipilh berdasarkan indeksnya
    #porsi: int -> sebagai variabel penentu berapa jumlah porsi makanan yang dipilih
    #ulang: string -> sebagai variabel penentu apabila subprogram terus berjalan atau tidak

    minKal = 0
    maxKal = 0
    no = 1
    while True:
        makan = int(input(f"{no}. Masukkan nomor makanan: "))
        porsi = int(input(f"   Jumlah porsi {menu[makan - 1][0]}: "))
        minKal += (menu[makan - 1][1] * porsi) #Menambahkan total kalori ke variabel minKal sesuai kalori minimal makanan dan jumlah porsinya
        maxKal += (menu[makan - 1][2] * porsi) #Menambahkan total kalori ke variabel maxKal sesuai kalori maksimal makanan dan jumlah porsinya
        no += 1
        ulang = input("Apakah ada tambahan makanan lain? (y/n): ").lower()
                         #Jika pengguna memilih y (yes), maka kondisi if tidak memenuhi, yang berarti perulangan akan terus berlanjut
        if ulang == "n": #Jika pengguna memilih n (no), maka kondisi if memenuhi, yang berarti subprogram akan mengoutput print terakhir dan kemudian return ke subprogram kalkulatorMakanan
            return minKal, maxKal
    

#Procedure Kalkulator Makanan
def kalkulatorMakanan(maksi):
    #Menghitung jumlah kalori yang dikonsumsi pengguna berdasarkan banyaknya makanan dan jumlah porsi

    #KAMUS LOKAL
    #min: int -> sebagai variabel penerima total jumlah kalori mininum makanan yang dipilih pengguna
    #max: int -> sebagai variabel penerima total jumlah kalori maksimum makanan yang dipilih pengguna
    #totalMin: int -> sebagai variabel penerima total jumlah kalori mininum makanan yang dipilih pengguna ditambah kalori minimum nasi
    #totalMax: int -> sebagai variabel penerima total jumlah kalori maksimum makanan yang dipilih pengguna ditambah kalori maksimum nasi

    judul("KALKULATOR MAKANAN")
    print("Berikut list makanan Kantin Bagas: ")
    listMakanan() #Memanggil procedure listMakanan untuk mengoutput semua makanan yang tersedia
    min, max = jumlahMakanan() #Memanggil fungsi jumlahMakanan untuk menghitung jumlah kalori total yang dikonsumsi
    totalMin = min + nasi[0]
    totalMax = max + nasi[1]
    print(f"Jumlah konsumsi kalori Anda hari ini: {totalMin} - {totalMax} kalori")
    #Mengoutput total kalori yang dikonsumsi serta kelebihan atau kekurangannya terhadap TDEE porsi makan siang
    if maksi > totalMax:
        print(f"Berdasarkan jumlah kalori tersebut, Anda mengonsumsi {maksi - totalMax:.2f} kalori lebih sedikit dari jumlah TDEE untuk porsi makan siang.")
    elif maksi < totalMin:
        print(f"Berdasarkan jumlah kalori tersebut, Anda mengonsumsi {totalMin - maksi:.2f} kalori lebih banyak dari jumlah TDEE untuk porsi makan siang.")
    else:
        print(f"Berdasarkan jumlah kalori tersebut, Anda mengonsumsi kalori di rentang yang serupa dengan TDEE.")

    input("Tekan ENTER untuk lanjut...")
    return




#======================ALGORITMA PROGRAM UTAMA======================
#Input data diri pengguna
judul("INPUT DATA DIRI") #Memanggil procedure judul untuk mengeprint format judul dengan teks "INPUT DATA DIRI"
nama = (input("Nama: "))
umur = int(input("Umur: "))
jk = (input("Gender (Pria/Wanita): "))
tb = int(input("Tinggi Badan (cm): "))
bb = int(input("Berat Badan (kg): "))
print("Tingkat Aktivitas:")
print("1. Sedenter: Minim aktivitas fisik, pekerjaan kantoran")
print("2. Ringan: Olahraga ringan 1-3 kali/minggu")
print("3. Sedang: Olahraga sedang 3-5 kali/minggu")
print("4. Berat: Olahraga berat 6-7 kali/minggu")
print("5. Ekstra: Olahraga sangat intens 2 kali sehari")
aktivitas = int(input("Input tingkat aktivitas (1-5): "))
skip() #Memanggil procedure skip untuk mengeprint 3 baris kosong


#Perhitungan nilai BMI, BMR, dan TDEE, serta pengoutputan hasil BMI dan TDEE berdasarkan inputan data diri dari pengguna
judul("KALKULASI BMI & TDEE")
bmi = hitungBMI(bb, tb) #Memanggil function hitungBMI untuk menghitung nilai BMI
klasifikasiBMI(bmi) #Memanggil procedure untuk mengoutput kelas BMI berdasarkan nilai BMI
bmr = hitungBMR(jk, bb, tb, umur) #Memanggil function hitungBMR untuk menghitung nilai BMR
tdee = hitungTDEE(bmr, aktivitas) #Menanggil function hitungTDEE untuk menghitung nilai TDEE
loading(4, 1) #Memanggil procedure loading untuk membuat teks loading sementara
print(f"TDEE: {tdee:.2f} kalori/hari")

maksi = tdee * 2 / 5 #Pembagian total kalori per hari untuk makan siang, asumsi pengguna makan di siang hari (Kalo pagi atau malem mungkin agak terlalu jauh :D)
print(f"Porsi Makan Siang di Kantin Bagas: {maksi:.2f} kalori")
input("Tekan ENTER untuk lanjut...")
skip()


#Perulangan menu rekomendasi dan perhitungan kalori, opsi bernilai -1 sebagai awlan agar dapat masuk ke perulangan while dan berhenti ketika input dari opsi bernilai 0
opsi = -1
while opsi != 0:
    judul("REKOMENDASI & KALKULATOR KALORI KANTIN BAGAS")
    print(f"Halo {nama}! Apa yang ingin kamu lakukan?")
    print("1. Berikan saya rekomendasi makanan!")
    print("2. Saya ingin tahu konsumsi kalori saya hari ini!")
    print("0. Keluar")
    opsi = int(input("⇒ "))
    skip()

    if opsi == 1: #Opsi 1 berupa pemberian rekomendasi makanan
        randomizerMakanan(maksi)
    elif opsi == 2: #Opsi 2 berupa perhitungan kalori makanan manual
        kalkulatorMakanan(maksi)
    #Opsi 0 tidak masuk ke dalam kondisi mana pun, sebab akan langsung menghentikan perulangan

    skip()

#Perulangan selesai dan program dihentikan
print("Terimakasih sudah menggunakan layanan Kalkulator Kalori Kantin Bagas!")