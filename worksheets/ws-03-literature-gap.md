# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

**Perbandingan pendekatan Author-centric vs Concept-centric:**

| Aspek | Author-centric (Hindari) | Concept-centric (Gunakan) |
|-------|--------------------------|---------------------------|
| **Struktur** | Per penulis/paper ("Rahman et al. menyatakan...") | Per konsep/metode ("Pendekatan evaluasi berbasis SUS") |
| **Tujuan** | Ringkasan isi paper | Perbandingan metode & identifikasi gap |
| **Contoh paragraph** | "Prabowo (2021) mengevaluasi IAIN Salatiga. Winandy (2024) mengevaluasi SIAKAD Unisba." | "Metode evaluasi dominan: SUS digunakan oleh 8 dari 12 paper karena efisiensinya dalam mengukur usabilitas tanpa butuh sampel besar." |
| **Hasil akhir** | Daftar paper | Peta pengetahuan + gap yang teridentifikasi |

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Skor usabilitas sistem eksisting selalu di bawah 68 |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada evaluasi kuantitatif pasca-implementasi |
| **Data Gap** | Dataset terbatas/tidak representatif | Responden hanya berasal dari admin, bukan mahasiswa |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada pengujian spesifik untuk Sistem Informasi Manajemen di UPB |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database utama**: IEEE Xplore, ACM DL, Scopus, Google Scholar
2. **Boolean query** yang terdokumentasi eksplisit
   - Contoh: `("usability testing" OR "evaluasi antarmuka") AND ("system usability scale" OR "SUS") AND ("sistem informasi akademik" OR "SIAKAD")`
3. **Snowballing** — dua arah:
   - **Backward snowballing**: telusuri referensi di paper kunci.
   - **Forward snowballing**: cari paper terbaru yang mengutip paper kunci tersebut.
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menggunakan instrumen evaluasi yang sama (SUS)? |
| **Representatif** | Apakah mengacu pada aturan perhitungan yang diakui global? |
| **State-of-the-Art** | Apakah interpretasi skor mengacu pada pedoman terbaru (Curved Grading Scale)? |

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| **Tujuan baca literatur** | Mencari solusi desain yang sudah ada | Memahami apa yang belum terjawab/terevaluasi |
| **Cara membaca paper** | Tutorial *wireframing*, *how-to* desain | Validitas metode ukur, limitasi sistem, metrik evaluasi |
| **Baseline** | *Template UI* terpopuler | Standar ambang batas (*threshold*) dari literatur global |
| **Dokumentasi pencarian** | Tidak diperlukan | Wajib (*reproducible*) |

---

## Template A.3 — Literature Mapping & Gap Identification

**LITERATURE MAPPING**

*   **Topik:** Evaluasi Usabilitas Sistem Informasi Akademik dengan Metode SUS
*   **Database:** Google Scholar, SINTA (Jurnal Nasional Terindeks)
*   **Query:** `("usability testing" OR "usability evaluation") AND ("system usability scale" OR "SUS") AND ("sistem informasi akademik" OR "SIAKAD")`
*   **Tahun:** 2021 – 2025
*   **Hasil awal:** 45 paper → Screening → 12 paper final (5 dipilih untuk matriks di bawah)

**Literature Matrix (concept-centric):**

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| Prabowo & Suprapto | 2021 | SUS | 66 Responden (Mahasiswa) | Skor 68,5 (Acceptable) | Pengelompokan responden terlalu luas, tidak fokus per fitur spesifik. |
| Putra & Adhicandra | 2022 | SUS | 40 Responden (Dosen & Mahasiswa) | Skor 49,6 (Marginal Low) | Tidak ada *open-ended question* untuk menggali keluhan mendalam. |
| Yasin et al. | 2022 | SUS & UEQ | 385 Responden (Mahasiswa) | Skor 52 (Not Acceptable) | Survei dilakukan saat server bermasalah, mencampurkan isu *backend* dan UI/UX. |
| Ramadhani & Yusianto | 2023 | SUS | 60 Responden | Skor 71,6 (Good) | Hanya mengevaluasi *dashboard* utama, tidak masuk ke fitur transaksional (seperti KRS/KHS). |
| Winandy et al. | 2024 | SUS | 30 Responden | Skor 66,2 (Marginal High) | Sampel responden terlalu kecil dan hanya dari satu program studi. |

