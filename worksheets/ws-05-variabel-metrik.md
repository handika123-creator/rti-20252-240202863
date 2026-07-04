# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

`Problem → Concept → Variable → Metric → Data → Result`

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

**VARIABLE & METRIC DEFINITION**

**Research Question:** Bagaimana tingkat usabilitas fitur Kartu Hasil Studi (KHS) pada SIM UPB jika diukur menggunakan metode *System Usability Scale* (SUS) dibandingkan dengan standar *acceptable score*?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
| Objek Evaluasi | IV (Konstan) | Sistem Informasi Akademik | Fitur KHS pada SIM UPB | Nominal | - | Meminta seluruh responden mengakses halaman KHS yang sama di SIM UPB. | Memastikan objek sistem yang dinilai seragam agar tidak ada variabel pengganggu dari halaman lain. |
| Tingkat Usabilitas | DV | Kemudahan & Kepuasan Pengguna | Skor *System Usability Scale* (SUS) | Interval | Poin (0-100) | Pengisian kuesioner 10 item skala Likert (1-5) pasca-interaksi. | SUS adalah standar global yang valid, reliabel, dan efisien untuk mengevaluasi antarmuka sistem. |
| Skenario Tugas | CV | Beban Kognitif Pengguna | Penyelesaian instruksi navigasi | Nominal | - | Memberikan instruksi spesifik (contoh: "Akses KHS dan temukan IPK"). | Memastikan evaluasi berdasar pada tugas yang sama, bukan eksplorasi acak yang bias. |

**Alignment Check:**
  RQ → Concept → Variable → Metric → Data → Result
  [x] Setiap langkah terdokumentasi
  [x] Tidak ada "lompatan logis"
  [x] Metrik mengukur apa yang dimaksud (construct validity)

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Bagaimana tingkat usabilitas fitur Kartu Hasil Studi (KHS) pada SIM UPB jika diukur menggunakan metode *System Usability Scale* (SUS) dibandingkan dengan standar *acceptable score*?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Sistem Akademik | IV | Platform Media Digital | Halaman KHS SIM UPB Eksisting | Nominal | — |
| Usabilitas | DV | Pengalaman Pengguna (UX) | Skor Komposit SUS | Interval | Poin (0-100) |
| Tingkat Kesulitan | CV | Kesetaraan Beban Interaksi | Kesamaan Instruksi Skenario Tugas | Nominal | — |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [x] Tidak
> **Jika ya, di mana?** Rantai operasionalisasi sudah solid dan bebas lompatan logis. Konsep abstrak "tingkat usabilitas" telah diterjemahkan secara langsung menggunakan instrumen SUS yang memang secara akademis teruji memiliki validitas konstruk (*construct validity*) untuk hal tersebut.

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| **Representative** | 5 | Sepuluh pertanyaan SUS secara komprehensif mewakili efektivitas, efisiensi, dan kepuasan pengguna. |
| **Sensitive** | 4 | Skala rentang 0 hingga 100 cukup peka untuk menangkap variasi kepuasan mahasiswa secara mendetail. |
| **Feasible** | 5 | Sangat praktis, tidak berbayar, dan data bisa dikumpulkan dengan cepat melalui platform kuesioner *online* seperti Google Form. |

**Apakah perlu secondary metric?** [x] Ya / [ ] Tidak
> **Jika ya, apa dan mengapa?** Ya, disarankan untuk menambahkan umpan balik kualitatif berupa pertanyaan terbuka (*open-ended question*) di akhir kuesioner. SUS hanya memberikan data angka (seberapa parah usabilitasnya), sedangkan komentar kualitatif akan memberikan konteks (*mengapa* skornya rendah dan fitur mana persisnya yang bermasalah).

**Contoh kasus ceiling effect untuk metrik ini:**
> *Ceiling effect* (skor mentok di angka maksimal) akan terjadi jika kuesioner hanya disebarkan secara eksklusif kepada staf admin/Biro Akademik yang setiap hari memproses KHS. Karena mereka adalah *expert users*, mereka tidak akan mengalami kebingungan navigasi dan cenderung memberi nilai SUS sempurna (mendekati 100), sehingga alat ukur gagal mendeteksi masalah UI/UX dari kacamata mahasiswa awam.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| **Completeness** | *Apakah semua data point terkumpul?* | Terdapat risiko kuesioner di-*submit* dalam keadaan tidak lengkap (ada pertanyaan SUS yang terlewat). | Mengaktifkan pengaturan *Required* (Wajib Diisi) pada setiap butir soal di *Google Form*. |
| **Consistency** | *Apakah ada kontradiksi internal?* | Responden mungkin malas membaca dan memberikan jawaban "5" semua (*straight-lining*), padahal SUS memiliki soal positif dan negatif. | Melakukan *data cleaning*. Jawaban responden yang membentuk pola lurus tanpa variasi akan dihapus karena tidak valid/kontradiktif. |
| **Validity** | *Apakah benar-benar mengukur yang dimaksud?* | Responden mungkin memberi skor rendah karena jaringan *WiFi* kampus yang sedang lambat, bukan karena antarmuka KHS-nya. | Menyisipkan paragraf *briefing* di awal kuesioner yang menegaskan bahwa evaluasi ini khusus menilai desain tata letak UI, bukan menilai kecepatan internet/server. |
| **Representativeness** | *Apakah sampel mewakili populasi target?* | Kuesioner berisiko hanya disebarkan ke teman satu kelas atau satu program studi saja. | Melakukan penyebaran acak berstrata (*stratified random sampling*) ke grup-grup Unit Kegiatan Mahasiswa (UKM) atau lintas fakultas. |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih atau mengganti metrik utama setelah melihat arah data (dikenal dengan *p-hacking* atau HARKing) adalah pelanggaran integritas riset. Peneliti secara tidak etis memanipulasi alat ukur agar seolah-olah eksperimennya menghasilkan angka yang "signifikan" atau sukses, sehingga melanggar prinsip *falsifiability* (kemampuan hipotesis untuk dibuktikan salah). 
> 
> Perbedaannya dengan eksplorasi data (*Exploratory Data Analysis*) terletak pada elemen prapendaftaran (*pre-registration*) dan transparansi. Dalam eksplorasi yang sah, metrik utama (seperti SUS) sudah dikunci dan didokumentasikan di awal. Jika saat menganalisis data peneliti menemukan korelasi unik lain secara tidak sengaja (misalnya: "Mahasiswa angkatan 2023 memberi skor jauh lebih rendah dibanding angkatan 2022"), temuan tersebut dilaporkan secara jujur sebagai "Temuan Tambahan/Eksploratif", bukan diklaim sebagai tujuan utama pembuktian riset sejak awal.