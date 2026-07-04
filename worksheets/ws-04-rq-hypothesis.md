# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

`RQ → Variable → Metric → Data → Analysis`

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

**RQ-CONTRIBUTION-HYPOTHESIS**

**Gap Statement** : Ketiadaan evaluasi empiris terisolasi menggunakan instrumen SUS secara spesifik pada fitur Kartu Hasil Studi (KHS) di lingkungan Sistem Informasi Manajemen (SIM) UPB.

**Research Question:**
* **Tipe** : [ ] Comparison  [ ] Improvement  [x] Exploratory
* **Formulasi** : Bagaimana tingkat usabilitas fitur Kartu Hasil Studi (KHS) pada SIM UPB jika diukur menggunakan metode *System Usability Scale* (SUS) dibandingkan dengan standar *acceptable score*?
* **Variabel IV** : Fitur KHS pada SIM UPB eksisting
* **Variabel DV** : Tingkat Usabilitas Pengguna
* **Metrik** : Skor komposit *System Usability Scale* (0-100)
* **Dataset** : Respons kuesioner primer dari sampel mahasiswa aktif pengguna SIM UPB
* **Baseline** : Standar kelayakan global SUS (Skor batas bawah = 68)

**Quality Check RQ:**
* [x] Variabel spesifik
* [x] Metrik jelas
* [x] Baseline ada
* [x] Konteks disebutkan
* [x] Memerlukan eksperimen (bukan hanya survei literatur)

**Contribution Statement:**
* **Apa yang baru diketahui** : Bukti empiris objektif mengenai kelayakan antarmuka fitur KHS SIM UPB beserta identifikasi area interaksi yang menyebabkan *bottleneck* bagi mahasiswa.
* **Jenis kontribusi** : [ ] Improvement  [x] Comparison (terhadap standar global)  [ ] Novel approach
* **Gap yang diisi** : *Method/Empiric Gap* & *Context Gap* (Memberikan *baseline* kuantitatif pada sistem spesifik yang sebelumnya belum pernah dievaluasi secara formal).

**Hypothesis Pair:**
* **H₀** : Skor rata-rata SUS fitur KHS SIM UPB <= 68 (Sistem belum memenuhi standar kelayakan usabilitas).
* **H₁** : Skor rata-rata SUS fitur KHS SIM UPB > 68 (Sistem memenuhi atau melampaui standar kelayakan usabilitas).
* **Threshold** : Skor rata-rata > 68 dengan signifikansi statistik (*p-value* < 0.05 pada *One-Sample T-Test*).
* **Justifikasi threshold** : Skor 68 merupakan ambang batas (*cutoff point*) "Acceptable" berdasarkan literatur standar global pengukuran instrumen SUS (Bangor et al., 2009).

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Ketiadaan evaluasi terisolasi menggunakan instrumen SUS untuk spesifik fitur KHS pada konteks lingkungan Sistem Informasi Manajemen UPB.

**RQ versi pertama (tulis bebas):**
> Apakah halaman KHS di SIM UPB mudah digunakan oleh mahasiswa saat ini?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| **Metode spesifik** | Tidak | Hanya bertanya "mudah digunakan" tanpa menyebut alat ukur (SUS). |
| **Metrik terukur** | Tidak | Kata "mudah" subjektif dan tidak memiliki skor ukur pasti. |
| **Baseline** | Tidak | Tidak ada standar acuan kelayakan sebagai pembanding. |
| **Dataset/konteks** | Ya | Lingkungan SIM UPB dan partisipan mahasiswa. |

**Tipe RQ:** [ ] Comparison / [ ] Improvement / [x] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Bagaimana tingkat usabilitas fitur Kartu Hasil Studi (KHS) pada SIM UPB jika diukur menggunakan metode *System Usability Scale* (SUS) dibandingkan dengan standar *acceptable score* (68)?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| **H₀** | Tidak terdapat tingkat usabilitas yang memadai pada fitur KHS SIM UPB (Skor rata-rata SUS <= 68). |
| **H₁** | Terdapat tingkat usabilitas yang memadai pada fitur KHS SIM UPB (Skor rata-rata SUS > 68). |
| **Metrik** | Skor kuantitatif *System Usability Scale* (0-100). |
| **Threshold** | Capaian skor > 68 dan *p-value* < 0.05 melalui pengujian statistik (misal: *One-Sample T-Test* terhadap nilai uji 68). |
| **Justifikasi threshold** | Menegaskan bahwa kelayakan sistem secara empiris melampaui batas *Marginal/Poor* menuju klasifikasi *Acceptable/Good*. |

**Apakah hipotesis ini falsifiable?** [x] Ya / [ ] Tidak
> **Bagaimana cara membuktikannya salah?** H₀ gagal ditolak jika hasil pengolahan kuesioner dari sampel mahasiswa menghasilkan skor rata-rata SUS di bawah atau sama dengan 68, membuktikan bahwa kelayakan sistem masih di bawah standar.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| **RQ** | Bagaimana tingkat usabilitas fitur KHS pada SIM UPB jika diukur dengan SUS dibandingkan dengan standar kelayakan 68? |
| **Variable (IV)** | Objek Sistem Konstan (Fitur KHS pada SIM UPB). |
| **Variable (DV)** | Tingkat Usabilitas Pengguna (*Usability Level*). |
| **Metric** | Instrumen 10 item *System Usability Scale* (Skala Likert 1-5, dikonversi menjadi skor 0-100). |
| **Data source** | Data Primer: Hasil pengisian angket kuesioner *online* oleh mahasiswa aktif setelah berinteraksi dengan KHS. |
| **Analysis method** | Analisis deskriptif komparatif (rata-rata skor dibandingkan dengan aturan *Curved Grading Scale*) dan uji signifikansi *One-Sample T-Test*. |

**Apakah rantai lengkap?** [x] Ya / [ ] Tidak
> **Jika tidak, tahap mana yang perlu direvisi?** (Rantai operasionalisasi sudah lengkap dan logis, dari penentuan objek hingga instrumen pengolahannya).

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Perancangan UI/UX Aplikasi My CIC Layanan Informasi Akademik (Muhyidin et al., 2020)
**RQ yang diekstrak:** Bagaimana cara merancang antarmuka (UI/UX) aplikasi My CIC yang memiliki desain lebih menarik dan modern?
**Komponen yang hilang:** RQ tersebut sama sekali tidak mencantumkan **metode evaluasi spesifik** (seperti SUS, UEQ, atau Heuristic), tidak ada **metrik yang terukur** (kata "menarik dan modern" tidak bisa dikuantifikasi), dan ketiadaan **baseline** (tidak ada perbandingan skor performa dengan sistem sebelumnya). Hal ini menunjukkan bahwa paper tersebut memecahkan masalah *Engineering* (membuat barang jadi), bukan masalah *Research* (membuktikan klaim secara saintifik).