# Tahap 3 — Pembuatan Skrip Otomatisasi Kalkulator SUS (Python)

**Status:** Selesai
**Tujuan:** Mengotomatisasi seluruh proses perhitungan manual untuk mencegah *human-error* dan mempercepat *data pipelines*.

## Proses
1. **Transisi Perangkat Lunak:** Memutuskan beralih dari pengolah data statistik grafis tradisional (seperti SPSS atau MS Excel) menuju *scripting* berbasis bahasa **Python**. Pendekatan ini dipastikan mampu memberikan aspek *reproducibility* secara mutlak.
2. **Library Requirements:** Skrip memanfaatkan paket `pandas` untuk melakukan *data wrangling* dan manipulasi *dataframe* CSV, serta paket `scipy` (`scipy.stats`) untuk mengeksekusi uji parametrik *T-Test*.
3. **Konstruksi Skrip `sus_calculator.py`:**
   - **Data Loading:** Fungsi membaca direktori `../04-data/`.
   - **Reverse Coding Engine:** Fungsi untuk mengonversi pertanyaan SUS ganjil menjadi `Skor - 1` dan pertanyaan SUS genap menjadi `5 - Skor`.
   - **Aggregation:** Fungsi akumulasi skor akhir 0-100 per individu (`total * 2.5`).
   - **Statistical Engine:** Mengeksekusi statistik deskriptif dan inferensial 1-tailed (H1 > 68).
   - **Export Data:** Menulis balik *dataframe* matang ke `../06-output/Data_KHS_Processed.csv`.

## Deliverable
- File skrip Python fungsional siap eksekusi (Tersimpan di `05-kode/sus_calculator.py`).
