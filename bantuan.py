def generate_id(data):
    if not data:
        return "A001"
    
    last_id = data[-1]["id"]
    number = int(last_id[1:]) + 1
    return f"A{number:03d}"

def pilih_layanan():
    layanan_list = [
        "Surat Domisili",
        "Surat Usaha",
        "Surat Nikah",
        "KTP",
        "Kartu Keluarga"
    ]

    print("\n=== PILIH LAYANAN ===")
    for i in range(len(layanan_list)):
        print(f"{i+1}. {layanan_list[i]}")

    while True:
        try:
            pilih = int(input("Pilih layanan (angka): "))
            if 1 <= pilih <= len(layanan_list):
                return layanan_list[pilih - 1]
            else:
                print("Pilihan tidak valid")
        except ValueError:
            print("Masukkan angka!")