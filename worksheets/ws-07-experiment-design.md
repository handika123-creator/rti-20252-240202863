# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question : Apakah perancangan prototype antarmuka mobile menggunakan pendekatan Design Thinking menghasilkan skor System Usability Scale (SUS) dan waktu penyelesaian tugas yang secara signifikan lebih baik dibandingkan antarmuka website My CIC eksisting berdasarkan pengujian terhadap mahasiswa?
Hypothesis        : H₁: Terdapat peningkatan skor SUS yang signifikan dan penurunan Time on Task pada prototype aplikasi mobile dibandingkan dengan website eksisting.
Tipe Eksperimen   : [x] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Mahasiswa menguji coba website sistem akademik lama (Sistem Eksisting) | Antarmuka Website | Skenario tugas A, B, dan C; dilakukan dalam lingkungan ber-WiFi; profil responden lintas jurusan. |
| Treatment | Mahasiswa menguji coba purwarupa (prototype) aplikasi baru (Sistem Usulan) | Antarmuka Aplikasi Mobile | Skenario tugas A, B, dan C; dilakukan dalam lingkungan ber-WiFi; profil responden lintas jurusan. |

Fairness Checklist:
  [x] Dataset identik untuk semua kondisi
  [x] Preprocessing setara
  [x] Tuning effort setara
  [x] Environment identik
  [x] Metrik evaluasi sama

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    | Learning/Order Effect: Responden yang menguji Website dulu lalu ke Mobile mungkin menjadi lebih cepat di Mobile karena sudah hafal tata letak/alur tugasnya. | Counterbalancing: Membagi responden menjadi dua kelompok. 50% responden menguji Web dulu lalu Mobile, 50% lagi menguji Mobile dulu baru Web. |
| External    | Selection Bias: Pengujian hanya dilakukan pada mahasiswa Fakultas IT yang secara bawaan lebih mahir beradaptasi dengan UI baru. | Stratified Random Sampling: Merekrut responden yang proporsional dari fakultas non-IT (seperti Ekonomi atau Komunikasi). |
| Construct   | Misinterpretation of Metric: Responden memberi nilai SUS rendah karena loading halaman lama (faktor server/sinyal), bukan karena UI/UX-nya buruk. | Clear Briefing: Memberikan peringatan tertulis bahwa kuesioner murni menilai "tata letak, navigasi, dan kemudahan fitur", bukan koneksi. |
| Conclusion  | Low Statistical Power: Jumlah sampel terlalu sedikit (misal < 10) sehingga uji komparasi gagal mendeteksi signifikansi statistik. | Adequate Sample Size: Menetapkan batas minimal 30 responden (sejalan dengan standar validitas riset Winandy et al., 2024). |

Statistical Plan:
  Uji statistik   : Paired Sample T-Test (jika data berdistribusi normal) atau Wilcoxon Signed-Rank Test (jika data tidak normal). 
  Justifikasi      : Menguji signifikansi perbedaan nilai rata-rata dari dua kondisi (Web vs Mobile) yang berasal dari satu kelompok responden yang sama (Within-Subjects Design).
  Alpha            : 0.05 (Tingkat kepercayaan 95%)
  Effect size min  : Cohen's d > 0.5 (Mencari efek perbaikan skala menengah/signifikan dari segi kepuasan pengguna).
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Apakah perancangan prototype antarmuka mobile menghasilkan skor SUS yang secara signifikan lebih tinggi dibandingkan antarmuka website My CIC eksisting?
**Tipe eksperimen:** [x] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Baseline menggunakan website My CIC eksisting. | Web-based UI | Lembar instruksi Task identik (Cek KRS, Nilai, Jadwal). Waktu timeout 3 menit per task. |
| Treatment | Purwarupa aplikasi yang dibangun berdasarkan Design Thinking. | Mobile App UI | Lembar instruksi Task identik (Cek KRS, Nilai, Jadwal). Waktu timeout 3 menit per task. |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✅ Memenuhi | Semua mahasiswa partisipan masuk dalam kriteria inklusi yang sama (aktif kuliah, pengguna SIAKAD). |
| Preprocessing setara | ✅ Memenuhi | Pendampingan sebelum tes (penjelasan goal) durasi dan materinya sama untuk kedua platform. |
| Tuning effort setara | ✅ Memenuhi | Peneliti sama sekali tidak boleh memberi hint atau bantuan klik saat responden merasa stuck di kedua tes. |
| Environment identik | ✅ Memenuhi | Diuji secara luring (in-person) menggunakan perangkat standar dan jaringan yang diawasi langsung oleh peneliti. |
| Metrik evaluasi sama | ✅ Memenuhi | Alat pencatat menggunakan lembar kuesioner SUS dari format instrumen asli (Brooke, 1996). |

**Ada yang tidak fair?** [ ] Ya / [x] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | *Data Leakage/Carryover Effect (Mengingat alur dari tes pertama). | Diterapkan Counterbalancing AB/BA (diacak siapa yang mulai dengan Mobile atau Web). |
| External | Bias demografi (responden terlalu tech-savvy). | Kriteria eksklusi (tidak merekrut mahasiswa yang jago coding/UI-UX design). |
| Construct | Pertanyaan SUS nomor genap yang kalimatnya negatif sering salah dipahami. | Diterjemahkan ke Bahasa Indonesia yang sudah tervalidasi atau ditekankan agar baca pelan-pelan. |
| Conclusion | Asumsi normalitas data untuk uji parametrik T-Test tidak terpenuhi. | Jika gagal uji normalitas Shapiro-Wilk, bergeser ke uji non-parametrik (Wilcoxon). |

**Ancaman mana yang paling sulit dimitigasi?** Internal Validity (Carryover Effect)
**Mengapa?**
> Karena dalam uji usabilitas, pengguna yang sudah berhasil mencari letak menu KRS di versi Website kemungkinan besar secara psikologis sudah tahu "kata kunci" apa yang harus dicari (misalnya masuk ke sub-menu 'Akademik'). Otak mereka tidak lagi bekerja dari nol saat menguji versi Mobile. Walaupun urutannya sudah diacak (counterbalancing), sisa-sisa memori eksperimen tetap membayangi kemurnian beban kognitif di tes kedua.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apakah Baseline yang dipilih valid dan mutakhir? (Atau hanya straw man/sistem lama yang sengaja dipilih karena mudah dikalahkan, alih-alih mengalahkan sistem SOTA).
2. Apakah kondisinya benar-benar identik (Fairness)? (Jangan-jangan sistem usulan dites dengan hardware lebih bagus, instruksi lebih mudah, atau dataset yang berbeda dari baseline).
3. Apakah signifikansinya diuji secara statistik? (Apakah selisih poin kemenangannya terbukti konsisten lewat p-value atau sekadar beda tipis karena faktor kebetulan (variansi acak)?).