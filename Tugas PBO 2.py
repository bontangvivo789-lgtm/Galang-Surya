import datetime

class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul               # public
        self._penulis = penulis          # protected
        self.__tahun_terbit = tahun_terbit  # private

    # Method untuk menampilkan info buku
    def get_info(self):
        return f"Judul: {self.judul}, Penulis: {self._penulis}, Tahun Terbit: {self.__tahun_terbit}"

    # Getter untuk tahun terbit
    def get_tahun_terbit(self):
        return self.__tahun_terbit

    # Setter untuk tahun terbit
    def set_tahun_terbit(self, tahun):
        tahun_sekarang = datetime.datetime.now().year
        if tahun <= tahun_sekarang:
            self.__tahun_terbit = tahun
        else:
            print("Error: Tahun terbit tidak boleh lebih dari tahun sekarang!")

# --- Contoh penggunaan ---
buku1 = Buku("Python OOP", "Galang", 2006)
print(buku1.get_info())

print("Tahun terbit:", buku1.get_tahun_terbit())
buku1.set_tahun_terbit(2025)   # valid
print("Tahun terbit baru:", buku1.get_tahun_terbit())

buku1.set_tahun_terbit(2030)   # tidak valid
