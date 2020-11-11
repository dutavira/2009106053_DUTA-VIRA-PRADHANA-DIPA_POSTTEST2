# celcius ke fahrenheit
def fahrenheit(n):
    fahrenheit = (n*1.8)+32
    return fahrenheit

# celcius ke kelvin
def kelvin(n):
    kelvin = n+273
    return kelvin

# celcius ke reamur
def reamur(n):
    reamur = n*0.8
    return reamur

# menampilkan konversi
def konversi(n):
    print()
    print('=============================================')
    print('Hasil konversi Celcius ke Fahrenheit', fahrenheit(n), 'F')
    print('Hasil konversi Celcius ke Kelvin', kelvin(n), 'K')
    print('Hasil konversi Celcius ke Reamur', reamur(n), 'R')
    print('=============================================')
    print()

print('=============================================\n'
      '             SELAMAT DATANG DI               \n'
      '           KONVERSI SUHU CELCIUS             \n'
      '=============================================\n\n')

# memasukkan nilai celcius
print('=============================================')
n = int(input('Masukkan nilai suhu Celcius : '))
print('=============================================\n')

# menampilkan hasil
konversi(n)
print()
print('=============================================\n'
      '              PROGRAM SELESESAI              \n'
      '=============================================\n')
