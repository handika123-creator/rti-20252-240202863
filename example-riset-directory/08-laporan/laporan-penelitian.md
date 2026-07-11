# Laporan Penelitian Akhir

**Judul:** Evaluasi Pengalaman Pengguna pada Fitur Kartu Hasil Studi (KHS) SIM Universitas Putra Bangsa Menggunakan System Usability Scale (SUS)

**Peneliti:** [Nama Peneliti / Mahasiswa]
**Target:** Laporan Akhir Tugas/Riset Evaluasi Usabilitas
**Status Penelitian:** Tahap 1–5 selesai seluruhnya. Draf manuskrip lengkap tersedia di `07-manuskrip/`.

---

## 1. Ringkasan Eksekutif

Penelitian ini mengevaluasi secara empiris tingkat kegunaan (*usability*) dari antarmuka fitur Kartu Hasil Studi (KHS) pada Sistem Informasi Manajemen (SIM) Universitas Putra Bangsa. Pengukuran dilakukan dengan menyebarkan kuesioner baku *System Usability Scale* (SUS) 10-item kepada 30 mahasiswa aktif sebagai sampel pengguna akhir. Data yang dikumpulkan diolah secara otomatis menggunakan skrip program Python (`pandas`, `scipy`) guna menjalankan kalkulasi *reverse coding* skala Likert dan uji hipotesis statistik komparatif.

**Temuan utama:**
- Skor komposit rata-rata SUS yang diperoleh dari populasi sampel adalah **63.33** (SD = 11.75).
- Uji hipotesis statistik (*One-Sample T-Test*) membuktikan bahwa rata-rata skor SUS pengguna **signifikan berada di bawah** ambang batas kelayakan global 68.0 dengan p-value sebesar 0.9810 (p > 0.05). H1 ditolak.
- Secara kualitatif, keluhan paling mendominasi adalah struktur tata letak antarmuka tabel KHS yang **tidak responsif di perangkat mobile**, sehingga mahasiswa dipaksa melakukan *pinch-and-zoom* hanya untuk melihat rentetan nilai mereka.

Penelitian ini merekomendasikan dilakukannya *redesign* antarmuka sistem secara cepat dengan memprioritaskan penyusunan tata letak *mobile-first design*.

---

## 2. Latar Belakang dan Rumusan Masalah

### 2.1 Latar Belakang
Portal Sistem Informasi Manajemen (SIM) adalah platform wajib harian bagi civitas academica UPB, khususnya ketika mengakses nilai melalui fitur Kartu Hasil Studi (KHS) di setiap akhir masa perkuliahan. Tingginya frekuensi akses tersebut ironisnya sejalan dengan masifnya keluhan mahasiswa mengenai antarmuka yang membingungkan dan kaku di gawai mereka. Sayangnya, akibat tiadanya pendataan terukur yang empiris (*empiric gap*), manajemen akademik tidak memiliki dasar objektivitas untuk menyegerakan tindakan perbaikan teknis.

### 2.2 Rumusan Masalah
Bagaimana tingkat *usability* serta kenyamanan interaksi pengguna pada fitur KHS SIM UPB jika dievaluasi secara objektif menggunakan instrumen pengukur standar *System Usability Scale* (SUS)? Serta, apakah capaian skor tersebut telah berhasil memenuhi batas minimal kelayakan (*acceptable score* = 68)?

### 2.3 Tujuan Penelitian
Membuktikan secara kuantitatif tingkat kelayakan *usability* antarmuka KHS SIM eksisting, memetakan isu-isu interaksi spesifik, serta menyediakan landasan rekomendasi perbaikan berbasis data bagi tim pengembang kampus.

---

## 3. Metodologi dan Pelaksanaan

Penelitian dieksekusi secara struktural dalam lima tahapan alur.

### 3.1 Tahap 1 — Perancangan Eksperimen
Membangun alur interaksi tugas wajib (*task scenario*) di mana responden dipandu untuk *login*, menjelajah, membuka menu KHS, hingga selesai melihat IPK. Tahap ini juga merancang formula dan konversi SUS yang dituang ke dalam diagram alur konseptual. (Dokumen: `03-teori/`)

### 3.2 Tahap 2 — Pengumpulan Data
Kuesioner elektronik SUS dibagikan ke responden. Survei ditutup setelah mendapatkan 30 sampel partisipan valid tanpa terindikasi asal menjawab (*straight-lining*). Semua respons ini ditarik secara mentah dalam *file* `.csv`. (Dokumen: `04-data/`)

### 3.3 Tahap 3 — Pembuatan Skrip Kalkulator Otomatis
Sebuah skrip analisis berbasis bahasa pemrograman Python (`sus_calculator.py`) diciptakan di `05-kode/`. Skrip ini mengotomatisasi baca-tulis *dataset*, *data cleaning*, penghitungan balik skor ganjil/genap (0-4), serta pengali akhir formula untuk memperoleh indeks 0-100 per individu. Skrip ini disisipkan fungsi komputasi *One-Sample T-Test* membandingkan total *mean* dengan *baseline* teori 68.

