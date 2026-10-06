#for
#nilai = [75, 60, 80, 90, 50]

#for elemen in nilai: #index = 0, 75
    #if elemen >= 70: 
        #print(f"Lulus dengan nilai: {elemen}")
    #else:
        #print(f"Tidak lulus nilai: {elemen}")

#range
#range(start, stop, step)
#for i in range (5, 0, -1):
    #print(f"Ini angka ke {i}")

#nested for
#for i in range(2): # berhenti sebelum 2 i --> 0 sampai 1
    #for j in range(3): # berhenti sebelum 3 j --> 0 sampai 2
        #print(f"{i} x {j} = {i*j}")
# iterasi 1
# i = 0, j = 0, j = 1, j = 2
# i x j = (i*j)
# 0 x 0 = 0
# 0 x 1 = 0
# 0 x 2 = 0

# iterasi 2
# i = 1, j = 0, j = 1, j = 2
# i x j = (i*j)
# 1 x 0 = 0
# 1 x 1 = 1
# 1 x 2 = 2

#while
#jawab = "df"
#hitung = 0

#while(jawab == "df"):
    #hitung += 1 # 0 -> 1
    #jawab = input("Mau Lanjut? ")

#print(f"Jumlah Perulangan: {hitung}")

#Break
#for i in range(4):
    #print(i)
    #break

#i = 0

#while True:
    #print(i)
    #i += 2
    #if i >= 11:
        #break

Menu = True
while True:
    print("MENU")
    print("1. Makan")
    print("2. Minum")
    print("0. Keluar")
    pilih = int(input("Masukkan Pilihan: "))
    if pilih == 0:
        break
    else:
        print(f"Anda memilih menu ke {pilih}")

#continue
#for i in range(10): # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. iterasi = baris kode yang akan diulang
    #if i % 2 == 0: # jika i habis dibagi 2
        #print(f"skip {i}") # cetak skip i jika i genap
        #continue # lanjut ke iterasi berikutnya
    #print(f"berhasil print {i}") # cetak i jika i ganjil

#for i in range(10):
 #   if i == 9: # jika i sama dengan 9
  #          print("Perulangan dihentikan") # cetak perulangan dihentikan
   #         break # keluar dari perulangan
    #elif i % 2 != 0: # jika i tidak habis dibagi 2
     #   continue # lanjut ke iterasi berikutnya
    #print(i)