def baca_suhu(nama_file):
    data = []

    with open(nama_file, "r") as file:
        for baris in file:
            baris = baris.strip()

            if baris == "":
                continue

            hari, suhu = baris.split(";")

            data.append({"hari": hari, "suhu": int(suhu)})

    return data


def analisis_suhu(*data_suhu, batas_panas=32):
    if len(data_suhu) == 0:
        raise ValueError("Data suhu tidak boleh kosong.")

    data_harian = []
    total_suhu = 0
    jumlah_hari_panas = 0

    for data in data_suhu:
        suhu = data["suhu"]

        if suhu >= batas_panas:
            kategori = "Panas"
            jumlah_hari_panas += 1
        else:
            kategori = "Normal"

        data_harian.append({"hari": data["hari"], "suhu": suhu, "kategori": kategori})

        total_suhu += suhu

    rata_rata = total_suhu / len(data_harian)

    tertinggi = max(data_harian, key=lambda item: item["suhu"])
    terendah = min(data_harian, key=lambda item: item["suhu"])

    return {"data_harian": data_harian, "rata_rata": rata_rata, "tertinggi": tertinggi, "terendah": terendah,"jumlah_hari_panas": jumlah_hari_panas}


def tulis_laporan(hasil, nama_file="laporan_suhu.txt"):
    with open(nama_file, "w") as file:
        file.write("LAPORAN ANALISIS SUHU MINGGUAN\n")
        file.write("==============================\n")
        file.write(
            f"Rata-rata suhu: {hasil['rata_rata']:.2f} C\n"
        )
        file.write(
            f"Suhu tertinggi: {hasil['tertinggi']['suhu']} C "
            f"({hasil['tertinggi']['hari']})\n"
        )
        file.write(
            f"Suhu terendah: {hasil['terendah']['suhu']} C "
            f"({hasil['terendah']['hari']})\n"
        )
        file.write(
            f"Jumlah hari Panas: {hasil['jumlah_hari_panas']}\n"
        )

        file.write("\nRincian suhu harian:\n")

        for data in hasil["data_harian"]:
            file.write(
                f"{data['hari']}: {data['suhu']} C - "
                f"{data['kategori']}\n"
            )


if __name__ == "__main__":
    try:
        data = baca_suhu("suhu.txt")

        hasil = analisis_suhu(*data, batas_panas=32)

        tulis_laporan(hasil)

        with open("laporan_suhu.txt", "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("Error: file suhu.txt tidak ditemukan.")

    except ValueError as error:
        print("Error:", error)