### 3.4 Tahap 4 — Eksekusi dan Output Visualisasi
Skrip dijalankan terhadap *file* mentah. *Output* sukses dicetak di layar konsol beserta lahirnya *file* lembar data matang (`Data_KHS_Processed.csv`) berisikan matriks skor konversi yang bersih untuk dilampirkan sebagai arsip penelitian. (Dokumen: `06-output/`)

### 3.5 Tahap 5 — Draf Naskah Ilmiah
Melahirkan karya tulis berformat IMRAD (*Introduction, Method, Result, Discussion*) yang diramu dari seluruh temuan tahap 1-4 untuk disiapkan bagi publikasi jurnal akademis nasional. (Dokumen: `07-manuskrip/`)

---

## 4. Hasil Penelitian

### 4.1 Statistik Deskriptif Skor SUS
Distribusi final dari 30 *user* menunjukkan angka sebagai berikut:
- **Nilai Minimum:** 40.0
- **Nilai Maksimum:** 90.0
- **Nilai Median:** 66.25
- **Rata-rata (Mean): 63.33**
- **Standar Deviasi (SD):** 11.75

### 4.2 Uji Hipotesis T-Test
- **Hipotesis (H1):** Rata-rata skor populasi SUS > 68 (Sistem layak).
- **Nilai T-Statistic:** -2.175
- **Probabilitas (1-tailed p-value):** 0.9810
- **Keputusan Analitik:** Berhubung probabilitas 0.981 > alpha 0.05, maka **H1 Ditolak**. Rata-rata sampel terbukti secara riil berada di bawah batas standar kelayakan *usability*.

### 4.3 Temuan Kualitatif
Eksplorasi isian ulasan kualitatif memperjelas sumber kejatuhan skor. Sebagian besar umpan balik menyinggung betapa rapuhnya ketanggapan antarmuka tabel KHS tatkala dimuat pada peramban gawai (HP). Pemaksaan adaptasi pencubitan layar (*pinch-and-pan*) untuk sekadar membaca rekapitulasi nilai berkontribusi besar merusak kenyamanan instingtif navigasi dan melahirkan sensasi kompleksitas semu.

---

## 5. Kendala dan Catatan Evaluasi

- **Limitasi Sampel Kuantitatif:** Survei berbasis N=30 secara hukum limit pusat cukup memadai untuk membuktikan *One-Sample T-Test*, namun skalanya terbilang terlampau mini untuk menyajikan cermin representatif dari preferensi mahasiswa di beragam fakultas dengan keragaman disiplin ilmunya.
- **Transisi ke Otomatisasi Python:** Mengubah total landasan pengolah data dari cara klik tradisional UI (SPSS/Excel) menuju eksekusi *scripted program* telah secara drastis mempercepat kalkulasi. Meski membutuhkan penyesuaian awal merakit *library*, *reproducibility* riset saat ini sangat terjamin, nol-kesalahan manusia (0 *human-error*).

---

## 6. Kesimpulan dan Rekomendasi

Sistem antarmuka fitur KHS pada SIM Universitas Putra Bangsa **terbukti secara empiris masih belum layak dan tertinggal di bawah target ideal**. Kategori skor final (63.33) mencerminkan status *Marginal Passive* — aplikasi tidak dibenci secara fatal namun tidak cukup nyaman untuk terus dipakai dengan sukarela. 

Rekomendasi teknis bagi pemegang otoritas IT di UPB ditekankan pada percepatan inisiasi pembaruan desain *front-end* tabel akademik, utamanya penguatan dukungan responsivitas antar-perangkat (*mobile-first principle*).

---

## 7. Lampiran — Peta Artefak Penelitian

| Folder / Repositori | Berisi | Status |
|---|---|---|
| [`01-proposal/`](../01-proposal/) | Proposal rencana penelitian | Selesai |
| [`02-literatur/`](../02-literatur/) | Matriks literatur riset sejenis | Selesai |
| [`03-teori/`](../03-teori/) | Diagram skenario interaksi pengguna | Selesai |
| [`04-data/`](../04-data/) | Data responden mentah (*raw survey*) | Selesai |
| [`05-kode/`](../05-kode/) | *Source code* otomatisasi komputasi | Selesai |
| [`06-output/`](../06-output/) | Rekapan data hasil hitung komputasi | Selesai |
| [`07-manuskrip/`](../07-manuskrip/) | Draf final manuskrip (*scientific paper*) | Selesai |
| [`08-laporan/`](../08-laporan/) | Eksekutif laporan riset (*dokumen ini*) | Selesai |

**Cara mereproduksi uji kalkulator statistik:**

```bash
# Instalasi library prasyarat
pip install pandas scipy

# Eksekusi skrip komputasi otomatis
cd 05-kode/
python sus_calculator.py
```
