# Implementasi Tugas 2

class Pelanggan:
    def __init__(self, nama, email):
        self.nama = nama
        self.email = email
        self.keranjang = Keranjang()        # setiap pelanggan punya keranjang
        self.riwayat_pesanan = []           # menyimpan daftar pesanan yang pernah dibuat

    def buat_pesanan(self):
        # Buat pesanan dari keranjang
        if not self.keranjang.items:
            print("Keranjang kosong, tidak bisa buat pesanan.")
            return None
        pesanan = Pesanan(self)
        for item in self.keranjang.items:
            pesanan.tambah_item(item.produk, item.jumlah)
            item.produk.stok -= item.jumlah   # kurangi stok produk
        self.riwayat_pesanan.append(pesanan)  # simpan ke riwayat
        self.keranjang = Keranjang()          # reset keranjang baru
        return pesanan


class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok


class Keranjang:
    def __init__(self):
        self.items = []   # daftar ItemPesanan

    def tambah_produk(self, produk, jumlah):
        if produk.stok < jumlah:
            print(f"Stok {produk.nama} tidak mencukupi!")
            return
        # Cek apakah produk sudah ada di keranjang
        for item in self.items:
            if item.produk == produk:
                item.jumlah += jumlah
                return
        # Jika belum ada, tambahkan item baru
        self.items.append(ItemPesanan(produk, jumlah))


class Pesanan:
    def __init__(self, pelanggan):
        self.pelanggan = pelanggan
        self.items = []

    def tambah_item(self, produk, jumlah):
        self.items.append(ItemPesanan(produk, jumlah))

    def total_harga(self):
        return sum(item.produk.harga * item.jumlah for item in self.items)


class ItemPesanan:
    def __init__(self, produk, jumlah):
        self.produk = produk
        self.jumlah = jumlah


# -------------------- Contoh Penggunaan --------------------
if __name__ == "__main__":
    # Buat produk
    p1 = Produk("Laptop", 10000000, 5)
    p2 = Produk("Mouse", 150000, 10)
    p3 = Produk("Keyboard", 180000, 10)

    # Buat pelanggan
    pelanggan = Pelanggan("Galang", "galang@mail.com")

    # Tambah produk ke keranjang
    pelanggan.keranjang.tambah_produk(p1, 2)
    pelanggan.keranjang.tambah_produk(p2, 1)
    pelanggan.keranjang.tambah_produk(p3, 1)

    # Buat pesanan
    pesanan = pelanggan.buat_pesanan()
    if pesanan:
        print(f"Pesanan oleh {pelanggan.nama}:")
        for item in pesanan.items:
            print(f"- {item.produk.nama} x {item.jumlah}")
        print("Total Harga:", pesanan.total_harga())
