# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

> Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---|---|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---|---|---|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|---|---|---|---|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |

*Kunci:* Parameter normalisasi (dalam ML) dihitung dari training set. Dalam riset survei (seperti SUS), normalisasi tidak digunakan; yang ada adalah **Transformasi** berdasarkan formula baku instrumen.

### Data Leakage Prevention (Konteks Riset Survei)

Data leakage dalam survei terjadi ketika peneliti memanipulasi data mentah agar skor akhirnya sesuai dengan hipotesis yang diharapkan:
- Membuang responden dengan skor rendah dengan alasan "outlier" tanpa justifikasi ← **SALAH**
- Mengubah jawaban Likert responden agar *mean* naik ← **SALAH**

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → salah rumus SUS bisa ubah kesimpulan total.
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → membuang opini tidak populer (outlier) mendistorsi realitas UX.
3. "Normalisasi selalu diperlukan" → tidak perlu untuk data survei parametrik deskriptif.
4. "Imputation sama untuk semua situasi" → dalam kuesioner berskala, lebih baik menolak *missing data* dari awal.

---

## Template A.13 — Preprocessing Documentation Log

**PREPROCESSING LOG**

- **Dataset :** `Data_KHS_Raw.xlsx`
- **Jumlah data awal :** 30 responden

**Cleaning:**

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---|---|---|---|
| Missing | 0 | Tidak ada (Listwise jika ada) | Fitur *Required* diaktifkan di Google Form |
| Duplikat| 0 | Pengecekan Timestamp & Nama | Tidak ada pengisian ganda di waktu berdekatan |
| Error | 0 | Filter tipe data | Input otomatis terbatasi skala linear 1-5 |

**Transformation:**

| Transformasi | Variabel | Detail | Alasan |
|---|---|---|---|
| Kalkulasi SUS | Q1 - Q10 | (Skor Ganjil - 1) + (5 - Skor Genap) x 2.5 | Aturan baku kalkulasi System Usability Scale (SUS) untuk mengonversi Likert (1-5) menjadi rentang persentil (0-100) |

**Normalization:**
- **Metode :** Tidak Menggunakan Normalisasi ML (Z-Score/Min-Max)
- **Alasan :** Analisis menggunakan uji statistik deskriptif pada data instrumen standar (SUS). Rentang 0-100 dari transformasi SUS sudah mutlak dan tidak boleh diskalakan ulang agar kompatibel dengan *benchmark* global.
- **Parameter :** Seluruh data (Populasi sampel N=30)

**Leakage Check:**
  [x] Konversi dilakukan menggunakan *script* / rumus absolut, tanpa intervensi manual
  [x] Tidak ada penghapusan baris data (outlier) untuk mendongkrak nilai rata-rata
  [x] Data mentah (Likert) dipertahankan sebagai *backup*

- **Jumlah data akhir :** 30 records siap analisis
- **Script tersedia :** [x] Ya → path: `sus_calculator.py` | [ ] Belum

---

## Latihan 1 — Cleaning Plan

Periksa dataset Anda (atau dataset contoh) dan dokumentasikan masalah yang ditemukan.

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---|---|---|---|
| Missing di kolom Q1-Q10 | 0 dari 300 data points | Pencegahan (Preventive) | Menggunakan limitasi "Wajib Diisi" pada instrumen survei |
| Straight-lining | 0 dari 30 responden | Verifikasi Standar Deviasi | Seluruh responden memiliki variansi jawaban (std > 0) |

- **Jumlah data sebelum cleaning:** 30 baris
- **Jumlah data setelah cleaning:** 30 baris
- **Persentase data yang hilang/berubah:** 0%

---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|---|---|---|---|---|---|
| Q1 - Q10 | 1 - 5 | Normal | Tidak | **Transformasi Linier (SUS)** | Mengubah skala sikap menjadi skor probabilitas UX baku. |
| Skor Akhir SUS | 40.0 - 90.0 | Normal | Tidak | **Tidak Diperlukan** | Data sudah berada dalam rentang [0,100] dan siap dibandingkan dengan rentang target kelayakan (68.0). |

**Apakah normalisasi (ML-style) diperlukan?** [ ] Ya / [x] Tidak
**Justifikasi:**
Metode *Robust Scaling* atau *Z-score* digunakan untuk menyeimbangkan bobot *features* dalam pemodelan prediktif. Pada evaluasi *usability*, data merupakan nilai tunggal deskriptif yang nilainya sudah dibatasi (0-100), sehingga normalisasi justru akan merusak interpretasi standar SUS.

**Leakage check:**
- [x] Transformasi dilakukan serentak pada seluruh dataset tanpa memilah hasil.
- [x] Hasil konversi (Mean 63.33) diterima apa adanya tanpa manipulasi batas rentang.

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

**PREPROCESSING SUMMARY**

1. **Dataset:** `Data_KHS_Raw.xlsx`
2. **Data awal:** 30 records, 10 features (Q1-Q10 Likert)
3. **Cleaning:**
   - Missing values: 0 kasus, metode: Pencegahan via UI Form
   - Duplikat: 0 kasus, tindakan: Verifikasi manual
   - Error/Straight-lining: 0 kasus, tindakan: Cek deviasi standar tiap baris
4. **Transformation:** Menerapkan rumus baku SUS untuk menghitung total bobot pertanyaan positif dan negatif (rentang dikali 2.5).
5. **Normalisasi:** Tidak dilakukan (Tidak relevan untuk analisis inferensial SUS).
6. **Data akhir:** 30 records, 1 feature utama (Skor_Akhir_SUS)
7. **Leakage check:** [x] Lulus / [ ] Ada masalah

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

**Pengalaman sebelumnya:**
Dalam tugas mata kuliah analisis data sebelumnya, saya cenderung mengaplikasikan *Min-Max Scaler* pada semua *dataset* secara membabi buta karena menganggap itu adalah "prosedur wajib" agar data terlihat rapi.

**Yang akan dilakukan berbeda:**
Saya sekarang menyadari bahwa *preprocessing* harus disesuaikan dengan jenis analisisnya. *Over-preprocessing* pada data kuesioner berskala (seperti membuang responden yang memberi nilai ekstrem rendah) akan mendistorsi realitas. Pada evaluasi antarmuka, sentimen pengguna yang ekstrem negatif (nilai 1) bukanlah "outlier sampah", melainkan "sinyal kritis" (UX problem) yang justru merupakan temuan utama penelitian. Membuangnya sama dengan menyembunyikan fakta.