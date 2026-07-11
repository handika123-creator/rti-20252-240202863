# Tahap 4 — Eksekusi Analisis Data & Pengujian Hipotesis

**Status:** Selesai
**Tujuan:** Menganalisis *raw data* menjadi *processed data* guna membuktikan apakah antarmuka KHS telah memenuhi standar kualitas.

## Proses
1. **Eksekusi Komputasi:** Menjalankan perintah `python sus_calculator.py` di terminal *environment* proyek yang secara instan akan memanen data mentah kuesioner.
2. **Kalkulasi Deskriptif:** Mesin secara independen akan merangkum skor agregat demografi. Pada tahap ini diperoleh angka mean akhir **63.33** (SD = 11.75).
3. **Pengujian Inferensial:** Mesin membandingkan rata-rata 63.33 terhadap *baseline target* 68.0 menggunakan uji signifikansi T-Test parametrik satu arah (1-tailed).
4. **Analisis Kualitatif:** Menginspeksi secara manual kolom *feedback* yang ada di dalam *dataset* untuk mengaitkan mengapa angka kuantitatif (63.33) bisa terjadi. Identifikasi terbesar menunjuk pada kendala akses gawai (skala UI tidak ramah *mobile*).
5. **Manajemen Berkas Output:** Skrip Python secara mandiri meletakkan salinan data matang ke direktori luaran.

## Deliverable
- File data *processed* CSV siap pakai (Tersimpan di `06-output/Data_KHS_Processed.csv`).
- Output analisis terminal (*Descriptive & T-Test result*).
