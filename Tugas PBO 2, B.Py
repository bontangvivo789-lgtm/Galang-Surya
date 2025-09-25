class AkunBank:
    def __init__(self, nama_pemilik, nomor_akun, saldo_awal):
        self.nama_pemilik = nama_pemilik       # public
        self.__nomor_akun = nomor_akun         # private
        if saldo_awal >= 50000:
            self.__saldo = saldo_awal          # private
        else:
            raise ValueError("Saldo awal minimal 50.000!")

    # Method untuk setor uang
    def setor(self, amount):
        if amount > 0:
            self.__saldo += amount
            print(f"Setor {amount} berhasil.")
        else:
            print("Jumlah setor harus lebih dari 0.")

    # Method untuk tarik uang
    def tarik(self, amount):
        if amount <= 0:
            print("Jumlah tarik harus lebih dari 0.")
        elif self.__saldo - amount < 50000:
            print("Gagal: Saldo tidak boleh kurang dari 50.000.")
        else:
            self.__saldo -= amount
            print(f"Tarik {amount} berhasil.")

    # Getter saldo
    def get_saldo(self):
        return self.__saldo

    # Method transfer ke akun lain
    def transfer(self, akun_tujuan, amount):
        if amount <= 0:
            print("Jumlah transfer harus lebih dari 0.")
        elif self.__saldo - amount < 50000:
            print("Gagal: Saldo tidak boleh kurang dari 50.000 setelah transfer.")
        else:
            self.__saldo -= amount
            akun_tujuan.__saldo += amount
            print(f"Transfer {amount} ke {akun_tujuan.nama_pemilik} berhasil.")

# --- Contoh penggunaan ---
akun1 = AkunBank("Galang", "12345", 100000)
akun2 = AkunBank("Surya", "67890", 75000)

print("Saldo awal Galang:", akun1.get_saldo())
print("Saldo awal Surya:", akun2.get_saldo())

akun1.setor(50000)
akun1.tarik(30000)
print("Saldo Galang:", akun1.get_saldo())

akun1.transfer(akun2, 20000)
print("Saldo Galang setelah transfer:", akun1.get_saldo())
print("Saldo Surya setelah menerima:", akun2.get_saldo())
