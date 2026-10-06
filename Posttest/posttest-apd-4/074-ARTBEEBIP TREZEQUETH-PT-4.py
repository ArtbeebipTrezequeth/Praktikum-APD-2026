Username = "Artbeebip"
pin = "074"
saldo = 1000000

print("--Selamat datang di ATM Bank Los Santos--")
print("Masukkan Username dan PIN Anda")
print()



batas_percobaan = 3

while batas_percobaan > 0:
    input_username = input("Username: ")
    input_pin = input("PIN: ")
    if input_username == Username and input_pin == pin:
        while True:
            print()
            print("Selamat datang, ", Username)
            print()
            print("Menu:")
            print("[1] Cek Saldo")
            print("[2] Tarik Tunai")
            print("[3] Setor Tunai")
            print("[4] Keluar")
            Pilihan = int(input("Masukkan pilihan Anda: "))
            if Pilihan == 1:
                print("Saldo Anda saat ini: Rp", saldo)


            elif Pilihan == 2:
                tarikan = int(input("Masukkan jumlah yang ingin ditarik: Rp"))
                if tarikan > saldo:
                    print("Saldo Anda tidak mencukupi.")
                else:
                    saldo -= tarikan
                    print("Transaksi berhasil. Saldo Anda saat ini: Rp", saldo)


            elif Pilihan == 3:
                setor = int(input("Masukkan jumlah yang ingin disetor: Rp"))
                if setor > 0:
                    saldo += setor
                    print("Transaksi berhasil. Saldo Anda saat ini: Rp", saldo)
                else:
                    print("Nominal setor harus lebih dari Rp0")


            elif Pilihan == 4:
                print("Terima kasih telah menggunakan layanan ATM Bank Los Santos")
                batas_percobaan = 0
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")


    else:
        print()
        print("Login gagal! Sisa percobaan Anda: ", batas_percobaan - 1)
        print()
        batas_percobaan -= 1
        if batas_percobaan == 0:
            print()
            print("Akun Anda diblokir. Silahkan hubungi bank.")
            break
