# Parent class
class Karyawan:
    def __init__(self, nama, id_karyawan, gaji_pokok):
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.gaji_pokok = gaji_pokok

    def hitung_gaji(self):
        return self.gaji_pokok

    def info(self):
        return f"{self.nama}, ID: {self.id_karyawan}, Gaji: {self.hitung_gaji()}"


# Subclass Manager
class Manager(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok, tunjangan):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.tunjangan = tunjangan

    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan

    def info(self):
        return f"Manager : {self.nama}, ID: {self.id_karyawan}, Gaji: {self.hitung_gaji()}"


# Subclass Programmer
class Programmer(Karyawan):
    def __init__(self, nama, id_karyawan, gaji_pokok, bonus):
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.bonus = bonus

    def hitung_gaji(self):
        return self.gaji_pokok + self.bonus

    def info(self):
        return f"Programmer : {self.nama}, ID: {self.id_karyawan}, Gaji: {self.hitung_gaji()}"


# === Contoh penggunaan ===
if __name__ == "__main__":
    manager1 = Manager("Galang", "202412043", 10000000.0, 5000000.0)
    programmer1 = Programmer("Surya", "202412044", 10000000.0, 2000000.0)

    print(manager1.info())
    print(programmer1.info())