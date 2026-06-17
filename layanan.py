import csv

def load_data():
    data = []
    try:
        with open("antrian.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass
    return data


def save_data(data):
    with open("antrian.csv", mode="w", newline="") as file:
        fieldnames = ["id", "nama", "layanan", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)