# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (DSR). Penting untuk membedakan keduanya:

| Paradigma | Cara Kerja | Contoh di TI |
|-----------|-----------|---------------|
| **Positivis** | Uji hipotesis dengan eksperimen terkontrol | Apakah CNN lebih akurat dari RF pada dataset X? |
| **Design Science Research** | Bangun artefak (sistem/model/framework) untuk menguji proposisi | Dapatkah arsitektur hybrid CNN+LSTM membuktikan peningkatan recall ≥5%? |
| **Interpretivis** | Pahami makna melalui konteks & kualitatif | Bagaimana peneliti manafsirkan anomali data sensor IoT? |

Dalam DSR, artefak **bukan tujuan akhir** — ia adalah instrumen untuk menghasilkan pengetahuan. Pertanyaan riset tetap harus difalsifikasi.

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
**Nama Peneliti**    : Handika Dwi Ardiyanto  
**Tanggal**          : 03/07/2026  

**1. Ketika membaca klaim "Sistem Informasi Akademik ini sudah sangat layak dan mudah digunakan":**
*   **Pertanyaan pertama saya:** Apakah klaim kelayakan tersebut dibuktikan melalui pengukuran kuantitatif menggunakan instrumen yang tervalidasi, atau hanya asumsi subjektif?
*   **Data yang dibutuhkan untuk verifikasi:** Skor kuantitatif usabilitas dari responden target (mahasiswa) menggunakan instrumen *System Usability Scale* (SUS).

**2. Posisi paradigma:**
*   **Pendekatan:** [x] Positivis  [ ] Interpretivis  [ ] Design Science  [ ] Mixed
*   **Alasan:** Riset ini bertujuan mengukur fenomena subjektif (pengalaman pengguna pada KHS) menjadi data metrik numerik yang objektif melalui eksperimen pengukuran terstandar.

**3. Identifikasi distorsi:**
*   **Asumsi tersembunyi:** Ketiadaan keluhan formal ke pihak admin diasumsikan tidak ada masalah pada antarmuka KHS SIM UPB.
*   **Sumber bias potensial:** *Sampling bias* jika responden didominasi *expert users* (mahasiswa tingkat akhir).
*   **Langkah mitigasi:** Menerapkan *purposive sampling* agar representasi responden merata lintas angkatan dan program studi.

**4. Komitmen etika:**
*   **Data yang tidak akan dimanipulasi:** Skor mentah kuesioner SUS, termasuk *outlier* yang menunjukkan ketidakpuasan ekstrem.
*   **Batasan yang diakui sejak awal:** Evaluasi berfokus murni pada aspek antarmuka (UI/UX) halaman KHS, tanpa mengevaluasi performa server/backend.

---

## Latihan 1 — Identifikasi Distorsi

**Paper yang dipilih:**
> **Judul:** Usability Testing pada Sistem Informasi Akademik IAIN Salatiga Menggunakan Metode System Usability Scale
> **Penulis (Tahun):** Mei Prabowo & Agung Suprapto (2021)
> **Sumber/Link DOI:** JISKa, Vol. 6, No. 1, 2021

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| **Reality → Data** | Menyebarkan kuesioner SUS kepada mahasiswa untuk menilai Sistem Informasi Akademik. | **Satisficing Bias:** Responden asal mengisi skala netral agar cepat selesai tanpa membaca teliti. |
| **Data → Processing** | Mengonversi skor Likert mentah menjadi aturan hitung *System Usability Scale* (0-100). | **Kesalahan Kalkulasi:** Kesalahan saat *reverse coding* pada pertanyaan negatif (nomor genap). |
| **Processing → Analysis** | Menggabungkan seluruh skor individu menjadi satu skor rata-rata sistem (*mean score*). | **Pengabaian Konteks:** Rata-rata yang tinggi menutupi fakta ada fitur spesifik yang skornya sangat rendah. |
| **Analysis → Inference** | Menyimpulkan bahwa sistem secara keseluruhan masuk kategori *Acceptable* (Layak). | **Halo Effect:** Menganggap status *Acceptable* berarti sistem sempurna dan tidak butuh iterasi desain lagi. |
| **Inference → Knowledge** | Menetapkan bahwa SIAKAD tersebut sudah optimal melayani mahasiswa. | **External Validity Threat:** Menganggap keberhasilan UI/UX di kampus tersebut pasti sama jika diterapkan di kampus lain. |

