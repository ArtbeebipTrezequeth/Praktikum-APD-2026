komponen_1 = 120000
komponen_2 = 135000
komponen_3 = 150000
komponen_4 = 175000
komponen_5 = 200000
komponen_6 = 220000
biaya_admin = 15000
total_biaya = komponen_1 + komponen_2 + komponen_3 + komponen_4 + komponen_5 + komponen_6 + biaya_admin
banyak_data = len([komponen_1, komponen_2, komponen_3, komponen_4, komponen_5, komponen_6])
rata_rata = total_biaya / banyak_data
nim = 74
boolean = nim != rata_rata
print("Total Biaya: ", total_biaya)
print("Rata-rata: ", rata_rata)
print("NIM: ", nim)
print("Boolean: ", boolean)