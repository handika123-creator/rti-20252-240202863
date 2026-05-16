# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

  Contoh config YAML dengan feature toggles:
  ```yaml
  model:
    type: cnn          # IV: ganti "rf" untuk kondisi baseline
  features:
    use_temporal: true  # toggle komponen temporal
    use_normalization: true  # toggle preprocessing
  experiment:
    seed: 42
    runs: 5
  ```
  Dengan pendekatan ini, berbeda kondisi eksperimen = berbeda satu baris config, **tanpa mengubah kode**.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question: Apakah perancangan prototype antarmuka mobile menggunakan pendekatan Design Thinking menghasilkan skor System Usability Scale (SUS) dan waktu penyelesaian tugas (Time on Task) yang secara signifikan lebih baik dibandingkan antarmuka website My CIC eksisting berdasarkan pengujian terhadap mahasiswa?

Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
| Jenis Antarmuka | IV   | URL Link Lingkungan Uji | Swap / mengganti link pengujian antara tautan Website kampus eksisting dengan tautan Prototype Figma Mobile. |
| Tingkat Usabilitas & Efisiensi | DV   | Google Form & Pengukur Waktu | Google Form mengukur skor komposit SUS (10 pertanyaan); Stopwatch / platform Maze mengukur durasi penyelesaian tugas (detik). |
| Skenario Tugas & Responden | CV   | Dokumen Task Scenario | Skenario tugas (misal: "Cek nilai semester") dibakukan dalam teks instruksi tertulis yang sama persis untuk semua tester mahasiswa. |

4 Prinsip Desain:
  [x] Traceability — Setiap komponen bisa ditelusuri ke variabel
  [x] Variable Isolation — IV bisa diubah tanpa mengubah CV
  [x] Measurement Integration — Pengukuran DV built-in
  [x] Reproducibility — Setup bisa direkonstruksi

Experimental Setup:
  Input data     : Interaksi klik/tap dari responden saat mengeksekusi skenario tugas (mencari KRS, melihat jadwal) pada antarmuka yang diberikan.
  Parameter      : 10 butir pertanyaan terstandar SUS (skala 1-5); batas waktu maksimal per tugas (misal: timeout 3 menit); kriteria mahasiswa lintas jurusan.
  Output format  : Spreadsheet tabulasi berisi skor mentah Likert per responden, konversi skor SUS akhir (0-100), dan durasi pencapaian tugas (Time on Task).
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Apakah perancangan prototype antarmuka mobile menggunakan pendekatan Design Thinking menghasilkan skor System Usability Scale (SUS) yang secara signifikan lebih tinggi dibandingkan antarmuka website My CIC eksisting?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| Tipe Antarmuka | IV | Platform (Website ↔ Prototype Mobile) | Mengganti URL / device pengujian untuk subjek eksperimen |
| Tingkat Usabilitas | DV | Google Form Kuesioner SUS | Tabulasi otomatis skor Likert 1-5 menjadi skor SUS (0-100) |
| Skenario Pengujian | CV | Dokumen Instruksi Skenario (Task Prompt) | Instuksi dibagikan secara seragam; tidak boleh ada improvisasi panduan saat tes |

**Apakah semua variabel bisa di-map?** [x] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? _________

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | ✅ | Alat pengukur Google Form terhubung langsung dan eksklusif untuk melayani variabel Usability (DV). |
| Modularity | ✅ | Desain mobile (Figma) diuji secara terpisah dari website tanpa perlu membongkar kode/sistem database asli milik kampus. |
| Controllability | ✅ | Tugas/beban kognitif dieksternalisasi menjadi "Dokumen Skenario" yang dikunci ketat (CV) agar adil untuk kedua antarmuka. |
| Measurability | ✅ | Skor SUS dihitung dengan formula matematika yang pasti, dan waktu (Time on Task) menghasilkan angka rasio mutlak. |

**Prinsip mana yang paling sulit dipenuhi?** Controllability (Keterkontrolan Lingkungan)
**Strategi untuk mengatasinya:**
> Jika pengujian dilakukan secara jarak jauh (remote testing), sangat sulit mengontrol distraksi lingkungan responden atau perbedaan kecepatan internet mereka yang bisa memengaruhi metrik Time on Task. Strategi mitigasinya adalah melakukan pengujian secara Moderated In-Person (didampingi langsung dalam satu ruangan dengan koneksi Wi-Fi yang seragam), atau menggunakan tools seperti Maze Design (seperti pada studi Winandy et al., 2024) yang bisa membatasi sesi jika terdeteksi koneksi tidak stabil.

---

## Latihan 3 — Ablation Study Planning

Sistem prototype mobile memiliki 3 fitur komponen utama untuk dievaluasi.

> **Panduan jumlah kondisi:** Untuk 3 komponen (A, B, C), kondisi minimal yang direkomendasikan:
> Full + (-A) + (-B) + (-C) = **4 kondisi dasar**. Jika waktu memungkinkan, tambahkan kombinasi ganda: (-A,-B), (-A,-C), (-B,-C) = **7 kondisi**. Sesuaikan dengan *computational cost* dan tenggat waktu penelitian.

| Kondisi | Komponen A (Search Bar Cepat) | Komponen B (Reminder Notifikasi) | Komponen C (Dashboard Card-Based) | Hasil yang Diharapkan |
|---------|-----------|-----------|-----------|----------------------|
| Full | ✅ Ada Search Bar | ✅ Ada Reminder | ✅ Desain Card-Based | Baseline penuh: Waktu penyelesaian tercepat dan SUS tertinggi. |
| – A | ❌ (Tanpa Search Bar) | ✅ | ✅ | Responden butuh waktu navigasi lebih lama untuk mencari menu spesifik (KRS/Jadwal) lewat hamburger menu. |
| – B | ✅ | ❌ (Tanpa Reminder) | ✅ | Responden mungkin kebingungan melihat status tenggat waktu akademik, butuh klik ekstra ke menu profil. |
| – C | ✅ | ✅ | ❌ (Ganti List teks biasa) | Nilai dimensi "Satisfaction" pada SUS berpotensi turun karena antarmuka terasa kaku dan kurang modern. |

**Komponen mana yang diprediksi paling berkontribusi?** Komponen A (Search Bar Cepat)
**Mengapa?**
> Sistem informasi akademik sangat sarat akan data. Mahasiswa biasanya membuka aplikasi dengan satu tujuan spesifik (contoh: hanya ingin melihat nilai matkul tertentu). Keberadaan Search Bar memotong seluruh hierarki navigasi (clicks), sehingga memanipulasi fitur ini secara langsung akan memberikan dampak paling drastis pada peningkatan metrik Time on Task (efisiensi).

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Jika sistem dibangun langsung jadi dengan fitur lengkap (monolitik) lalu diuji dan hasilnya "bagus", peneliti akan terjebak dalam masalah Credit Assignment Problem. Peneliti tidak akan bisa membuktikan secara spesifik fitur mana yang membuat sistem itu bagus. Apakah karena warnanya? Apakah karena navigasinya? Atau karena performanya?
> Arsitektur modular dalam riset DSR (Design Science Research) sangat penting karena memungkinkan peneliti melakukan Variable Isolation. Dengan modularitas, kita bisa menghidupkan atau mematikan satu fitur tertentu (seperti pada Ablation Study) sambil menahan fitur lainnya tetap konstan. Hal ini memungkinkan kita menarik kesimpulan kausalitas sebab-akibat yang kuat dan valid secara ilmiah.