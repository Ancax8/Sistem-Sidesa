from collections import deque
from layanan import save_data

def proses_antrian(data):
    queue = deque()

    for item in data:
        if item["status"] == "menunggu":
            queue.append(item)

    if not queue:
        print("Tidak ada antrian")
        return

    current = queue.popleft()

    for item in data:
        if item["id"] == current["id"]:
            item["status"] = "diproses"

    print("Memproses:", current["nama"])
    save_data(data)