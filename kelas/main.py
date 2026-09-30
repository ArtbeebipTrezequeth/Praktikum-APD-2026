#angka = int(input("Masukkan Angka: "))

#if angka > 0:
#    print("Angka Positif")
#elif angka == 0:
#    print("Angka tepat nol")

#else:
#    print("Angka Negatif")

#umur = 18
#status = "Dewasa" if umur >= 18 else "Belum Dewasa"
#print("Status: ", status)

total_pembelian = int(input("Masukkan total pembelian: "))
if total_pembelian > 200000:
    diskon = total_pembelian * 0.3
elif total_pembelian > 100000:
    diskon = total_pembelian * 0.1
else:
    diskon = 0

print("Diskon yang diperoleh: Rp", diskon)