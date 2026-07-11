# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

> Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|---|---|---|
| **Accuracy** | Nilai dalam range masuk akal | Skor SUS individu = 110 (di luar [0,100]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 28 dari 30 run tercatat (missing 2) |
| **Validity** | Data sesuai desain eksperimen | Responden belum pernah akses KHS ikut dihitung |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|---|---|---|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan (Straight-lining) |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|---|---|---|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger/Google Form
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, 44, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

**DATA VALIDATION CHECKLIST**

**Completeness:**
  [x] Semua skenario tercakup
  [x] Jumlah run sesuai rencana
  [x] Tidak ada file output hilang
  Missing: 0 dari 30 data points

**Format Consistency:**
  [x] Semua file format sama (CSV / .csv)
  [x] Header konsisten
  [x] Tipe data konsisten (numerik tetap numerik)

**Range & Logic:**
  [x] Nilai dalam range masuk akal (Skala Likert 1-5)
  [x] Tidak ada waktu negatif
  [x] Metrik 0–100%, tidak di luar range
  Anomali ditemukan: 0 (Tidak terdeteksi straight-lining)

**Cross-Validation:**
  [x] Run identik → hasil mendekati
  [x] Trend konsisten dengan ekspektasi teori

**Keputusan:**
  [x] Data siap analisis
  [ ] Perlu cleaning
  [ ] Perlu re-run (skenario: ____)

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|---|---|---|---|---|
| Kuesioner SUS KHS | 30 | 30 | 0 | — |

**Total expected:** 30 | **Total actual:** 30 | **Missing:** 0

**Keputusan untuk data missing:**
> Tidak ada data yang hilang. Fitur *required* (wajib isi) pada form berfungsi dengan baik sehingga 30 responden melengkapi seluruh pertanyaan (Q1-Q10). Data terkumpul 100%.

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Dataset sampel (Representasi 5 Data Teratas):**

| Run (Responden) | Skor SUS |
|---|---|
| 1 | 67.5 |
| 2 | 55.0 |
| 3 | 70.0 |
| 4 | 62.5 |
| 5 | 57.5 |

**Deteksi outlier (Dari 30 Populasi Data):**
- Q1 = 52.50 | Q3 = 71.25 | IQR = 18.75
- Batas bawah (Q1 - 1.5×IQR) = 24.38
- Batas atas (Q3 + 1.5×IQR) = 99.38
- Outlier terdeteksi: Tidak ada. Rentang nilai aktual terendah adalah 40.0 dan tertinggi 90.0, semuanya berada di dalam batas aman distribusi statistik.

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---|---|---|---|
| - | - | Tidak ditemukan data pencilan/outlier. | Seluruh 30 baris data dipertahankan untuk analisis rata-rata. |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 100% data terkumpul (30/30)
**2. Format:** [x] Konsisten / [ ] Ada inkonsistensi: —
**3. Range check (anomali):** Skor tiap butir soal berada di batas valid (1-5). Tidak ditemukan *pattern anomaly* seperti *straight-lining* (nilai standar deviasi > 0 untuk semua responden).
**4. Logic check:** [x] Parameter sesuai plan / [ ] Ada ketidaksesuaian: —

**Kesimpulan:** [x] Data siap analisis / [ ] Perlu tindakan: —

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

Data yang "benar" merujuk pada validitas teknis, misalnya Google Form sukses menyimpan jawaban berupa angka tanpa adanya *error* atau nilai *null*. Sedangkan data yang "dipercaya" berhubungan dengan kualitas substansi—apakah angka tersebut benar-benar mencerminkan opini jujur pengguna atau sekadar asal klik agar cepat selesai. 

Proses validasi formal tetap mutlak diperlukan karena sistem otomatis tidak memiliki konteks kognitif. Google Form tidak tahu jika ada responden yang menjawab angka "3" untuk ke-10 pertanyaan tanpa membacanya (*straight-lining*). Tanpa deteksi anomali ini, data sampah akan merusak perhitungan *mean* dan menuntun peneliti pada kesimpulan akhir yang salah.