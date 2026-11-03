#RAIHAN WIJAYAPUTRA
#2608576
#1A
#Sesi 3
a= int(0)
dataProduk = {
"P001": ["Keyboard", 85],
"P002": ["Mouse", 65],
"P003": ["Headset", 78],
"P004": ["Webcam", 90],
"P005": ["USB Hub", 60]
}
baik = []
kurang = []
dataNew = ["Keyborad", "Mouse", "Headset","Webcam", 'USB Hub']
rating = [85, 65, 78, 90, 60] 
data = int(len(dataProduk))

print('===== HASIL PENILAIAN PRODUK =====\n')
while a in range(data):
 
    print(f'Produk  : {dataNew[a]}\nRating  : {rating[a]}')
    if rating[a] >= 70:
        print('Status : Rating baik\n')
        baik.append(rating[a])
    else:
        print('Status   : Rating Kurang\n')
        kurang.append(rating[a])
    print('===== REKAPITULASI =====')
   
    a+=1

print(f'Jumlah Produk Rating baik   : {len(baik)}')
print(f'Jumlah Produk Rating Kurang : {len(kurang)}')
print(f'Persentase Rating Baik      : {(len(baik)/len(rating))*100}%')