from layanan import load_data
from antrian import (
    tambah_antrian,
    tampilkan_data,
    update_status,
    cari_data
)
from antrian2 import proses_antrian


def menu():
    while True:
        data = load_data()

        print("\n=== SIDESA SIRNABAYA ===")
        print("1. Ambil Antrian")
        print("2. Lihat Data")
        print("3. Proses Antrian")
        print("4. Update Status")
        print("5. Cari Data")
        print("6. Keluar")

        pilih = input("Pilih: ")

        if pilih == "1":
            tambah_antrian(data)
        elif pilih == "2":
            tampilkan_data(data)
        elif pilih == "3":
            proses_antrian(data)
        elif pilih == "4":
            update_status(data)
        elif pilih == "5":
            cari_data(data)
        elif pilih == "6":
            print("Keluar program")
            break
        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    menu()