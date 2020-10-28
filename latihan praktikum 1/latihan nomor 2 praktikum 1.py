bahasaindonesia = int(input("Masuukan Nilai bahasa indonesia :"))
ipa = int(input("Masukkan Nilai Ipa :"))
matematika = int(input("Masukkan Nilai Matematika :"))

if (bahasaindonesia  < 0) or (ipa < 0) or (matematika < 0):
    print("Nilai tidak valid")
else:
    print("nilai valid")
