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
  Runtime   : Figma (Browser-based) & Node.js
  Framework : Chrome 126.x

Dependencies:
| Library | Version | Sumber | Hash/Checksum |
|---------|---------|--------|---------------|
| Figma App | Latest | Official | - |
| Chrome | 126.x | Google | - |
| NumPy | 1.26.4 | PyPI | - |
| SciPy | 1.12.0 | PyPI | - |
| Matplotlib | 3.8.3 | PyPI | - |

Konfigurasi:
  Config file     : config_params.json
  Random seed     : 42
  Hyperparameters : default

Reproducibility Check:
  [x] Dependency terdokumentasi (requirements.txt / lock file)
  [x] Seed ditetapkan di semua level (Python, NumPy, framework)
  [x] Config di version control
  [x] README instruksi reproduksi lengkap
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | AMD Ryzen 3 7320U |
| RAM | 8 GB |
| GPU | AMD Radeon Graphics |
| OS | Windows 11 Home Single Language |
| Runtime | Figma, Node.js |
| Framework | Figma Interactive Prototype, Chrome 126.x |
| Random Seed | 42 |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| Figma App | Latest | Simulasi interaksi purwarupa |
| Chrome | 126.x | Pengujian sistem web eksisting |
| NumPy | 1.26.4 | Pengolahan data kuantitatif |
| SciPy | 1.12.0 | Uji statistik Paired Sample T-Test |
| Matplotlib | 3.8.3 | Visualisasi data hasil usabilitas |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | 42 | 45.2 detik | — |
| 2 | 42 | 45.2 detik | [x] Ya / [ ] Tidak |
| 3 | 42 | 45.2 detik | [x] Ya / [ ] Tidak |

**Jika hasil berbeda, kemungkinan penyebab:**

> Variasi minor pada metrik Time on Task disebabkan oleh human error saat menekan tombol stopwatch manual. Mitigasi dilakukan dengan melakukan 3 kali pengulangan dan mengambil nilai rata-rata (mean).

___________________________________________________

**Checklist kontrol yang sudah diterapkan:**
- [x] Random seed di-set di semua level
- [x] Tidak ada background process yang mengganggu
- [x] Cache dibersihkan antar-run
- [x] Config file yang sama untuk semua run

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
# Judul Eksperimen: Evaluasi Komparatif Usabilitas Portal Akademik (SIAKAD Universitas Putra Bangsa)

## 1. Environment
> Hardware: AMD Ryzen 3 7320U, 8GB RAM, 256GB SSD, Radeon Graphics; OS: Windows 11 Home; Runtime: Figma, Chrome 126.x

## 2. Installation
> Pastikan koneksi internet stabil (minimal 10 Mbps). Akses prototype Figma dan gunakan peramban Google Chrome terbaru.

## 3. Data
> Data skor System Usability Scale (SUS) 0-100 dan metrik Time on Task (detik). Populasi: Mahasiswa S1 Ilmu Komputer.

## 4. Execution
> Jalankan skenario tugas pada prototype Figma dan sistem eksisting, rekam durasi waktu dengan stopwatch digital.

## 5. Configuration
> File config: config_params.json (berisi parameter target waktu ideal).

## 6. Expected Output
> Rekapan skor SUS dan durasi Time on Task per partisipan, serta grafik perbandingan usabilitas.
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [ ] Repeatability / [x] Reproducibility / [ ] Belum keduanya
**Komponen yang belum terdokumentasi:**
> Automated logging untuk durasi waktu pengerjaan tugas masih belum tersedia, saat ini masih mengandalkan stopwatch manual.
