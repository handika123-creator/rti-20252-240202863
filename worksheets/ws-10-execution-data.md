# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

> Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Dalam konteks riset kuesioner, minimum 30 run (responden) menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario (Kriteria Inklusi Responden)
- Jumlah run per skenario (Target Responden)
- Random seed per run (Penyebaran Acak/Purposive)
- Urutan eksekusi (Pilot Test & Main Execution)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, kriteria aktif
3. **Hasil** — Semua metrik, skor SUS
4. **Metadata** — Waktu eksekusi, kelengkapan data

Format: Excel/CSV — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering (Asal Jalan) | Research (Valid) |
|---|---|---|
| Run | Sekali (deploy) | Multiple (min 30 responden) |
| Logging | Error log, access log | Semua parameter, raw data, skor akhir |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → drop/cleaning |
| Urutan | Tidak penting | Bisa bias — perlu screening awal |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → Drop data invalid
- **Data yang bias** jika hanya simpan run "berhasil" (Misal: Straight-lining)

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → pengumpulan sampel acak memengaruhi validitas
3. "Run gagal langsung hapus" → kehilangan temuan potensial (wajib log di WS-11)
4. "Semua run harus hari ini" → fatigue (kuesioner disebar bertahap)

---

## Template A.10 — Execution Plan & Data Log

**EXECUTION PLAN**

| Batch # | Skenario / Fase | Target Sampling | Rentang Waktu | Status | Output File |
|---|---|---|---|---|---|
| 1 | Pilot Test & Sebar Awal | 4 Responden | 4 - 5 Juli 2026 | Selesai | Data_KHS_Raw.xlsx |
| 2 | Penyebaran Utama (Part 1) | 11 Responden | 6 - 9 Juli 2026 | Selesai | Data_KHS_Raw.xlsx |
| 3 | Penyebaran Utama (Part 2) | 15 Responden | 10 - 11 Juli 2026 | Selesai | Data_KHS_Raw.xlsx |

Jumlah target responden  : 30
Total aktual terkumpul   : 30

**DATA LOG (per run / baris Excel):**
- Run ID    : R-001 s.d. R-030
- Timestamp : [Otomatis dari Google Forms]
- Skenario  : Evaluasi antarmuka KHS SIM UPB
- Input     : Jawaban Likert 1-5 (Q1 - Q10)
- Output    : Kalkulasi Skor SUS (0 - 100)
- Anomali   : Deteksi std deviasi (Straight-lining)
- Catatan   : Validasi screening KHS

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # / Batch | Skenario | Seed / Kriteria | Parameter Kunci | Status |
|---|---|---|---|---|
| 1 | Pilot (Uji Form) | Mahasiswa UPB | Aktif fitur KHS | Selesai |
| 2 | Main Execution | Mahasiswa UPB | Aktif fitur KHS | Selesai |
| 3 | Final Follow-up | Mahasiswa UPB | Aktif fitur KHS | Selesai |

**Total skenario:** 1 (Evaluasi SUS KHS)
**Run per skenario (Target):** 30
**Total run keseluruhan (Aktual):** 30

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|---|---|
| Run ID | R-001 |
| Timestamp | 2026-07-04T22:35:22 |
| Nama/Prodi | Febri Muhsinin / Ilmu Komputer |

**Konfigurasi:**
| Field | Contoh |
|---|---|
| Kriteria Screening | Akses KHS Sebelumnya = Ya |
| Form Version | Final SUS 10-Item |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|---|---|---|
| Jawaban Q1-Q10 | Integer | 1 - 5 |
| Skor SUS | Float | 0.0 - 100.0 |
| Kritik/Saran | String | Bebas |

**Format output:** [ ] CSV / [ ] JSON / [ ] Database / [x] Lainnya: Excel (.xlsx)

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---|---|---|
| Run gagal (Missing Data) | Responden lupa isi Q5 | Form diset "Wajib Diisi", tolak submit jika kosong |
| Hasil ekstrem (Straight-lining) | Menjawab angka 3 semua | Hitung Std Deviasi. Jika = 0, hapus baris, catat di log |
| Waktu eksekusi anomali | Submit dalam 5 detik | Flag sebagai data mencurigakan (speeding) |
| Inkonsistensi kriteria | Belum pernah akses KHS | Drop data dari perhitungan rata-rata akhir |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Sering menguji aplikasi hanya berbekal opini sendiri atau 1-2 teman terdekat (*single run*). Risikonya, hasilnya sangat bias dan tidak mewakili populasi mahasiswa secara umum.

**Yang akan dilakukan berbeda:**
> Menerapkan *multiple runs* dengan target 30 responden riil menggunakan metrik SUS. Ini menghasilkan data berdistribusi normal, rata-rata (mean) yang dapat dipertanggungjawabkan, dan meminimalisir bias subjektivitas.