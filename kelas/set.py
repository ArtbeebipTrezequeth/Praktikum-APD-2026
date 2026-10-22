#set
#angka = {1, 1, 1, 2, 3, 3, 2+1+3}
#prima = {2, 3, 5, 7}
#print(angka.union(prima.union(angka.union(prima)))

#angka = {1, 1, 1, 2, 3, 3, 2+1+3}
#prima = {2, 3, 5, 7}
#print(angka | prima)

#intersection
#angka = {1, 1, 1, 2, 3, 3, 2+1+3}
#prima = {2, 3, 5, 7}
#print(angka & prima)

#angka = {1, 2, 3, 6}
#prima = {2, 3, 5, 7}
#print(angka.intersection(prima.union(angka)))

#difference
#angka = {1, 2, 3, 6}
#prima = {2, 3, 5, 7}
#print(angka.difference(prima))

#angka = {1, 2, 3, 6}
#prima = {2, 3, 5, 7}
#print(angka - prima)

#angka = {1, 2, 3, 6}
#prima = {2, 3, 5, 7}
#print(prima.discard(5))

#angka = {1, 2, 3, 6}
#prima = {2, 3, 5, 7}
#for item in prima:
#    print(item)



#Dictionary
#kendaraan = {'Mobil' : 'Pajero Sport',
#             'Motor' : 'Yamaha',
#             'Sepeda' : 'BMX'}
#print(kendaraan.get('Motr'))

#kendaraan = {'Mobil' : 'Pajero Sport',
#             'Motor' : 'Yamaha',
#             'Sepeda' : 'BMX'}
#for key, value in kendaraan.items():
#    print(f"{key} : {value} ")

#dictionary union
#kendaraan = {'Mobil' : 'Pajero Sport',
#             'Motor' : 'Yamaha',
#             'Sepeda' : 'BMX'}

#kendaraan['pesawat'] = 'boeing'
#kendaraan.update({"kapal" : "kapal laut",
#                  "Helikopter" :"Maverick"})
#print(kendaraan)

#setdefault
#kendaraan = {'Mobil' : 'Pajero Sport',
#             'Motor' : 'Yamaha',
#             'Sepeda' : 'BMX'}
#key = input("Masukkan Key:")
#kendaraan["Mobil"] = "Toyota"

kendaraan = {'Mobil' : 'Pajero Sport',
             'Motor' : 'Yamaha',
             'Sepeda' : 'BMX'}
kendaraan.update({"Mobil" : "Toyota", "Sepeda" : "Gunung"})
print(kendaraan)

#Del
kendaraan = {'Mobil' : 'Pajero Sport',
             'Motor' : 'Yamaha',
             'Sepeda' : 'BMX'}
del kendaraan['Mobil']
