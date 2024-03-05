class Mahasiswa:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

    def info_mahasiswa(self):
        print("Nama:", self.nama)
        print("Kelas:", self.kelas)
        print("Prodi:", self.prodi)
        print("Fakultas:", self.fakultas)
        print("Tempat Tinggal:", self.tempat_tinggal)
        print("Asal:", self.asal)

# Contoh penggunaan
mahasiswa1 = Mahasiswa("Erlangga", "A", "Pendidikan Komputer", "FKIP", "Samarinda", "Kota Bangun")
mahasiswa1.info_mahasiswa()


