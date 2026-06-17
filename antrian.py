from layanan import save_data
from bantuan import generate_id
from bantuan import generate_id, pilih_layanan

def tambah_antrian(data):
    id = generate_id(data)
    nama = input("Nama: ")
    layanan_user = pilih_layanan()

    data.append({
        "id": id,
        "nama": nama,
        "layanan": layanan_user,
        "status": "menunggu"
    })

    save_data(data)

    print(f"\nNama {nama} masuk ke dalam antrian")
    print(f"Tiket antrian: {id}")


def tampilkan_data(data):
    if not data:
        print("Data kosong")
        return

    print("\n=== DATA ANTRIAN ===")
    for item in data:
        print(f"{item['id']} | {item['nama']} | {item['layanan']} | {item['status']}")


def update_status(data):
    id = input("Masukkan ID: ")

    for item in data:
        if item["id"] == id:
            print("1. Selesai")
            print("2. Batal")

            pilih = input("Pilih: ")

            if pilih == "1":
                item["status"] = "selesai"
            else:
                item["status"] = "batal"

    save_data(data)


def cari_data(data):
    keyword = input("Cari nama: ")

    for item in data:
        if keyword.lower() in item["nama"].lower():
            print(item)