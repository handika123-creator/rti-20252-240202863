# Jadwal & Log Pelaksanaan Penelitian

Catatan kronologis pelaksanaan tiap tahap (sumber: penyelesaian dokumen Worksheet (WS) 01 hingga 11 dan instrumen penelitian). 

## Log Pelaksanaan

| Tanggal | Tahap | Aktivitas | Referensi |
|---|---|---|---|
| 2026-07-01 | Tahap 1 (WS-01 s.d. WS-04) | **Fondasi Riset:** Perumusan masalah terkait keluhan *usability* fitur KHS di SIM UPB. Penyusunan tinjauan pustaka, penetapan hipotesis (Target Skor SUS > 68), dan penentuan metodologi riset menggunakan survei kuantitatif. | `WS-01` s.d. `WS-04` |
| 2026-07-02 | Tahap 2 (WS-05 s.d. WS-08) | **Desain Riset:** Identifikasi variabel penelitian, pemilihan instrumen baku System Usability Scale (SUS) 10-item, perancangan skenario eksperimen (tugas akses KHS), dan penetapan rencana uji statistik (One-Sample T-Test dengan Python). | `WS-05` s.d. `WS-08` |
| 2026-07-03 | Tahap 3 (WS-09 s.d. WS-10) | **Persiapan Eksekusi:** Penyusunan bab Implementasi & Kontrol Lingkungan. Menetapkan *Execution Plan* dengan target 30 responden mahasiswa aktif (Purposive Sampling) yang dibagi menjadi Batch 1 (Pilot) dan Batch 2 (Main). | `WS-09`, `WS-10` |
| 2026-07-04 | Tahap 4 (WS-11) | **Validasi & Integritas Data:** Menyusun parameter *Data Validation Checklist* dan protokol penanganan anomali (*Data Cleaning*), menetapkan tindakan tegas untuk kasus data tidak lengkap dan *straight-lining*. | `WS-11` |
| 2026-07-04 | Tahap Instrumen | **Perancangan Kuesioner:** Pembuatan draf final kuesioner SUS 10-item, lengkap dengan instruksi skenario tugas pencarian nilai KHS untuk diimplementasikan ke dalam Google Forms. | `Draf Google Form SUS` |
| 2026-07-05 | Tahap Instrumen | **Penyiapan Instrumen Digital:** Memindahkan kuesioner ke Google Forms dan membuat skrip Python (`sus_calculator.py`) untuk otomatisasi konversi skor dan uji statistik. | `Google Forms`, `sus_calculator.py` |
| 2026-07-11 | Eksekusi Riset | **Pengumpulan Data:** Telah terkumpul 30 respons dari responden mahasiswa UPB. Data mentah telah diunduh ke `Data_KHS_Raw.csv`. | `Data_KHS_Raw.csv` |
| 2026-07-12 | Analisis Data | **Otomatisasi & Hitung SUS:** Menjalankan skrip Python `sus_calculator.py` untuk mengolah data, menghasilkan rata-rata 63.33 (H1 Ditolak). | `Data_KHS_Processed.csv` |
| 2026-07-12 | Tahap Akhir | **Penulisan Laporan:** Penyelesaian worksheet WS-12 s.d. WS-16, pembuatan draf manuskrip, dan penulisan laporan akhir penelitian. | `naskah-jurnal.md`, `laporan-penelitian.md` |

## Status Ringkas

- **Tahap Perencanaan & Desain (WS-01 s.d. WS-11)**: Selesai 100%. 
- **Tahap Instrumen & Eksekusi**: Selesai 100%. 
- **Tahap Pemrosesan & Analisis (WS-12 s.d. WS-14)**: Selesai 100%. Data berhasil diolah menggunakan Python dengan skor rata-rata SUS 63.33.
- **Tahap Publikasi & Laporan (WS-15 s.d. WS-16)**: Selesai 100%. Manuskrip draf jurnal dan laporan akhir riset telah berhasil disusun.

## Item Tindak Lanjut (Checklist Sebelum Pengumpulan Data)

- [x] Penyelesaian dokumen metodologi dan perencanaan (WS-01 s.d. WS-11)
- [x] Pembuatan Draf Kuesioner SUS dan Instruksi Skenario
- [x] Memindahkan draf pertanyaan dan konfigurasi skala linear (1-5) ke Google Forms
- [x] Membuat skrip Python (`sus_calculator.py`) untuk automasi konversi skor Likert dan perhitungan analitik
- [x] Melakukan *Pilot Study* dengan menyebarkan kuesioner ke 5 responden awal untuk evaluasi pemahaman instrumen
- [x] Menyebarkan kuesioner utama ke 25 target responden aktif (Mahasiswa UPB)

## Item Tindak Lanjut Berikutnya (Pemrosesan & Analisis)

- [x] Melakukan pembersihan data (*data cleaning*) pada `Data_KHS_Raw.csv` (membuang *straight-lining* atau jawaban tidak valid)
- [x] Menghitung dan mengonversi skor SUS menggunakan formulasi yang sudah ditentukan
- [x] Melakukan uji statistik (One-Sample T-Test)
- [x] Mengerjakan worksheet analisis dan presentasi hasil (WS-12 s.d. WS-16)
- [x] Menyusun dokumen draf publikasi/manuskrip ilmiah dan laporan akhir riset

## Korespondensi

*(belum ada — tambahkan catatan korespondensi atau revisi dari pembimbing/dosen di sini saat tersedia)*