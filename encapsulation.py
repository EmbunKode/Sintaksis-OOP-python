# MENGGUNAKAN OBJECT ORIENTED PROGRAMMING (OOP)
from geometri.bangun_ruang import BangunRuang
from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga

# p1 merupakan object
# PersegiPanjang merupakan class
# hitung luas
print('Menggunakan OOP Encapsulation')
p1 = PersegiPanjang(10, 69)
print(p1.info())
print(p1.hitung_luas())

s1 = Segitiga(4, 3)
print(s1.info())
print(s1.hitung_luas())

print('\nMenggunakan OOP Inheritance')
print('Mencoba membuat object dari kelas BangunRuang')
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())

# Polymorphism: kemampuan object untuk merespon berbeda, terhadap pemanggilan method yang sama
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

print('\n Polymorphism')
for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())
