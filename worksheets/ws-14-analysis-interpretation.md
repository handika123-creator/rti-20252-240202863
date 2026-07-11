# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

> Data → Analysis → Interpretation → Explanation → Knowledge

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|---|---|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---|---|
| 1 grup vs nilai acuan/target | One-Sample t-test |
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**. Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.

### Limitation Types

| Jenis | Contoh |
|---|---|
| **Internal validity** | Confounders yang tidak dikontrol (misal: kondisi *mood* responden saat mengisi) |
| **External validity** | Generalisasi ke domain lain (misal: hasil ini khusus untuk KHS, bukan KRS) |
| **Construct validity** | Metrik mengukur apa yang dimaksud? (Kuesioner SUS sudah teruji global) |
| **Statistical limitation** | Sample size terbatas, distribusi skewness |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size.
2. "Hipotesis tidak didukung → cari sudut baru" → manipulasi p-value (p-hacking).
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight (padahal kegagalan sistem = temuan UX).
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman analisis hilang.

---

## Template A.14 — Analysis & Interpretation Report

**ANALYSIS & INTERPRETATION**

**1. Statistik Deskriptif:**

| Skenario | Mean | Std | Median | Min | Max | n |
|---|---|---|---|---|---|---|
| Fitur KHS SIM UPB | 63.33 | 11.75 | 66.25 | 40.0 | 90.0 | 30 |

