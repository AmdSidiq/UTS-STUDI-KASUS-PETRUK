def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                try:
                    npm, nama, nilai = baris.strip().split(";")
                    nilai = int(nilai)

                    data.append({"npm": npm, "nama": nama, "nilai": nilai})
                    
                except ValueError:
                    print("Ada baris tidak valid dan dilewati.")

        return data

    except FileNotFoundError:
        print(f"Error: file {nama_file} belum ada.")
        return []

hasil = baca_data("nilai.txt")
print(hasil)