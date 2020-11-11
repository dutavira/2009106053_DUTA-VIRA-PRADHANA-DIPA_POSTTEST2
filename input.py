print('============================================================\n'
      '                       SELAMAT DATANG  DI                   \n'
      '                        PENDATAAN SEPATU                    \n'
      '============================================================\n\n')
print('===================================\n'
      '  SILAHKAN LENGKAPI DATA BERIKUT   \n'
      '===================================\n\n')
# membuat input
print('---------------------------------')
merek   = input('Masukkan merek sepatu  : ')
print('---------------------------------')
ukuran    = int(input('Masukkan ukuran sepatu : '))
print('---------------------------------')
warna   = input('Masukkan warna sepatu  : ')
print('---------------------------------')
harga   = float(input('Masukkan harga sepatu  : '))
print('---------------------------------')
pasang  = int(input('Berapa pasang sepatu   : '))
print('---------------------------------\n\n')
# penggolongan tipe data
print('============================================================\n'
      '                    PENGGOLONGAN TIPE DATA                  \n'
      '============================================================\n')
print('Variabel merek  :', merek, 'bertipe data  :', type(merek), end='\n')
print('Variabel ukuran :', ukuran, 'bertipe data :', type(ukuran), end='\n')
print('Variabel warna  :', warna, 'bertipe data  :', type(warna), end='\n')
print('Variabel harga  :', harga, 'bertipe data  :', type(harga), end='\n')
print('Variabel pasang :', pasang, 'bertipe data :', type(pasang), end='\n')
print('============================================================\n\n')
# membuat list
print('=======================\n'
      ' LIST PADA DATA DI ATAS\n'
      '=======================\n')
list = []
list.append(merek)
list.append(ukuran)
list.append(warna)
list.append(harga)
list.append(pasang)
print('Merek    : ', list[0],'\n'
      'Ukuran   : ', list[1],'\n'
      'Warna    : ', list[2],'\n'
      'Harga    : ', list[3],'\n'
      'Pasang   : ', list[4],'\n'
      '======================\n\n\n')
print('============================================================\n'
      '                      PROGRAM SELESAI                       \n'
      '============================================================')