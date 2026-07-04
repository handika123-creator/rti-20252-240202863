# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario | Seed/Batch | Parameter | Status | Waktu | Output File |
|-------|----------|------------|-----------|--------|-------|-------------|
| 1 | Pilot Study | Batch 1 | N/A | Selesai | Juli 2026 | Pilot_Data.csv |
| 2 | Main Study | Batch 2 | N/A | Rencana | Juli 2026 | Main_Data_T.csv |
| 3 | Main Study | Batch 3 | N/A | Rencana | Juli 2026 | Main_Data_NT.csv |

Jumlah runs per skenario : 1 (menggunakan kuesioner sebagai instrumen)
Total runs               : 30 (responden)

DATA LOG (per run):
  Run ID    : RES-001 (Contoh)
  Timestamp : Otomatis (Google Forms)
  Skenario  : Evaluasi KHS SIM UPB
  Input     : Skor Likert 1-5
  Output    : Skor komposit SUS 0-100
  Anomali   : N/A
  Catatan   : Perangkat (Desktop/Mobile)
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed/Batch | Parameter Kunci | Status |
|-------|----------|------------|----------------|--------|
| 1-5 | Akses KHS | Pilot | N/A | Planned |
| 6-20 | Akses KHS | Batch 2 | N/A | Planned |
| 21-30 | Akses KHS | Batch 3 | N/A | Planned |

**Total skenario:** 1
**Run per skenario:** 30
**Total run keseluruhan:** 30

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
Field | Contoh |
|-------|--------|
| Run ID | RES-001 |
| Timestamp | 2026-07-03T10:00:00 |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Seed | N/A |
| Code version | SIM-UPB-v1 |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| Skor SUS | float | 0.0 – 100.0 |

**Format output:** [x] CSV / [ ] JSON / [ ] Database / [ ] Lainnya: ____

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | Google Form tidak bisa diakses | Re-invite responden |
| Hasil ekstrem | Skor 0 atau 100 | Investigasi validitas |
| Waktu eksekusi anomali | Pengisian < 1 menit | Delete entry (Straight-lining) |
| Inkonsistensi | Skor Q1 dan Q2 bertolak belakang | Data Cleaning |

**Prinsip:**
Meskipun lingkungan eksternal tidak bisa dikontrol 100%, saya akan memitigasinya dengan cara:

1. Memberikan instruksi skenario tugas yang baku di awal survei agar setiap responden memiliki beban kognitif awal yang sama.

2. Menambahkan pertanyaan screening (seperti: 'Apakah Anda menggunakan perangkat Desktop/Mobile?') untuk mengelompokkan data. Jika nanti ditemukan anomali,
  saya bisa melihat apakah anomali tersebut disebabkan oleh faktor teknis (perangkat) atau murni karena masalah desain antarmuka KHS.

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Hanya mengandalkan asumsi, risiko bias konfirmasi tinggi.
**Yang akan dilakukan berbeda:**
> Menerapkan protokol data cleaning yang ketat agar riset lebih objektif dan saintifik.