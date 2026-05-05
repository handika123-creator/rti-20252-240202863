# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

**Perbandingan pendekatan Author-centric vs Concept-centric:**

| Aspek | Author-centric (Hindari) | Concept-centric (Gunakan) |
|-------|--------------------------|---------------------------|
| Struktur | Per penulis/paper ("Rahman et al. menyatakan...") | Per konsep/metode ("Pendekatan berbasis transformer") |
| Tujuan | Ringkasan isi paper | Perbandingan metode & identifikasi gap |
| Contoh paragraph | "Rahman (2023) pakai CNN. Lee (2022) pakai LSTM. Zhang (2021) pakai RF." | "Tiga pendekatan dominan: CNN digunakan oleh 4 paper untuk representasi fitur visual; LSTM untuk data sekuensial; RF sebagai baseline klasik." |
| Hasil akhir | Daftar paper | Peta pengetahuan + gap yang teridentifikasi |

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database utama**: IEEE Xplore, ACM DL, Scopus
   - Akses IEEE/ACM melalui jaringan kampus atau VPN institusi
   - Alternatif bebas biaya: Google Scholar, ResearchGate ([researchgate.net](https://www.researchgate.net)), arXiv ([arxiv.org](https://arxiv.org))
2. **Boolean query** yang terdokumentasi eksplisit
   - Contoh: `("anomaly detection" OR "intrusion detection") AND ("deep learning" OR "neural network") NOT ("medical imaging")`
   - Gunakan tanda kutip untuk frasa eksak; AND/OR/NOT mengontrol scope
3. **Snowballing** — dua arah:
   - **Backward snowballing**: buka daftar referensi di paper kunci → telusuri paper yang dikutip
   - **Forward snowballing**: di Google Scholar, klik "Cited by" di bawah paper kunci → temukan paper yang mengutipnya
   - Ulangi 1–2 tingkat untuk membangun cakupan komprehensif
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Evaluasi dan Perancangan Ulang UI/UX Sistem Informasi Akademik Berbasis Mobile
Database   : Google Scholar, Portal Jurnal Nasional
Query      : ("Sistem Informasi Akademik" OR "SIAKAD") AND ("UI/UX" OR "User Experience") AND ("SUS" OR "Heuristic Evaluation" OR "Mobile")
Tahun      : 2020 - 2025
Hasil awal : 45 paper → Screening → 5 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
|(Baseline) Muhyidin et al.|2020|Prototyping (Figma)|Wawancara beberapa mahasiswa|Desain prototype mobile UI akademik My CIC|Berhenti pada pembuatan artefak visual, tidak ada pengujian empiris kuantitatif pengguna akhir.|
|Firjinia et al.|2025|User Centered Design (UCD) & SUS|6 Responden (Wali, Admin, Ahli)|Desain baru mendapat skor SUS 88,5 (Grade A)|Skala pengujian sangat kecil, dominan berfokus pada pengguna lingkungan pesantren.|
|Yusupa et al.|2025|Design Thinking & Heuristic Evaluation|3 Evaluator Pakar UI/UX|Teridentifikasi pelanggaran usability pada desain|Pengujian murni dari sudut pandang pakar (expert review), tanpa keterlibatan pengguna akhir awam.|
|Dellia et al.|2025|Heuristic Evaluation & UEQ|57 Mahasiswa Aktif|Ditemukan 20 masalah UI; Metrik Stimulasi UEQ rendah (1.45)|Masih membutuhkan pengujian dengan metode lain dan variasi kelompok pengguna.|
|Winandy et al.|2024|Design Thinking & SUS|30 Responden (Mahasiswa & Staf)|Skor Maze 76; Skor SUS 74,08 (Acceptable)|Desain prototype hanya berfokus pada hak akses mahasiswa, belum menyentuh dosen/admin.|

Pola yang ditemukan:
  Metode dominan     : Perancangan menggunakan pendekatan Design Thinking atau UCD yang dievaluasi dengan System Usability Scale (SUS) atau Heuristic Evaluation.
  Dataset umum       : Mahasiswa aktif sebagai end-user utama, dikombinasikan dengan pakar UI/UX.
  Limitasi berulang  : Studi yang sekadar membuat prototype tanpa evaluasi (seperti baseline) kehilangan validitas objektivitasnya. Sementara studi yang melakukan evaluasi sering kali terhambat pada homogenitas atau jumlah sampel yang kecil.

GAP IDENTIFICATION

Gap 1: [Jenis: Method Gap]
  Deskripsi    : Terdapat kesenjangan metodologis di mana beberapa perancangan UI/UX SIAKAD (khususnya peralihan Web ke Mobile) hanya fokus pada pembuatan artefak visual tanpa validasi metrik usabilitas yang terstandar.
  Bukti        : Studi baseline oleh Muhyidin et al. (2020) merancang prototype My CIC di Figma namun tidak melakukan pengujian akhir. Sebaliknya, studi terbaru seperti Winandy et al. (2024) dan Firjinia et al. (2025) membuktikan bahwa pengujian metrik (seperti SUS) mutlak diperlukan untuk membuktikan kelayakan desain
  Signifikansi : Mengeklaim sebuah desain itu "baik" hanya dari asumsi desainer adalah straw man. Mengisi gap ini berarti membuktikan efektivitas desain My CIC secara ilmiah dan empiris.

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
|UI Web Eksisting & Prototype My CIC|Menyelesaikan masalah yang sama: kebingungan navigasi informasi akademik kampus.|Mewakili praktik riset lama yang sekadar mendesain tanpa evaluasi usability.|Muhyidin et al. (2020)|
|SIAKAD Mobile UNU Kalbar|Merupakan solusi peralihan web ke aplikasi mobile menggunakan Design Thinking dan diuji dengan SUS.|State-of-the-Art (SOTA) untuk metode perancangan dan evaluasi di bidang yang sama.|Winandy et al. (2024)|
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan database akademik.

> **Panduan pencarian:**
> - Database: IEEE Xplore, ACM DL, Google Scholar, atau ResearchGate
> - Tulis query Boolean yang digunakan: contoh `("object detection" OR "image classification") AND ("edge computing") NOT ("medical")`. Dokumentasikan query secara eksplisit.
> - Akses gratis: buka Google Scholar → cari judul paper → klik [PDF] jika tersedia, atau akses lewat campus VPN

**Topik riset:** Evaluasi dan Perancangan Ulang UI/UX Sistem Informasi Akademik Berbasis Mobile
**Query pencarian:** ("Sistem Informasi Akademik" OR "SIAKAD") AND ("UI/UX" OR "User Experience") AND ("SUS" OR "Heuristic Evaluation" OR "Mobile")
**Database:** Google Scholar, Portal Jurnal Nasional

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Muhyidin et al. (Baseline) | 2020 | Prototyping (Figma) | Wawancara subjektif | Prototype aplikasi My CIC mobile | Ketiadaan metrik pengujian usabilitas pasca-perancangan desain |
| 2 |Firjinia et al.|2025|User Centered Design & SUS|6 Responden (Wali, Ahli, Admin)|Skor SUS 88,5 (Grade A)|Skala responden sangat kecil dan spesifik pada lingkungan pesantren|
| 3 |Yusupa et al.|2025|Design Thinking & Heuristic|3 Evaluator Pakar UI/UX|Teridentifikasi pelanggaran prinsip Visibility of System Status|Pengujian bersifat expert-based, belum diuji langsung ke end-user awam|
| 4 |Dellia et al.|2025|Heuristic Evaluation & UEQ|57 Mahasiswa Aktif|20 temuan masalah UI; Skor stimulasi UEQ rendah (1.45)|Pengujian butuh diperluas melibatkan kelompok pengguna yang lebih beragam|
| 5 |Winandy et al.|2024|Design Thinking, Maze, SUS|30 Mahasiswa & Staf Akademik|Skor Maze 76; Skor SUS 74,08 (Acceptable)|Perancangan fokus pada hak akses mahasiswa, belum menyentuh UI dosen|

**Pola yang terlihat — Metode dominan:** Perancangan antarmuka menggunakan pendekatan Design Thinking atau UCD yang dilanjutkan dengan pengujian System Usability Scale (SUS) atau Heuristic Evaluation.
**Limitasi yang berulang:** Ketiadaan uji metrik kuantitatif (baseline), dan jika ada pengujian, sering kali terhambat pada bias jumlah/jenis responden (seperti hanya diuji oleh pakar atau sampel mahasiswa yang terlalu sedikit).

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [ ] Ya / [x] Tidak | - |
| Method Gap | [x] Ya / [ ] Tidak |Terdapat kekosongan dalam validasi empiris kuantitatif secara terstandar (seperti skor SUS) pasca-pembuatan artefak visual pada studi-studi terdahulu.|
| Data Gap | [x] Ya / [ ] Tidak |Evaluasi desain masih ada yang bias karena hanya dilakukan oleh kelompok pakar (Expert Review), belum sepenuhnya melibatkan end-user awam secara luas.|
| Context Gap | [x] Ya / [ ] Tidak |Fokus evaluasi pada transisi pengalaman pengguna antarmuka website eksisting ke aplikasi mobile belum dilakukan secara beriringan.|

**Gap utama yang dipilih:** Method Gap (Ketiadaan Validasi Empiris pada Artefak Desain Mobile)
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Dalam paradigma Design Science Research (DSR), membangun purwarupa saja tidak cukup; artefak tersebut harus dibuktikan kelayakannya. Mengeklaim antarmuka baru lebih "modern dan menarik" tanpa adanya instrumen evaluasi kuantitatif dari end-user membuat riset kehilangan objektivitas dan validitas. Mengisi gap ini sangat penting untuk memastikan desain mobile baru benar-benar memecahkan kebingungan navigasi secara terukur.
---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | Antarmuka Web Lama & Prototype Mobile My CIC | Memecahkan task akademik yang identik (Cek Nilai, KRS). | Mewakili praktik riset perancangan prototype yang tidak dilengkapi evaluasi pengguna (usability testing). | Bukan, mewakili masalah dan solusi awal tanpa uji empiris. | Muhyidin et al., 2020 |
| 2 | | | | | |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [x] Tidak
> Justifikasi: Sangat adil (fair). Riset ini tidak membandingkan desain mobile canggih dengan sistem lama secara tidak proporsional, melainkan membandingkan antarmuka lama dan desain tak teruji (Muhyidin et al.) dengan desain baru yang dievaluasi dengan metode State-of-the-Art yang terstandarisasi (SUS), guna mendapatkan selisih peningkatan kepuasan pengguna.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Klaim "belum ada yang meneliti ini" umumnya bersumber dari asumsi, opini, atau pencarian literatur yang acak (author-centric), sehingga rentan salah jika nyatanya topik tersebut sudah banyak dibahas. Sebaliknya, research gap yang valid dilandasi oleh pemetaan literatur yang terstruktur dan obyektif (concept-centric).
> Untuk membuktikan sebuah gap benar-benar ada, peneliti wajib menggunakan systematic search strategy dengan Boolean query di database akademik yang kredibel, lalu mengekstraksi matriks penelitian (Metode, Data, Limitasi). Jika dari tabel matriks tersebut terlihat adanya pola metode yang selalu dilewati atau limitasi yang selalu berulang dari berbagai paper (misal: ketiadaan uji SUS), barulah gap riset tersebut bisa dinyatakan valid dan kuat secara ilmiah.