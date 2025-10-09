# Template awal untuk Tugas 3

class Perusahaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_proyek = []   # menyimpan objek Proyek
        self.daftar_tim = []      # menyimpan objek Tim

    def buat_proyek(self, nama_proyek, deskripsi):
        proyek = Proyek(nama_proyek, deskripsi)
        self.daftar_proyek.append(proyek)
        return proyek

    def buat_tim(self, nama_tim):
        tim = Tim(nama_tim)
        self.daftar_tim.append(tim)
        return tim


class Proyek:
    def __init__(self, nama, deskripsi):
        self.nama = nama
        self.deskripsi = deskripsi
        self.tugas = []   # menyimpan daftar tugas

    def tambah_tugas(self, deskripsi_tugas):
        tugas_baru = Tugas(deskripsi_tugas)
        self.tugas.append(tugas_baru)
        return tugas_baru

    def __repr__(self):
        return f"Proyek(nama={self.nama!r}, tugas={len(self.tugas)})"


class Tim:
    def __init__(self, nama):
        self.nama = nama
        self.developers = []   # daftar developer

    def tambah_developer(self, developer):
        if not isinstance(developer, Developer):
            raise TypeError("Harus objek Developer")
        self.developers.append(developer)

    def __repr__(self):
        return f"Tim(nama={self.nama!r}, jumlah_dev={len(self.developers)})"


class Developer:
    def __init__(self, nama, keahlian):
        self.nama = nama
        self.keahlian = keahlian

    def __repr__(self):
        return f"Developer(nama={self.nama!r}, keahlian={self.keahlian!r})"


class Tugas:
    def __init__(self, deskripsi):
        self.deskripsi = deskripsi
        self.developer = None   # siapa developer yang ditugaskan

    def tugaskan_ke(self, developer):
        if not isinstance(developer, Developer):
            raise TypeError("Harus objek Developer")
        self.developer = developer

    def __repr__(self):
        return f"Tugas(deskripsi={self.deskripsi!r}, developer={self.developer.nama if self.developer else None})"


# =====================
# Contoh penggunaan
# =====================
if __name__ == "__main__":
    # Buat perusahaan
    perusahaan = Perusahaan("TechCorp")

    # Buat proyek
    proyek1 = perusahaan.buat_proyek("Website E-Commerce", "Membangun toko online")

    # Tambah tugas ke proyek
    tugas1 = proyek1.tambah_tugas("Buat halaman login")
    tugas2 = proyek1.tambah_tugas("Integrasi pembayaran")

    # Buat tim
    tim1 = perusahaan.buat_tim("Tim Backend")

    # Tambah developer ke tim
    dev1 = Developer("Galang", "Python")
    dev2 = Developer("Surya", "Database")
    tim1.tambah_developer(dev1)
    tim1.tambah_developer(dev2)

    # Tugaskan tugas ke developer
    tugas1.tugaskan_ke(dev1)
    tugas2.tugaskan_ke(dev2)

    # Cek hasil
    print(perusahaan.daftar_proyek)
    print(proyek1.tugas)
    print(tim1.developers)