**Distorsi paling besar di tahap:** Data → Processing dan Processing → Analysis.

**Dua distorsi spesifik yang teridentifikasi:**
1. *Satisficing & Acquiescence Bias* saat pengambilan data kuesioner.
2. Ketergantungan absolut pada nilai rata-rata yang dapat menutupi *outlier* keluhan dari pengguna.

---

## Latihan 2 — Analisis Kasus Etika

**Skenario:** Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| **Kejujuran ilmiah** | Peneliti wajib mempertahankan data outlier dalam dataset asli. Menghapus data tanpa justifikasi metodologis adalah bentuk manipulasi (*cherry-picking*). |
| **Transparansi** | Melaporkan analisis utama dengan outlier, dan dapat menyertakan analisis tambahan (tanpa outlier) beserta kronologis teknis penyebab munculnya anomali tersebut. |
| **Peer review** | Memberikan kesempatan bagi penguji untuk mengevaluasi batasan nyata dari eksperimen dan mendiskusikan variabel pengganggu (*confounding variables*). |

**Keputusan akhir dan justifikasi:**
> Peneliti **tidak boleh** menghapus data outlier tersebut. Dalam pengujian usabilitas, outlier berupa skor rendah sering merepresentasikan minoritas pengguna yang menghadapi hambatan nyata. Membuang data ini melanggar prinsip objektivitas dan membiaskan realitas.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Evaluasi Usabilitas Fitur Kartu Hasil Studi (KHS) pada Sistem Informasi Manajemen (SIM) UPB Menggunakan Metode System Usability Scale (SUS).

> **Skala 1–5:** 1 = tidak sesuai sama sekali dengan topik ini, 5 = sangat sesuai dan dominan digunakan pada riset bertopik serupa.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| **Kesesuaian dengan topik (1–5)** | **5** — Sangat sesuai; mengukur usabilitas menjadi metrik kuantitatif terstandar (SUS). | **2** — Tidak sesuai; tidak menggali kedalaman makna secara kualitatif. | **1** — Tidak sesuai; tidak berfokus membangun artefak (sistem/desain) baru. |
| **Jenis data yang dikumpulkan** | Metrik interval numerik (Skor SUS), rata-rata, standar deviasi. | Transkrip wawancara terbuka, observasi lapangan mendalam. | Arsitektur, wireframe, purwarupa, pengujian iteratif produk. |
| **Limitasi paradigma** | Tidak mampu menceritakan konteks spesifik di balik kebingungan responden pada elemen tertentu. | Rentan terhadap bias subjektivitas peneliti. | Membutuhkan waktu dan sumber daya yang difokuskan pada kreasi, bukan evaluasi objektif. |

**Paradigma yang dipilih:** Positivis.  
**Alasan:** Riset ini menggunakan kuesioner terstandar untuk menghasilkan data kuantitatif dalam menguji kelayakan sistem. Fokus utamanya adalah observasi objektif dan pengukuran empiris, bukan perancangan atau interpretasi makna kualitatif.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelum mempelajari modul ini, saya cenderung langsung menerima klaim efektivitas suatu sistem tanpa kritis terhadap asal data. Sekarang, saya akan mempertanyakan validitas pengukuran dan keterwakilan sampel: *"Apa instrumen yang digunakan untuk membuktikan angka tersebut, dan apakah populasi pengujiannya terbebas dari sampling bias?"*