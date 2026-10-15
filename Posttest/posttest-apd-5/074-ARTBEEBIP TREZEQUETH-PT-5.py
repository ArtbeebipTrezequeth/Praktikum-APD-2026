inventory = ["diamond", "oak_wood", "iron_ingot"]

print("=== WELCOME TO 'My World' SERVER! ===")
role = input("Pilih role Anda (admin / user): ")
while role != "admin" and role != "user":
  print("Role tidak valid! Masukkan 'admin' atau 'user'.")
  role = input("Pilih role Anda (admin / user): ")

berjalan_program = True
while berjalan_program:
  print("\n=== MENU CRUD INVENTORY ===")
  print("1. Create")
  print("2. Read")
  print("3. Update")
  print("4. Delete")
  print("5. Keluar")

  pilihan_menu = input("Pilih menu (1-5): ")

  # 1. CREATE
  if pilihan_menu == "1":
    if role == "admin":
      aktif_create = True
      while aktif_create:
        print("\n=== [CREATE - ADMIN] ===")
        item_baru = input("Masukkan nama item yang ingin diambil: ")
        inventory.append(item_baru)
        print(f"Berhasil menambahkan '{item_baru}' ke inventory.")

        lagi = input("Ingin mengambil item lagi? (ya/keluar): ")
        if lagi == "keluar":
          aktif_create = False
    elif role == "user":
      aktif_craft = True
      while aktif_craft:
        print("\n=== [MENU CRAFTING KHUSUS USER BIASA] ===")
        print("Resep: stick, oak_plank, door, sword, pickaxe, axe, hoe, shovel, bow, furnace, bed")
        resep = input("Ketik nama item yang ingin di-craft: ")

        resep_valid = False
        if (resep == "stick" or resep == "oak_plank" or resep == "door" or resep == "sword" or resep == "pickaxe" or resep == "axe" or resep == "hoe" or resep == "shovel" or resep == "bow" or resep == "furnace" or resep == "bed"):
          resep_valid = True

        if resep_valid:
          inventory.append(resep)
          print(f"Berhasil craft dan memasukkan '{resep}' ke inventory.")
        else:
          print("Resep crafting tidak ditemukan!")

        lagi_craft = input("Ingin craft lagi? (ya/keluar): ")
        if lagi_craft == "keluar":
          aktif_craft = False

  # 2. READ
  elif pilihan_menu == "2":
    aktif_read = True
    while aktif_read:
      print("\n=== [READ] INVENTORY SAAT INI ===")
      if len(inventory) == 0:
        print("Inventory kosong.")
      else:
        idx_r = 0
        while idx_r < len(inventory):
          print(f"Slot {idx_r}: {inventory[idx_r]}")
          idx_r += 1

      keluar_read = input("Apakah ingin keluar ke menu CRUD? (ya/tidak): ")
      if keluar_read == "ya":
        aktif_read = False

  # 3. UPDATE
  elif pilihan_menu == "3":
    aktif_update = True
    while aktif_update:
      if len(inventory) == 0:
        print("Tidak ada yang bisa diperbarui (Inventory kosong).")
        keluar_kosong = input("Apakah ingin keluar ke menu CRUD? (ya/tidak): ")
        if keluar_kosong == "ya":
          aktif_update = False

      else:
        print("\n=== [UPDATE] ===")
        idx_u = 0
        while idx_u < len(inventory):
          print(f"Slot {idx_u}: {inventory[idx_u]}")
          idx_u += 1

        pilih_idx = input("Masukkan nomor slot item yang ingin dikelola: ")

        is_num = True
        if len(pilih_idx) == 0:
          is_num = False
        else:
          for i in pilih_idx:
            if i not in "0123456789":
              is_num = False

        if is_num:
          idx = int(pilih_idx)
          if idx >= 0 and idx < len(inventory):
            if role == "admin":
              aksi_admin = input("Pilih aksi admin (pindah / ubah_item): ")
              if aksi_admin == "pindah":
                tujuan_str = input("Masukkan nomor slot tujuan: ")
                is_tujuan = True
                if len(tujuan_str) == 0:
                  is_tujuan = False
                else:
                  for i in tujuan_str:
                    if i not in "0123456789":
                      is_tujuan = False
                if is_tujuan:
                  tujuan = int(tujuan_str)
                  if tujuan >= 0 and tujuan < len(inventory):
                    item_pindah = inventory.pop(idx)
                    inventory.insert(tujuan, item_pindah)
                    print("Berhasil memindahkan item!")
                  else:
                    print("Nomor slot tujuan tidak valid.")
                else:
                  print("Nomor slot tujuan harus berupa angka.")
              elif aksi_admin == "ubah_item":
                item_baru = input("Masukkan nama item baru: ")
                inventory[idx] = item_baru
                print("Berhasil mengubah item")
              else:
                print("Masukkan aksi yang benar(pindah / ubah_item).")
            elif role == "user":
              tujuan_str = input("Masukkan nomor slot tujuan pindah: ")
              is_tujuan = True
              if len(tujuan_str) == 0:
                is_tujuan = False
              else:
                for i in tujuan_str:
                  if i not in "0123456789":
                    is_tujuan = False
              if is_tujuan:
                tujuan = int(tujuan_str)
                if tujuan >= 0 and tujuan < len(inventory):
                  item_pindah = inventory.pop(idx)
                  inventory.insert(tujuan, item_pindah)
                  print("Berhasil memindahkan item!")
                else:
                  print("Nomor slot tujuan tidak valid.")
              else:
                print("Nomor slot tujuan harus angka.")
          else:
            print("Nomor slot tidak ditemukan.")
        else:
          print("Nomor slot harus berupa angka.")

        keluar_up = input("Apakah ingin keluar ke menu CRUD? (ya/tidak): ")
        if keluar_up == "ya":
          aktif_update = False

  # 4. DELETE
  elif pilihan_menu == "4":
    aktif_delete = True
    while aktif_delete:
      if len(inventory) == 0:
        print("Tidak ada item yang bisa dihapus (Inventory kosong).")
        keluar_del_kosong = input("Apakah ingin keluar ke menu CRUD? (ya/tidak): ")
        if keluar_del_kosong == "ya":
          aktif_delete = False
        else:
          print("Peringatan: Tidak ada item yang bisa dihapus.")
      else:
        print("\n=== [DELETE] ===")
        idx_d = 0
        while idx_d < len(inventory):
          print(f"Slot {idx_d}: {inventory[idx_d]}")
          idx_d += 1

        mode_del = input("Hapus (satu / seluruh): ")
        if mode_del == "seluruh":
          inventory = []
          print("Seluruh inventory berhasil dihapus!")
        elif mode_del == "satu":
          slot_del = input("Masukkan nomor slot yang ingin dihapus: ")
          is_sd = True
          if len(slot_del) == 0:
            is_sd = False
          else:
            for i in slot_del:
              if i not in "0123456789":
                is_sd = False
          if is_sd:
            idx_s = int(slot_del)
            if idx_s >= 0 and idx_s < len(inventory):
              dihapus = inventory.pop(idx_s)
              print(f"Berhasil menghapus item '{dihapus}'")
            else:
              print("Nomor slot tidak valid.")
          else:
            print("Nomor slot harus angka.")
        else:
          print("Mode hapus tidak dikenal.")

        keluar_del = input("Apakah ingin keluar ke menu CRUD? (ya/tidak): ")
        if keluar_del == "ya":
          aktif_delete = False

  # 5. KELUAR
  elif pilihan_menu == "5":
    print("Keluar dari program")
    print("Logging out from server...")
    print("Logged out!")
    berjalan_program = False

  else:
    print("Peringatan: Pilih menu yang tepat (masukkan antara angka 1 sampai 5)")