from random import randint
awal = 0
while True:
    bil = randint(0,10)
    print(bil)
    awal = awal + 1
    if bil == 5:
        print('jumlah perulangan : ' + str(awal))
        break