**Pola yang ditemukan:**
*   **Metode dominan:** Kuesioner *System Usability Scale* (SUS) sangat mendominasi pengujian antarmuka akademik karena efisien.
*   **Dataset umum:** Rata-rata responden berada di kisaran 30-70 orang dengan demografi campuran.
*   **Limitasi berulang:** Sebagian besar penelitian mengevaluasi sistem secara "gelondongan" (*general*), jarang ada yang membedah tingkat usabilitas pada satu fitur spesifik yang vital (seperti khusus KHS atau khusus KRS), sehingga rekomendasi perbaikannya kurang tajam.

---

**GAP IDENTIFICATION**

**Gap 1: Context Gap**
*   **Deskripsi:** Belum ada penelitian yang mendokumentasikan evaluasi usabilitas secara spesifik pada Sistem Informasi Manajemen (SIM) di Universitas Putra Bangsa (UPB).
*   **Bukti:** Penelusuran menggunakan kata kunci "SIM UPB" AND "SUS" di Google Scholar menghasilkan nol (*0*) hasil relevan.
*   **Signifikansi:** Tanpa adanya data lokal, pengelola akademik UPB tidak memiliki acuan objektif untuk melakukan pembaruan antarmuka.

**Gap 2: Method/Empiric Gap**
*   **Deskripsi:** Mayoritas literatur mengevaluasi SIAKAD secara keseluruhan. Terdapat kekosongan empiris (ketiadaan data kuantitatif) yang mengevaluasi secara eksklusif fitur Kartu Hasil Studi (KHS).
*   **Bukti:** Dari 12 literatur *screening* final, 100% berfokus pada "SIAKAD/Portal Akademik", namun tidak ada yang memecah usabilitas berdasarkan intensitas penggunaan fitur tunggal seperti KHS.
*   **Signifikansi:** Mahasiswa berinteraksi dengan KHS di bawah tekanan (ingin melihat kelulusan mata kuliah). Usabilitas yang buruk di fitur ini memiliki dampak psikologis yang jauh lebih besar dibanding fitur lain, sehingga butuh evaluasi terpisah yang tajam.

---

**Baseline Selection:**

| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
| SUS *Curved Grading Scale* (Skor > 68) | Metrik standar global untuk memvalidasi kelayakan usabilitas instrumen KHS | Menginterpretasikan raw skor SUS menjadi Grade (A-F) dan klasifikasi penerimaan. | Lewis & Sauro (2018) / Bangor et al. (2009) |

---

## Latihan 1 — Concept-Centric Literature Table

**Topik riset:** Evaluasi Usabilitas Sistem Informasi Akademik
**Query pencarian:** `("system usability scale" OR "SUS") AND "Sistem Informasi Akademik" AND "KHS"`
**Database:** Google Scholar

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Prabowo & Suprapto | 2021 | Kuesioner SUS | 66 Mahasiswa | Skor rata-rata 68,5 (Acceptable) | Pengujian bersifat umum, tidak fokus ke fungsionalitas menu tertentu. |
| 2 | Putra & Adhicandra | 2022 | Kuesioner SUS | 40 Mahasiswa & Dosen | Skor rata-rata 49,6 (Marginal Low) | Tidak menggali akar masalah secara kualitatif. |
| 3 | Yasin et al. | 2022 | SUS + UEQ | 385 Mahasiswa | Skor SUS 52 (Grade F) | Evaluasi terganggu oleh isu teknis server (*confounding variable*). |
| 4 | Ramadhani & Yusianto | 2023 | Kuesioner SUS | 60 Responden Acak | Skor rata-rata 71,6 (Acceptable) | Mengabaikan proses bisnis fitur KRS/KHS. |
| 5 | Winandy et al. | 2024 | Kuesioner SUS | 30 Mahasiswa | Skor 66,2 (Marginal High) | Sampel tidak merepresentasikan seluruh fakultas. |

