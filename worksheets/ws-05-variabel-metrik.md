# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: Apakah perancangan prototype antarmuka mobile menggunakan pendekatan Design Thinking menghasilkan skor System Usability Scale (SUS) yang secara signifikan lebih tinggi dibandingkan antarmuka website My CIC eksisting berdasarkan pengujian terhadap mahasiswa?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
|Jenis Antarmuka| IV   |Platform Sistem Informasi|Kategori platform: Website Eksisting vs Aplikasi Mobile Baru|Nominal|   -    |Menetapkan dua kondisi pengujian (environment) yang berbeda kepada responden penelitian.|Menjawab komparasi langsung antara sistem legacy (sumber masalah) dengan prototype (usulan solusi).|
|Tingkat Kegunaan (Usability)| DV   |Pengalaman dan Kemudahan Pengguna|Skor System Usability Scale (SUS)|Interval|Poin (0-100)|Responden mengisi 10 item kuesioner SUS skala Likert setelah menyelesaikan skenario tugas.|SUS adalah instrumen standar global yang terbukti valid, reliabel, dan direkomendasikan dalam literatur terkait (misal: Winandy et al., 2024; Firjinia et al., 2025).|
|Skenario Tugas (Task)| CV   |Kesetaraan Beban Kognitif|Daftar instruksi tugas spesifik (misal: "Cari nilai IPK", "Cek Jadwal Kuliah")|Nominal|     -  |Memberikan lembar instruksi tugas yang sama persis saat responden menguji Website maupun Mobile.|Memastikan bahwa perbedaan skor SUS murni karena kualitas desain UI/UX, bukan karena tugas di satu platform lebih mudah dari platform lainnya.|

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [x] Setiap langkah terdokumentasi
  [x] Tidak ada "lompatan logis"
  [x] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Apakah perancangan prototype antarmuka mobile menggunakan pendekatan Design Thinking menghasilkan skor System Usability Scale (SUS) yang secara signifikan lebih tinggi dibandingkan antarmuka website My CIC eksisting berdasarkan pengujian terhadap mahasiswa?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Jenis Antarmuka | IV | Platform Media Digital | Kategori: Antarmuka Web vs Antarmuka Mobile | Nominal | — |
| Usability | DV | Kemudahan Penggunaan (User Experience) | Skor Komposit System Usability Scale | Interval | Skor (0-100) |
| Tingkat Kesulitan | CV | Kesetaraan Beban Interaksi | Kesamaan Skenario Tugas (Task Scenario) | Nominal | - |
| Karakteristik Pengguna | CV | Keterwakilan Demografi Pengguna Akhir | Status Mahasiswa Aktif Lintas Program Studi | Nominal | - |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [x] Tidak
> Jika ya, di mana? Rantai operasionalisasi sudah solid. Konsep abstrak "kemudahan UI/UX" telah dijabarkan menggunakan metrik komposit (SUS) yang memang secara akademis diciptakan untuk mengukur usability.

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | Kuesioner SUS terbukti mampu mewakili 3 dimensi utama usabilitas: efisiensi, efektivitas, dan kepuasan pengguna. |
| Sensitive | 4 | Rentang penilaian 0-100 dan penggunaan 10 item pertanyaan dengan skala Likert 1-5 cukup peka untuk menangkap perbedaan kualitas antarmuka yang diuji. |
| Feasible | 5 | Sangat praktis, gratis, dan waktu pengumpulannya cepat karena dapat didistribusikan melalui Google Form langsung kepada partisipan. |

**Apakah perlu secondary metric?** [x] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? disarankan menambahkan Time on Task (Waktu Penyelesaian Tugas dalam satuan Detik) sebagai secondary metric. Skor SUS hanya mengukur persepsi subjektif pengguna (apa yang dirasakan). Kita memerlukan Time on Task sebagai ukuran objektif untuk memastikan apakah aplikasi mobile tersebut benar-benar membuat pengguna lebih cepat dalam menyelesaikan tugas administrasinya dibandingkan website lama.

**Contoh kasus ceiling effect untuk metrik ini:**
> Ceiling effect (efek mentok di atas) akan terjadi jika skenario tugas yang diberikan terlalu dangkal/mudah (misalnya: "Silakan Login ke sistem"). Karena tugasnya sangat mudah, hampir semua responden akan memberikan skor SUS sempurna (mendekati 100) baik untuk Website maupun aplikasi Mobile. Akibatnya, metrik gagal mendeteksi antarmuka mana yang sebenarnya lebih unggul karena datanya menumpuk di nilai maksimal.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | Apakah semua data point terkumpul? | Ada risiko data bolong karena responden tidak sengaja melewati beberapa pertanyaan SUS. | Mengaktifkan fitur Required (Wajib Diisi) pada setiap butir pertanyaan SUS di dalam Google Form agar tidak bisa di-submit jika belum lengkap. |
| Consistency | Apakah ada kontradiksi internal? | Kuesioner SUS memiliki pertanyaan positif (nomor ganjil) dan negatif (nomor genap). Responden yang malas mungkin akan menjawab skor "5" secara lurus ke bawah (straight-lining). | Melakukan tahapan Data Cleaning. Data dari responden yang menjawab dengan pola seragam (misal: 5-5-5-5-5 atau 1-1-1-1-1) akan dihapus dari analisis karena kontradiktif. |
| Validity | Apakah benar-benar mengukur yang dimaksud? | Terdapat kemungkinan bias di mana responden malah memberi nilai buruk karena sinyal internetnya lambat, bukan karena UI/UX-nya buruk. | Memberikan briefing tertulis/lisan sebelum pengujian bahwa evaluasi ini murni untuk menilai tata letak, kemudahan navigasi, dan desain visual, BUKAN menilai kecepatan server atau internet. |
| Representativeness | Apakah sampel mewakili populasi target? | Sering kali pengujian desain IT hanya diberikan kepada teman sekelas di Fakultas IT yang sudah terbiasa dengan teknologi kompleks. | Menerapkan Stratified Random Sampling dengan merekrut responden mahasiswa dari fakultas non-IT (misal: Ekonomi, Hukum, Sastra) agar mewakili populasi mahasiswa awam secara keseluruhan. |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih metrik utama setelah melihat hasil data disebut p-hacking (atau HARKing: Hypothesizing After Results are Known) karena ini adalah bentuk manipulasi akademik. Peneliti mengutak-atik atau menukar alat ukur hanya untuk mencari nilai statistik yang terlihat "signifikan" agar risetnya terkesan sukses. Hal ini merusak prinsip objektivitas dan falsifiability (kemampuan hipotesis untuk dibuktikan salah).
> Perbedaannya dengan eksplorasi data yang sah (Exploratory Data Analysis / EDA) terletak pada transparansi. Dalam EDA, metrik utama (seperti SUS) sudah dikunci sejak awal. Jika saat menganalisis data peneliti tidak sengaja menemukan pola menarik lain (misalnya: "Ternyata mahasiswa semester akhir lebih cepat menggunakan aplikasi dibanding maba"), hal tersebut dilaporkan secara jujur sebagai "Temuan Eksploratif" atau "Observasi Tambahan", bukan diklaim sebagai tujuan utama atau pembuktian hipotesis riset yang disembunyikan.