# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

> Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|---|---|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot / Histogram |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|---|---|---|---|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|---|---|---|
| **Truncated axis** | Y tidak dari 0 | Memperbesar perbedaan kecil |
| **Inconsistent scale** | Dua grafik skala beda | Perbandingan menyesatkan |
| **Cherry-picked data** | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| **3D effects** | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| **Missing error bar** | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|---|---|---|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

**RESULT PRESENTATION PLAN**

- **Research Question :** Bagaimana tingkat usability antarmuka fitur KHS pada SIM UPB?
- **Metrik Utama :** Skor System Usability Scale (SUS) 0-100.

**Tabel Hasil:**

| Skenario / Sistem | Skor SUS (mean ± std) | Interpretasi Adjektif | n |
|---|---|---|---|
| Evaluasi KHS SIM UPB | 63.33 ± 11.75 | Marginal / OK | 30 |

**Visualisasi yang Direncanakan:**

| # | Jenis Grafik | Pesan Utama | Metrik |
|---|---|---|---|
| 1 | Histogram dengan Garis Target | Menunjukkan distribusi skor mayoritas responden berada di bawah standar global (68.0) | Frekuensi Skor SUS |
| 2 | Box Plot | Menunjukkan sebaran kuartil (Q1-Q3) dan ketiadaan nilai ekstrem (outlier) | Rentang Skor SUS |

**Bias Check:**
  [x] Y-axis (atau X-axis pada SUS) diset pada rentang valid (0 - 100)
  [x] Standar deviasi (std) dan variabilitas (box plot) ditampilkan
  [x] Semua data (30 responden) disertakan tanpa ada yang dibuang diam-diam
  [x] Menggunakan grafik 2D datar agar presisi membaca angka tidak terdistorsi

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).

| Sistem yang Dievaluasi | Skor SUS (Mean ± Std) | Min - Max | Target Kelayakan | n |
|---|---|---|---|---|
| Fitur KHS SIM UPB | 63.33 ± 11.75 | 40.0 - 90.0 | > 68.0 | 30 |

**Checklist tabel:**
- [x] Self-contained (judul jelas, satuan ada, N tercantum)
- [x] Mean ± std (bukan single number)
- [x] Diurutkan berdasarkan metrik utama
- [x] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik | Pesan | Data yang Digunakan |
|---|---|---|---|
| 1 | Histogram (dengan 2 garis vertikal) | Memperlihatkan bahwa posisi rata-rata (63.33) meleset di sebelah kiri batas target (68.0) | Seluruh 30 data Skor Akhir SUS |
| 2 | Box Plot Horizontal | Membuktikan integritas data: sebaran kuartil wajar dan tidak ada titik pencilan (*outlier*) di luar kumis (*whiskers*) | Distribusi (Min, Q1, Median, Q3, Max) |

---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** Metode A = 91.2%, Metode B = 90.8%. Bar chart dengan Y-axis mulai dari 90%.

| Pertanyaan | Jawaban |
|---|---|
| Apakah Y-axis menyesatkan? | Ya. Karena dimulai dari 90%, batang A akan terlihat 2x lipat lebih tinggi dari batang B, padahal selisih aslinya hanya 0.4%. Ini memanipulasi persepsi visual pembaca. |
| Apakah error bar ditampilkan? | Tidak ada informasi terkait sebaran data (std), bisa jadi kemenangan A secara statistik tidak signifikan. |
| Apakah semua kondisi ditampilkan? | Tidak diketahui, ada potensi metode lain yang performanya buruk disembunyikan (*cherry-picking*). |
| Apa solusinya? | Mulai Y-axis dari 0 (atau 50% jika sangat justifiable), tambahkan *error bar* pada puncak batang, dan cantumkan nilai N. |

**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [x] Semua bias check lulus
- [ ] Ada yang perlu diperbaiki: —

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

Tabel dan grafik memiliki fungsi kognitif yang berbeda. Grafik sangat kuat untuk menarik perhatian audiens secara instan terhadap sebuah pola (misalnya, melihat histogram yang condong ke kiri langsung memberi impresi "nilai sistem ini kurang baik"). Namun, grafik tidak bisa memberikan angka presisi yang spesifik. Di situlah tabel masuk untuk menyajikan angka baku (misal: tepat 63.33, dengan variasi 11.75) yang dapat dikutip oleh peneliti lain.

Dalam proyek desain UI/UX terdahulu, saya sering membuat *bar chart* yang Y-axis-nya saya potong (*truncated axis*) agar perbedaan hasil survei antar-desain terlihat sangat jauh dan dramatis di mata dosen/klien. Setelah mempelajari *visualization bias*, saya menyadari bahwa itu adalah praktik manipulasi data yang melanggar integritas riset kuantitatif.