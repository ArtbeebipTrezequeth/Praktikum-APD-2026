from prettytable import PrettyTable
from fungsi import server_name

def tampilkan_selamat_datang():
    print(f"=== WELCOME TO '{server_name()}' SERVER! ===")

def tampilkan_inventory(inv):
    print("\n=== [READ] INVENTORY SAAT INI ===")
    if len(inv) == 0:
        print("Inventory kosong.")
    else:
        # Menggunakan Prettytable untuk membuat tabel rapi
        table = PrettyTable()
        table.field_names = ["Slot", "Item Name"]
        
        for slot, item in inv.items():
            table.add_row([slot, item])
            
        print(table)