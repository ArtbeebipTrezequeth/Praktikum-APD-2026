def server_name():
    return "My World Server"

def crafting_recipes():
    return ["stick", "oak_plank", "door", "sword", "pickaxe", "axe", "hoe", "shovel", "bow", "furnace", "bed"]

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

def analisis_slot_detail(slot_str, inv):
    apakah_digit = slot_str.isdigit()
    status_ada = False

    if apakah_digit:
        konversi_angka = int(slot_str)
        if konversi_angka in inv:
            status_ada = True
    return status_ada