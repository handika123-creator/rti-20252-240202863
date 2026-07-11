# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

> **Mengapa reproducibility penting?** Sains dibangun di atas prinsip verifikasi — temuan harus bisa dikonfirmasi oleh peneliti lain. _Replicability crisis_ yang terjadi di banyak paper riset ML/AI disebabkan oleh environment tidak terdokumentasi: orang lain tidak bisa reproduksi, hasil diragukan, kepercayaan terhadap temuan hilang. Prinsip: **dokumentasi environment = snapshot kredibilitas riset Anda.**

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
   - **Docker** = teknologi container yang "membungkus" aplikasi beserta seluruh dependency-nya dalam satu unit terisolasi. Hasilnya: kode berjalan identik di laptop, server, maupun reviewer lain. Intro singkat: `docker run -v $(pwd):/workspace environment-image python run_experiment.py`
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Dependency Locking

Mengandalkan "install library terbaru" berbahaya: versi berbeda = perilaku berbeda = hasil tidak reproducible. Praktik:
- **Python**: buat `requirements.txt` dengan versi eksplisit: `scikit-learn==1.3.2`, lalu kunci dengan `pip freeze > requirements.txt`
- **Conda**: gunakan `conda env export > environment.yml` untuk snapshot lengkap
- **Node.js/R/Julia**: gunakan `package-lock.json` / `renv.lock` / `Project.toml` — semua fungsi serupa: lock versi + hash

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : AMD Ryzen 3 7320U
  RAM     : 8 GB
  GPU     : AMD Radeon Graphics
  Storage : 256 GB SSD (119 GB + 117 GB)

Software:
  OS        : Windows 11 Home Single Language
  Runtime   : Web Browser (Chrome/Edge untuk Google Forms)
  Framework : Google Forms (Instrumen) & Python (Analisis)

Dependencies:

| Library/Tool | Version | Sumber | Peran / Fungsi |
|---------|---------|--------|---------------|
| Google Forms | 2026 Build | cloud | Platform perekaman Skala Likert responden |
| Python (Pandas) | v3 | lokal | Kalkulasi *reverse coding* (Inversi skor SUS) |
| Python (SciPy) | v1 | lokal | Pengujian hipotesis (*One-Sample T-Test*) |

Konfigurasi:
  Config file     : Skrip Python sus_calculator.py
  Random seed     : Kriteria Inklusi Responden Acak Berstrata
  Hyperparameters : Threshold Baseline SUS = 68, Alpha = 0.05

Reproducibility Check:
  [x] File data mentah (*raw data* .csv) tersimpan aman dan tidak dimanipulasi.
  [x] Rumus kalkulasi (inversi skor SUS) didokumentasikan dalam skrip sus_calculator.py.
  [x] File data mentah dan *file* analisis terpisah secara fisik untuk menjaga integritas data.
  [x] README instruksi reproduksi mencakup langkah *data cleaning* dan prosedur statistik dengan Python.
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| **CPU** | AMD Ryzen 3 7320U with Radeon Graphics |
| **RAM** | 8 GB |
| **GPU** | AMD Radeon(TM) Graphics |
| **OS** | Windows 11 Home Single Language |
| **Runtime** | Chrome Browser & Python |
| **Framework** | Google Forms |
| **Kriteria Input** | Mahasiswa UPB aktif (divalidasi via pertanyaan screening di Google Form) |

**Dependencies (minimal 5):**

| Library/Tool | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| Google Forms | Latest | Pengumpulan data SUS 10-item yang terstruktur dan mudah di-*export*. |
| Python (Pandas) | v3 | Validasi data, *data cleaning* (straight-lining), dan kalkulasi skor SUS. |
| Python (SciPy) | v1 | Uji hipotesis statistik (*One-Sample T-Test*) untuk membandingkan skor SUS dengan threshold 68. |
| Google Drive | Sync-v2 | Penyimpanan *raw data* yang aman dan sinkronisasi antar perangkat. |
| SUS Scoring Template | v1.0 | Standarisasi perhitungan agar tidak ada *human error* dalam rumus konversi. |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Input File | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | Raw_Data_KHS.csv | Skor Mean SUS & P-Value | — |
| 2 | Raw_Data_KHS.csv | Skor Mean SUS & P-Value | [x] Ya |
| 3 | Raw_Data_KHS.csv | Skor Mean SUS & P-Value | [x] Ya |


___________________________________________________

**Checklist kontrol yang sudah diterapkan:**
- [x] Tautan kuesioner ditutup (*closed accepting responses*) sebelum diekspor ke CSV.
- [x] Rumus kalkulasi di dalam Python dapat divalidasi keakuratannya.
- [x] File *Raw Data* dipisahkan dari file *Analysis Data*.
- [x] Parameter *Test Value* (68) di Python diketik secara absolut.

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
# Judul Eksperimen: Evaluasi Komparatif Usabilitas Portal Akademik (SIAKAD Universitas Putra Bangsa)

## 1. Environment
> Hardware: AMD Ryzen 3 7320U, 8GB RAM, 256GB SSD, Radeon Graphics; OS: Windows 11 Home; Runtime: Python v3.

## 2. Installation
> Unduh repositori ini.
> Buka terminal / IDE Python.
> Pastikan library Pandas dan SciPy sudah terpasang.

## 3. Data
> Sumber: Kuesioner primer Google Forms (Juni/Juli 2026).
> Ukuran: N >= 30 Mahasiswa Aktif UPB.
> Format: Raw_KHS_Responses.csv (File berisi timestamp dan jawaban skala Likert 1-5 murni).

## 4. Execution
> Salin kolom item pertanyaan SUS (Q1-Q10) dari Raw_KHS_Responses.csv.
> Simpan data respons mentah ke file `Data_KHS_Raw.csv` di folder `04-data`.
> Buka Sheet "Result" untuk melihat skor rata-rata komposit secara otomatis.
> Jalankan skrip `sus_calculator.py` untuk menghitung skor dan uji T-Test secara otomatis.

## 5. Configuration
> Reverse Coding Positif (Ganjil): Jawaban - 1
> Reverse Coding Negatif (Genap): 5 - Jawaban
> Skor Individu SUS: (Total Nilai Ganjil + Ganjil + Genap + Genap) * 2.5

## 6. Expected Output
> Rata-rata Skor SUS (Angka 0-100) dan penempatan huruf mutu (Grade A-F).
> Output console Python menunjukkan nilai signifikansi (P-Value < 0.05).
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [ ] Repeatability / [x] Reproducibility / [ ] Belum keduanya
**Komponen yang belum terdokumentasi:**
> Komponen yang sudah terdokumentasi meliputi raw data yang di-anonymized serta kode sumber perhitungan Python. Dengan instruksi di README, pihak lain (dosen/peneliti lain) dapat melakukan kalkulasi ulang dan mendapatkan hasil yang konsisten dengan riset saya.