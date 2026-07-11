# Tahap 2 — Pengumpulan Data Survei Kuantitatif

**Status:** Selesai
**Tujuan:** Menghimpun respons empiris dari pengguna target melalui metode *purposive sampling*.

## Proses
1. **Digitalisasi Instrumen:** Mentransfer rancangan kuesioner dari Tahap 1 ke dalam formulir daring (Google Forms).
2. **Mitigasi Bias:** Memastikan validasi *wajib isi* pada seluruh soal untuk mencegah data rumpang (*missing values*), serta mengatur urutan pertanyaan agar selang-seling antara pernyataan bernada positif dan negatif demi meminimalkan *straight-lining*.
3. **Eksekusi:** Menyebarkan *link* kuesioner ke populasi mahasiswa aktif. Survei dijalankan secara masif dalam jangka waktu pendek untuk menghindari risiko bertepatan dengan masa pembaruan sistem (*maintenance/patch*) oleh developer kampus.
4. **Ekstraksi Data:** Mengunduh lembar rentang (*spreadsheet*) hasil survei menjadi sebuah file `Data_KHS_Raw.csv`. Total sampel yang diperoleh adalah N=30 (memenuhi syarat minimum parametrik).

## Deliverable
- Dataset mentah CSV (Tersimpan di `04-data/Data_KHS_Raw.csv`).
