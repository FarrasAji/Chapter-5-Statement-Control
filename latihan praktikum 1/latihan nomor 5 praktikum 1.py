kodekaryawan = int(input("Masukkan kode karyawan : "))
namakaryawan = input("Masukkan Nama karyawan : ")
golongan     = input("Masukkan golongan : ")
status       = input("Masukkan Status(1:Menikah,2: Belum : ")
jumlahanak   = int(input("Masukkan Jumlah Anak : "))    

if golongan=="A" or golongan=="a":
    gajipokok = 10000000
    if golongan =="A" or golongan=="a":
        potongan = 2.5
elif golongan=="B" or golongan=="b":
    gajipokok = 8500000
    if golongan=="B" or golongan=="b":
        potongan = 2.0
elif golongan=="C" or golongan=="c":
    gajipokok = 7000000
    if golongan=="C" or golongan=="c":
        potongan = 1.5
elif golongan=="D" or golongan=="d":
    gajipokok = 5500000
    if golongan=="D" or golongan=="d":
        potongan = 1.0

if(status == '1') :
    status = 'Sudah Menikah'
else:
    jumlahanak = 0
    tunjangansuamiistri = 0
    tunjangananak = 0
    status = 'Belum Menikah'
    
tunjangansuamiistri = gajipokok * 10 / 100
tunjangananak = gajipokok * 5/100
gajikotor = gajipokok + tunjangansuamiistri + tunjangananak
gajibersih = gajikotor - potongan
hitungpotongan = gajipokok * potongan/100

print("===========================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("---------------------------")
print("Nama karyawan : ",namakaryawan)
print("Golongan      :",golongan)
print("Status Menikah : ",status)
print("Jumlah Anak :",jumlahanak)
print("---------------------------")
print("Gaji pokok    :",gajipokok)
print("Tunjangan Istri/Suami :",tunjangansuamiistri)
print("Tunjangan Anak :",tunjangananak)
print("---------------------------")
print("Gaji Kotor : ",gajikotor)
print("Potongan",potongan,"% :",hitungpotongan)
print("---------------------------")
print("Gaji bersih   : ",gajibersih)
