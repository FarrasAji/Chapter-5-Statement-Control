kodekaryawan = int(input("Masukkan kode karyawan : "))
namakaryawan = input("Masukkan Nama karyawan : ")
golongan     = input("Masukkan golongan : ")
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
else:
    print("Tidak termasuk golongan")
perhitunganpotong = gajipokok*potongan/100
hitunggaji= gajipokok - perhitunganpotong

print("===========================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("---------------------------")
print("Nama karyawan : ",namakaryawan)
print("Golongan      :",golongan)
print("---------------------------")
print("Gaji pokok    :",gajipokok)
print("Potongan",potongan,"% :",perhitunganpotong)
print("---------------------------")
print("Gaji bersih   : ",hitunggaji)
