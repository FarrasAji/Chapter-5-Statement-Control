bahasaindonesia = int(input("Masukan Nilai bahasa indonesia :"))
ipa = int(input("Masukkan Nilai Ipa :"))
matematika = int(input("Masukkan Nilai Matematika :"))

if (bahasaindonesia  >= 60) and (ipa >= 60) and (matematika > 70):
    print("Status Kelulusan : LULUS")
else:
    print("Status Kelulusan : TIDAK LULUS")
print("Sebab :")

if(bahasaindonesia < 60):
    print ("Nilai Bahasa indonesia kurang dari 60")
if (ipa < 60):
    print("Nilai ipamu kurang dari 60")
if(matematika < 70):
    print("Matematikamu kurang dari 70")
