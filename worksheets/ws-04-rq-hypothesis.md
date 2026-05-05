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

```
RQ → Variable → Metric → Data → Analysis
```

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

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : Ketiadaan validasi empiris kuantitatif (seperti pengujian System Usability Scale) pada perancangan antarmuka mobile sistem informasi akademik pasca-pembuatan artefak visual.

Research Question:
  Tipe         : [ ] Comparison  [x] Improvement  [ ] Exploratory
  Formulasi    : Apakah perancangan prototype antarmuka mobile menggunakan pendekatan Design Thinking menghasilkan skor System Usability Scale (SUS) yang secara signifikan lebih tinggi dibandingkan antarmuka website My CIC eksisting berdasarkan pengujian terhadap mahasiswa?
  Variabel IV  : Jenis Antarmuka (Website My CIC Eksisting vs Prototype Mobile My CIC Baru)
  Variabel DV  : Tingkat Kegunaan (Usability)
  Metrik       : Skor System Usability Scale (Skala 0-100)
  Dataset      : Respons kuesioner SUS dari sampel mahasiswa yang telah menguji kedua antarmuka.
  Baseline     : Skor SUS dari antarmuka website My CIC eksisting (sistem legacy).
Quality Check RQ:
  [x] Variabel spesifik
  [x] Metrik jelas
  [x] Baseline ada
  [x] Konteks disebutkan
  [x] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Bukti empiris mengenai seberapa besar efektivitas dan peningkatan usabilitas dari transisi website akademik menjadi aplikasi mobile yang dirancang melalui Design Thinking.
  Jenis kontribusi        : [x] Improvement  [ ] Comparison  [ ] Novel approach
  Gap yang diisi          : Method Gap (Menyediakan validasi empiris yang terstandar pada artefak desain mobile yang sebelumnya absen di literatur baseline).

Hypothesis Pair:
  H₀ : Tidak ada peningkatan skor SUS secara signifikan (skor mobile $\le$ skor web) antara prototype aplikasi mobile dan website eksisting.
  H₁ : Prototype aplikasi mobile menghasilkan skor SUS yang secara signifikan lebih tinggi dibandingkan antarmuka website eksisting.
  Threshold              : p-value < 0.05 pada uji statistik komparasi (T-Test) dan skor akhir minimum 68.
  Justifikasi threshold  : p-value < 0.05 membuktikan bahwa perbaikan tersebut bukan kebetulan (signifikan secara statistik), dan skor 68 adalah batas kelayakan (Acceptable) standar global untuk instrumen SUS.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Method Gap (Ketiadaan validasi empiris menggunakan metrik kuantitatif pasca-pembuatan artefak prototype antarmuka akademik mobile).

**RQ versi pertama (tulis bebas):**
> Bagaimana cara membuat UI/UX mobile My CIC yang lebih modern dan mudah digunakan oleh mahasiswa?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik |Tidak|Hanya menyebut "membuat UI/UX" tanpa metode perancangan spesifik.|
| Metrik terukur |Tidak|Kata "mudah digunakan" sangat subjektif dan tidak ada alat ukurnya.|
| Baseline |Tidak|Tidak ada pembanding terhadap sistem yang lama.|
| Dataset/konteks |Ya|Konteksnya aplikasi My CIC untuk mahasiswa.|

**Tipe RQ:** [ ] Comparison / [x] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah perancangan prototype antarmuka mobile menggunakan pendekatan Design Thinking menghasilkan skor System Usability Scale (SUS) yang secara signifikan lebih tinggi dibandingkan antarmuka website My CIC eksisting berdasarkan pengujian terhadap mahasiswa?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Tidak ada peningkatan skor SUS secara signifikan (skor mobile $\le$ skor web) antara prototype antarmuka mobile dengan website akademik eksisting. |
| H₁ |Terdapat peningkatan skor SUS secara signifikan pada prototype antarmuka mobile dibandingkan dengan website akademik eksisting.|
| Metrik |Skor kuantitatif System Usability Scale (0 - 100).|
| Threshold |p-value < 0.05 (uji beda/T-Test) dan capaian skor prototype minimum 68.|
| Justifikasi threshold |Mengonfirmasi bahwa peningkatan yang terjadi bersifat valid secara statistik dan memenuhi standar kelayakan minimum usability industri.|

**Apakah hipotesis ini falsifiable?** [x] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? H₀ gagal ditolak (terbukti salah) jika hasil pengolahan data kuesioner menunjukkan rata-rata skor SUS prototype mobile sama dengan atau justru lebih rendah daripada skor website lama.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Apakah perancangan prototype mobile dengan Design Thinking menghasilkan skor SUS lebih tinggi dibandingkan website eksisting? |
| Variable (IV) | Jenis/Platform Antarmuka (Website Eksisting vs Prototype Mobile). |
| Variable (DV) |Tingkat Kegunaan (Usability Level).|
| Metric |Instrumen hitung System Usability Scale (skor 0-100).|
| Data source |Data primer: Hasil angket kuesioner SUS dari mahasiswa yang mensimulasikan task pada kedua antarmuka.|
| Analysis method |Uji Prasyarat (Normalitas) dan Uji Komparatif Statistik (misal: Paired Sample T-Test jika respondennya sama).|

**Apakah rantai lengkap?** [x] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Perancangan User Interface dan User Experience Aplikasi My CIC (Muhyidin et al., 2020)
**RQ yang diekstrak:** Bagaimana merancang antarmuka (UI/UX) mobile untuk aplikasi My CIC yang memiliki desain menarik dan modern?
**Komponen yang hilang:** 
  ~Metode spesifik evaluasi tidak disebutkan.
  ~Metrik terukur tidak ada (hanya klaim subjektif "menarik dan modern").
  ~Baseline (perbandingan dengan efisiensi sistem lama) tidak disertakan sama sekali. RQ tersebut masih berada di level Engineering (sekadar membangun), bukan Research (membuktikan secara empiris).