from geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):

    # fungsi __init__ merupakan fungsi yang dipanggil pertama kali saat object diciptakan
    def __init__(self, p, l):
        self.p = p
        self.l = l

    def info(self):
        return f'Modul menghitung rumus Persegi Panjang dengan panjang {self.p} dan lebar {self.l}'

    def hitung_luas(self):
        return self.p * self.l
