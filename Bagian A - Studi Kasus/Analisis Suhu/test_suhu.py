import unittest
from suhu import analisis_suhu


class TestAnalisisSuhu(unittest.TestCase):

    def setUp(self):
        data = [
            {"hari": "Senin", "suhu": 31},
            {"hari": "Selasa", "suhu": 33},
            {"hari": "Rabu", "suhu": 29},
            {"hari": "Kamis", "suhu": 35},
            {"hari": "Jumat", "suhu": 32},
            {"hari": "Sabtu", "suhu": 30},
            {"hari": "Minggu", "suhu": 28}
        ]

        self.hasil = analisis_suhu(
            *data,
            batas_panas=32
        )

    def test_rata_rata_suhu(self):
        self.assertAlmostEqual(
            self.hasil["rata_rata"],
            31.142857142857142
        )
        
    def test_jumlah_hari_panas(self):
        self.assertEqual(
            self.hasil["jumlah_hari_panas"],
            3
        )

    def test_kategori_suhu(self):
        self.assertEqual(
            self.hasil["data_harian"][4]["kategori"],
            "Panas"
        )
        self.assertEqual(
            self.hasil["data_harian"][0]["kategori"],
            "Normal"
        )

    def test_data_kosong(self):
        with self.assertRaises(ValueError):
            analisis_suhu()


if __name__ == "__main__":
    unittest.main()
