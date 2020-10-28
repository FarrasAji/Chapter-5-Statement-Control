print('Hai...nama saya mr, lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!')
angka=int(input('Tebakan Anda : '))
kurangpoin=0
while True:
    if(angka<10):
        print('Hehehe.....Bilangan tebakan anda terlalu kecil')
        ta=int(input('Tebakan Anda : '))
        kurangpoin+=2
    elif(angka>10):
        print('Hehehe.....Bilangan tebakan anda terlalu besar')
        ta=int(input('Tebakan Anda : '))
        kurangpoin+=2
    elif(angka==10):
        print('yeeee...Bilangan tebakan anda BENAR')
        score=100-kurangpoin
        print('Score Anda : ' + str(score))
        break
