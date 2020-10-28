print('Hai...nama saya mr, lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!')
angka=int(input('Tebakan Anda : '))
while True:
    if(angka<10):
        print('Hehehe.....Bilangan tebakan anda terlalu kecil')
        angka=int(input('Tebakan Anda : '))
    elif(angka>10):
        print('Hehehe.....Bilangan tebakan anda terlalu besar')
        angka=int(input('Tebakan Anda : '))
    elif(angka==10):
        print('yeeee...Bilangan tebakan anda BENAR :)')
        break
