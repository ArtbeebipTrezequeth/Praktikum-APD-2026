Username = "Bip"
Password = 74

input_username = input("Masukkan Username: ")
input_password = int(input("Masukkan Password: "))

if input_username == Username and input_password == Password:
    print("Login berhasil")
else:
    print("Login gagal")

ID_Game = input("Masukkan ID Game: ")
print("Pilih Game: ")
print("Genshin Impact")
print("Minecraft")
print("Mobile Legends")

Nama_Game = input("Masukkan Nama Game: ")
print("Pilih Kategori Top Up: ")
print("Kecil")
print("Menengah")
print("Besar")

Kategori_Top_Up = input("Masukkan Kategori Top Up: ")
if Kategori_Top_Up == "Kecil":
    Harga_Dasar = 15000
elif Kategori_Top_Up == "Menengah":
    Harga_Dasar = 50000
elif Kategori_Top_Up == "Besar":
    Harga_Dasar = 100000

print("Pilih Metode Pembayaran: ")
print("E-Wallet")
print("Pulsa")
metode_pembayaran = input("Masukkan Metode Pembayaran: ")
biaya_admin = 2500 if metode_pembayaran == "Pulsa" else 500

total_biaya = Harga_Dasar + biaya_admin
total_biaya = str(total_biaya)
biaya_admin = str(biaya_admin)
Struk_Pembelian = "ID Game: " + ID_Game + ", Nama Game: " + Nama_Game + ", Kategori Top Up: " + Kategori_Top_Up + ", Metode Pembayaran: " + metode_pembayaran + ", Biaya Admin: " + biaya_admin + ", Total Biaya: " + total_biaya
print("Struk Pembelian: ", Struk_Pembelian)