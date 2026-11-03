#RAIHAN WIJAYAPUTRA
#2608576
#1A
#Sesi 3

percobaan = 0
a = 0
user = "loginAppGB"
pw = "GlowBeauty<3"
dataPengunjung = []
dataObatMurah = []
dataObatMahal = []
while percobaan < 3:
    print('Silahkan Login\n\n')
    username = input('Username: ')
    password = input('Password: ')
    if username == user and password == pw:
        print('Selamat Datang di aplikasi Glow Beauty.\n Pilih menu')
        menu = int(input('1. Kunjungan pasien\n2. Data Obat\n\nSilahkan pilih menu 1 atau 2: '))
        
        if menu == 1:
            print('\n=== Kunjungan Pasien ===')
            while a < 9:
                jumlahPengunjung = int(input('Input Jumlah pengunjung: '))
                dataPengunjung.append(jumlahPengunjung)
                a+=1

            print(f'Total penunjung yang meningkat: {sum(dataPengunjung)}')
            if sum(dataPengunjung)<50:
                print('Keputusan: Tidak membuka Cabang baru')
                break
            elif sum(dataPengunjung) >= 50 and sum(dataPengunjung)<=100:
                print('Keputusan: Menambah 1 cabang baru')
                break
            else:
                print('Keputusan: Menambah 2 Cabang abru')
                break
        elif menu == 2:
            print('===== Data Obat =====')
            while a < 6:
                biayaObat = int(input('Input Biaya Obat: '))
                a+=1
                if biayaObat < 30000:
                    break
                elif biayaObat < 150000:
                    dataObatMurah.append(biayaObat)
                else:
                    dataObatMahal.append(biayaObat)      
            print(f'Total Biaya Obat Mahal adalah Rp.{sum(dataObatMahal)}')
            print(f'Total Biaya Obat Murah adlah Rp.{sum(dataObatMurah)}')   
            break      
    else:
        print(f'Login Salah! Kesempatan anda {2-percobaan}x kali lagi.')

    percobaan+=1
    

