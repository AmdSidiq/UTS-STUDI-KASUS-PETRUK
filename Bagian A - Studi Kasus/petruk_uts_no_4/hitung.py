def hitung_rata_rata(daftar_nilai):
    if len(daftar_nilai) == 0:
        raise ValueError("Daftar nilai tidak boleh kosong")

    total = 0

    for n in daftar_nilai:
        total = total + float(n)

    rata_rata = total / len(daftar_nilai)
    return rata_rata


def tentukan_status(rata_rata, batas_lulus=70):
    status = "Lulus" if rata_rata >= batas_lulus else "Tidak Lulus"
    return status


def tampilkan_hasil(nama, daftar_nilai, batas_lulus=70):
    rata_rata = hitung_rata_rata(daftar_nilai)
    status = tentukan_status(rata_rata,batas_lulus=batas_lulus)

    print("Nama :", nama)
    print("Rata-rata :", rata_rata)
    print("Status :", status)
    print()


if __name__ == "__main__":
    nilai_budi = ["80", "75", "90"]
    nilai_sari = ["60", "65", "55", "70"]

    tampilkan_hasil("Budi", nilai_budi)
    tampilkan_hasil("Sari", nilai_sari)