**Pola yang terlihat — Metode dominan:** Penggunaan kuesioner kuantitatif (SUS 10-item) tanpa penambahan metode kualitatif (wawancara terbuka) yang mendalam.
**Limitasi yang berulang:** Overgeneralisasi. Peneliti mengevaluasi seluruh halaman website sekaligus, sehingga gagal menemukan spesifik *pain point* pada fitur esensial seperti pembacaan nilai/KHS.

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| **Performance Gap** | [x] Ya / [ ] Tidak | Mayoritas sistem akademik eksisting mendapat skor di perbatasan "Marginal" (Skor 50-68), menunjukkan perlunya perhatian serius pada aspek UI/UX di kampus-kampus. |
| **Method Gap** | [x] Ya / [ ] Tidak | Belum ada pendekatan evaluasi yang mengisolasi variabel dengan memfokuskan pengujian secara eksklusif hanya pada satu fitur vital (KHS). |
| **Data Gap** | [x] Ya / [ ] Tidak | Kekurangan data empiris spesifik terkait tingkat usabilitas sistem akademik di Universitas Putra Bangsa (UPB). |
| **Context Gap** | [x] Ya / [ ] Tidak | Konteks interaksi mahasiswa yang terdesak saat melihat KHS di akhir semester belum dievaluasi secara terpisah dari navigasi normal. |

**Gap utama yang dipilih:** Context Gap + Method/Empiric Gap. (Ketiadaan evaluasi terisolasi menggunakan instrumen SUS untuk spesifik fitur KHS pada konteks lingkungan Sistem Informasi Manajemen UPB).
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Gap ini penting karena fitur KHS bukan sekadar halaman informatif, melainkan "produk akhir" dari satu semester penuh perjuangan mahasiswa. Kesalahan desain atau kerumitan navigasi pada halaman ini dapat menghambat mahasiswa dalam mengurus beasiswa, perbaikan nilai, atau konsultasi DPA. Evaluasi spesifik diperlukan untuk mencegah tebak-tebakan saat pihak kampus berencana melakukan pembaruan antarmuka.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | Ambang Batas Kelayakan (Skor SUS 68) | Batas ukur apakah KHS SIM UPB layak atau tidak. | Digunakan sebagai standar de facto di industri *Usability Engineering*. | Ya, masih menjadi *gold standard* evaluasi. | Bangor, Kortum, & Miller (2009) |
| 2 | *Curved Grading Scale* (Grade A-F) | Skala untuk menginterpretasikan skor akhir menjadi huruf penilaian. | Mempermudah manajemen kampus memahami hasil angka mentah. | Ya, versi perbaikan dari penilaian sebelumnya. | Lewis & Sauro (2018) |

**Apakah pemilihan baseline ini bisa dianggap *straw man*?** [ ] Ya / [x] Tidak
> **Justifikasi:** Pemilihan *baseline* ini bukanlah *straw man* karena riset ini tidak membandingkan metode evaluasi kita dengan metode evaluasi yang lemah. Kita secara jujur menggunakan standar ambang batas global industri (skor 68 dan *Grading Scale* A-F) yang diakui secara internasional untuk menguji "kekuatan" sistem milik universitas.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Klaim "belum ada yang meneliti ini" biasanya hanya asumsi tebakan peneliti akibat kurangnya membaca literatur, dan rawan menjadi klaim palsu (*false claim*). Sebaliknya, *research gap* yang valid adalah kekosongan ilmu atau data yang dibuktikan keberadaannya setelah peneliti melakukan pemetaan literatur yang sistematis (*systematic mapping*). 
> 
> Cara membuktikannya adalah dengan mendokumentasikan kueri Boolean (*Boolean query*) yang dipakai saat pencarian, menampilkan hasil saringan jurnal (*screening*), dan menunjukkan tabel literatur yang mengonfirmasi bahwa dari sekian banyak penelitian terkait (misal: tentang SUS pada SIAKAD), memang belum ada satupun yang fokus memecahkan variabel yang sedang kita angkat (seperti evaluasi eksklusif pada fitur KHS atau pengujian khusus pada demografi kampus UPB).