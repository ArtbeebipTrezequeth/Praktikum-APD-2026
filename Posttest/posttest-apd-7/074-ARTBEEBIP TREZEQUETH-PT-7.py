# ==========================================
# VARIABEL GLOBAL (Minimal 3 variabel)
# ==========================================
inventory = {0: "diamond", 1: "oak_wood", 2: "iron_ingot"}
program_berjalan = True
role = ""

# ==========================================
# FUNGSI TANPA PARAMETER (2 fungsi)
# ==========================================
def server_name():
    return "My World Server"

def crafting_recipes():
    return ["stick", "oak_plank", "door", "sword", "pickaxe", "axe", "hoe", "shovel", "bow", "furnace", "bed"]

# ==========================================
# FUNGSI DENGAN PARAMETER (2 fungsi)
# ==========================================
def check_recipe_valid(resep, daftar_resep):
    if resep in daftar_resep:
        return True
    return False

def mengurai_slot_input(slot_str):
    try:
        hasil_int = int(slot_str)
        return hasil_int
    except ValueError:
        return None

# ==========================================
# PROSEDUR (2 prosedur - fungsi tanpa return value)
# ==========================================
def tampilkan_selamat_datang():
    """Prosedur untuk menampilkan sambutan server."""
    print("=== WELCOME TO '" + server_name() + "' SERVER! ===")

def tampilkan_inventory(inv):
    """Prosedur untuk menampilkan isi inventory ke layar."""
    print("\n=== [READ] INVENTORY SAAT INI ===")
    if len(inv) == 0:
        print("Inventory kosong.")
    else:
        for slot, item in inv.items():
            print(f"Slot {slot}: {item}")

# ==========================================
# FUNGSI DENGAN 5 VARIABEL LOKAL
# ==========================================
def analisis_slot_detail(slot_str, inv):
    panjang_str = len(slot_str)      # Lokal 1
    apakah_digit = slot_str.isdigit() # Lokal 2
    konversi_angka = -1              # Lokal 3
    status_ada = False               # Lokal 4
    keterangan = "Memeriksa..."      # Lokal 5
    
    if apakah_digit:
        konversi_angka = int(slot_str)
        if konversi_angka in inv:
            status_ada = True
            keterangan = "Slot ditemukan"
        else:
            keterangan = "Slot tidak ada di inventory"
    else:
        keterangan = "Bukan angka valid"
        
    return status_ada

tampilkan_selamat_datang()

role = input("Pilih role Anda (admin / user): ")
while role != "admin" and role != "user":
    print("Role tidak valid! Masukkan 'admin' atau 'user'.")
    role = input("Pilih role Anda (admin / user): ")

daftar_resep_valid = crafting_recipes()

while program_berjalan:
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
                item_baru = input("Masukkan nama item yang ingin ditambah: ")
                slot_baru = len(inventory)
                inventory[slot_baru] = item_baru
                print(f"Berhasil menambahkan '{item_baru}' ke slot {slot_baru}.")

                lagi = input("Ingin menambah item lagi? (ya/keluar): ")
                if lagi == "keluar":
                    aktif_create = False
        elif role == "user":
            aktif_craft = True
            while aktif_craft:
                print("\n=== [MENU CRAFTING KHUSUS USER BIASA] ===")
                print(f"Resep: {', '.join(daftar_resep_valid)}")
                resep = input("Ketik nama item yang ingin di-craft: ")

                if check_recipe_valid(resep, daftar_resep_valid):
                    slot_baru = len(inventory)
                    inventory[slot_baru] = resep
                    print(f"Berhasil craft dan memasukkan '{resep}' ke slot {slot_baru}.")
                else:
                    print("Resep crafting tidak ditemukan!")

                lagi_craft = input("Ingin craft lagi? (ya/keluar): ")
                if lagi_craft == "keluar":
                    aktif_craft = False

    # 2. READ
    elif pilihan_menu == "2":
        aktif_read = True
        while aktif_read:
            tampilkan_inventory(inventory)
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
                tampilkan_inventory(inventory)

                pilih_idx = input("Masukkan nomor slot item yang ingin dikelola: ")
                idx = mengurai_slot_input(pilih_idx)

                if idx is not None:
                    # Penerapan Error Handling spesifik tanpa except Exception (menggunakan KeyError)
                    try:
                        item_terpilih = inventory[idx]
                        if role == "admin":
                            aksi_admin = input("Pilih aksi admin (pindah / ubah_item): ")
                            if aksi_admin == "pindah":
                                tujuan_str = input("Masukkan nomor slot tujuan: ")
                                tujuan = mengurai_slot_input(tujuan_str)
                                if tujuan is not None:
                                    item_pindah = inventory.pop(idx)
                                    if tujuan in inventory:
                                        item_tujuan_lama = inventory[tujuan]
                                        inventory[tujuan] = item_pindah
                                        inventory[idx] = item_tujuan_lama
                                    else:
                                        inventory[tujuan] = item_pindah
                                    print("Berhasil memindahkan item!")
                                else:
                                    print("Nomor slot tujuan harus berupa angka.")
                            elif aksi_admin == "ubah_item":
                                item_baru = input("Masukkan nama item baru: ")
                                inventory[idx] = item_baru
                                print("Berhasil mengubah item")
                            else:
                                print("Masukkan aksi yang benar (pindah / ubah_item).")
                        elif role == "user":
                            tujuan_str = input("Masukkan nomor slot tujuan pindah: ")
                            tujuan = mengurai_slot_input(tujuan_str)
                            if tujuan is not None:
                                item_pindah = inventory.pop(idx)
                                if tujuan in inventory:
                                    item_tujuan_lama = inventory[tujuan]
                                    inventory[tujuan] = item_pindah
                                    inventory[idx] = item_tujuan_lama
                                else:
                                    inventory[tujuan] = item_pindah
                                print("Berhasil memindahkan item!")
                            else:
                                print("Nomor slot tujuan harus angka.")
                    except KeyError:
                        print("Error: Nomor slot tidak ditemukan di dalam inventory.")
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
                tampilkan_inventory(inventory)
                metode_del = input("Hapus (satu / seluruh): ")
                if metode_del == "seluruh":
                    inventory = {}
                    print("Seluruh inventory berhasil dihapus!")
                elif metode_del == "satu":
                    slot_del = input("Masukkan nomor slot yang ingin dihapus: ")
                    idx_s = mengurai_slot_input(slot_del)
                    if idx_s is not None:
                        try:
                            dihapus = inventory.pop(idx_s)
                            print(f"Berhasil menghapus item '{dihapus}' dari slot {idx_s}")
                        except KeyError:
                            print("Error: Nomor slot tidak ditemukan.")
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
        program_berjalan = False

    else:
        print("Peringatan: Pilih menu yang tepat (masukkan antara angka 1 sampai 5)")