**2. Uji Hipotesis:**
- **Uji yang digunakan:** One-Sample T-Test
- **Justifikasi:** Membandingkan nilai rata-rata (mean) sampel dari 1 grup (63.33) dengan konstanta nilai target / acuan kelayakan SUS (68.0). Asumsi normalitas data terpenuhi.
- **Hasil:** t = -2.17, p < 0.05 (signifikan), effect size (Cohen's d) = -0.39 (Medium)
- **CI 95%:** [59.0, 67.7]

**3. Keputusan:**
- [x] H₀ ditolak (Karena p < 0.05, rata-rata sampel terbukti secara statistik *signifikan berada di bawah* target 68.0).
- [ ] H₀ tidak ditolak

**4. Interpretasi:**
- **Hubungan ke RQ:** Menjawab rumusan masalah bahwa tingkat *usability* fitur KHS di SIM UPB saat ini masih di bawah standar kelayakan.
- **Practical significance:** Penurunan skor ini (Cohen's d = 0.39) bersifat *medium effect*, artinya kesulitan yang dialami mahasiswa saat mengakses nilai KHS benar-benar terasa secara praktis, bukan sekadar selisih angka desimal.
- **Perbandingan literatur:** Rata-rata global batas bawah kelayakan SUS adalah 68.0 (Sauro, 2011). SIM UPB (63.33) berada pada kategori *Marginal (Grade D)* yang berarti sistem bekerja namun membutuhkan perbaikan antarmuka segera.

**5. Limitation:**

| Jenis | Ancaman | Dampak | Mitigasi |
|---|---|---|---|
| Statistical | *Sample size* minimum (n=30) | Kekuatan *power test* terbatas jika dipecah per-fakultas | Data hanya dianalisis secara agregat untuk seluruh populasi, tidak dipecah sub-grup. |
| External Validity | Survei hanya dilakukan pada modul KHS | Kesimpulan tidak merepresentasikan sistem SIM UPB secara keseluruhan | Menyatakan batas lingkup *scope* secara eksplisit pada bab kesimpulan. |

**6. Failure Analysis (Jika sistem gagal mencapai target):**
- **Penyebab potensial :** Navigasi berbelit, *layout* tabel nilai kurang responsif di layar ponsel, atau minimnya *feedback* visual saat sistem memuat data KHS.
- **Boundary condition :** Nilai buruk ini khusus terjadi pada *touchpoint* pencarian nilai akhir semester.
- **Insight :** "Kegagalan" sistem ini membuktikan bahwa opini subjektif keluhan mahasiswa adalah fakta berbasis data (empiris). Hal ini memberikan pijakan yang kuat untuk rekomendasi *redesign* UI/UX KHS di masa depan.

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan | Jawaban |
|---|---|
| Berapa grup yang dibandingkan? | 1 Grup (Sampel) dibandingkan dengan 1 Nilai Konstanta (Target 68.0) |
| Apakah data berpasangan (paired)? | Tidak |
| Apakah distribusi normal? | Ya, distribusi skor SUS [0-100] dari 30 responden menyebar normal. |
| **Uji yang dipilih:** | **One-Sample T-Test** |
| **Justifikasi:** | Metode ini paling akurat untuk menguji apakah rata-rata sebuah populasi tunggal berbeda secara signifikan dari nilai spesifik (skor kelayakan global SUS). |

**Effect size yang akan dilaporkan:** [x] Cohen's d / [ ] Eta-squared / [ ] Lainnya: ____

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data:**

| Model / Sistem | Accuracy/SUS (mean ± std) | n |
|---|---|---|
| KHS SIM UPB | 63.33 ± 11.75 | 30 |

Target Kelayakan = 68.0 | p < 0.05, Cohen's d = 0.39, CI 95% = [59.0, 67.7]

| Aspek | Interpretasi |
|---|---|
| Signifikansi statistik | Nilai (p < 0.05) menunjukkan bahwa skor KHS benar-benar di bawah 68.0 dan selisihnya bukan karena kebetulan acak (random chance). |
| Effect size | Cohen's d = 0.39 menunjukkan ada efek negatif berukuran "sedang/medium". |
| Practical significance | Mahasiswa secara nyata membutuhkan bantuan atau menghabiskan waktu lebih lama dari yang semestinya saat menggunakan fitur ini. |
| Hubungan ke RQ | Menkonfirmasi bahwa antarmuka sistem saat ini bermasalah secara *usability*. |
| Perbandingan literatur | Masuk ke dalam *Acceptability Range: Marginal* dan *Adjective Rating: OK/Poor* menurut kerangka referensi penilaian SUS dari Bangor et al. (2008). |

---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

**Skenario:** Hipotesis awal menyatakan bahwa KHS SIM UPB layak (Skor > 68). Kenyataannya mendapat Skor = 63.33.

| Pertanyaan | Jawaban |
|---|---|
| Apakah ini "gagal"? | Risetnya berhasil membuktikan fakta, namun "Sistemnya" yang gagal lolos uji kelayakan. Ini adalah kontribusi temuan yang valid. |
| Kemungkinan penyebab? | Merujuk pada isian opsional kuesioner, kemungkinan ada ketidakkonsistenan desain tata letak (UI) saat diakses via *mobile device*. |
| Boundary condition? | Kurangnya *usability* ini diukur pada antarmuka *existing* versi saat ini (Juli 2026). Hasil dapat berubah bila ada pembaruan *patch* dari tim developer kampus. |
| Insight yang bisa diambil? | Diperlukan audit *Usability Heuristics* secara spesifik pada arsitektur informasi modul KHS untuk mendeteksi letak kesulitan *(pain points)* yang spesifik. |
| Apakah layak dilaporkan? Mengapa? | Sangat layak. Melaporkan nilai rendah pada sistem internal institusi adalah bentuk evaluasi kritis akademis yang dapat mendrive inovasi nyata bagi pihak universitas. |

**Limitation terkait:**

| Jenis | Ancaman | Dampak |
|---|---|---|
| *External* | Mahasiswa yang sudah terbiasa dengan UI lama mungkin bias dan memberi nilai terlalu tinggi (Toleransi). | Memperkecil deteksi *pain point* (Skor bisa saja lebih rendah dari 63.33 jika diujikan pada mahasiswa baru). |

---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?

**Pengalaman sebelumnya:**
Dulu saya menganggap bahwa jika nilai uji sistem saya berada di bawah standar, maka sistem saya jelek dan riset saya dianggap gagal. Hal ini memicu dorongan untuk memanipulasi perhitungan agar data terlihat mencapai "target kelulusan".

**Yang akan dilakukan berbeda:**
Saya sekarang memahami bahwa *failure analysis* terhadap skor rendah (63.33) justru adalah *output* utama yang dicari dalam riset *usability*. Kegagalan antarmuka untuk mencapai skor kelayakan (68.0) adalah fakta empiris yang membuktikan adanya ruang untuk perbaikan (kontribusi penelitian). Menemukan dan menganalisis mengapa sistem ini gagal memberi *user experience* yang baik jauh lebih berharga daripada memanipulasi data agar sistem terlihat sempurna.