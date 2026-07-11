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

---

## Template A.7 — Desain Eksperimen Lengkap

**EXPERIMENT DESIGN**

**Research Question :** Bagaimana tingkat usabilitas fitur Kartu Hasil Studi (KHS) pada SIM UPB jika diukur menggunakan metode *System Usability Scale* (SUS) dibandingkan dengan standar *acceptable score*?
**Hypothesis        :** Skor rata-rata SUS fitur KHS SIM UPB > 68 (Sistem memenuhi standar kelayakan usabilitas).
**Tipe Eksperimen   :** [x] Comparison (Komparasi terhadap Standar Referensi)  [ ] Ablation  [ ] Parameter

**Kondisi Eksperimen (Desain Komparatif Referensi):**

| Kondisi | Deskripsi | IV Value (Objek) | CV Settings (Parameter Kontrol) |
|---------|-----------|----------|-------------|
| **Control** (*Baseline*) | Ambang batas kelayakan usabilitas global menurut literatur. | Skor Konstan: 68 | Aturan *Curved Grading Scale* (A-F). |
| **Treatment** (*Tested*) | Pengujian evaluasi pada antarmuka sistem eksisting. | Fitur KHS SIM UPB | Responden mahasiswa, skenario tugas seragam, instrumen SUS 10 item. |

**Fairness Checklist:**
  [x] Dataset/Responden representatif untuk kondisi yang diuji.
  [x] Pembersihan data (*preprocessing*) setara (membuang jawaban bias/asal).
  [x] Usaha pengujian setara (tidak ada *treatment* khusus bagi kelompok responden tertentu).
  [x] Lingkungan pengujian (*environment*) diatur menggunakan instruksi tugas baku.
  [x] Metrik evaluasi sama (Skala SUS 0-100).

**Threat Analysis:**

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| **Internal** | *Acquiescence Bias* (Responden malas membaca dan menjawab setuju semua). | Menyaring data yang memiliki pola jawaban garis lurus (*straight-lining*) dan memastikan kalkulasi inversi skor berjalan benar. |
| **External** | Sampel responden hanya berasal dari satu program studi yang melek IT. | Melakukan penyebaran kuesioner dengan teknik *Stratified Random Sampling* lintas fakultas. |
| **Construct** | Form evaluasi keliru dipahami sebagai pengujian kecepatan *server* kampus. | Penegasan di instruksi awal kuesioner bahwa yang dinilai murni tata letak dan desain antarmuka. |
| **Conclusion** | Ukuran sampel terlalu kecil (di bawah 30) sehingga distribusi data tidak normal dan uji beda gagal. | Menargetkan minimal sampel $N \ge 30$ untuk memenuhi *Central Limit Theorem* agar distribusi normal. |

**Statistical Plan:**
  **Uji statistik** : *One-Sample T-Test* (Uji-T Satu Sampel)
  **Justifikasi** : Digunakan untuk membandingkan nilai rata-rata dari satu kelompok sampel independen (Skor SUS KHS) dengan satu nilai referensi atau standar populasi (Skor *Acceptable* 68).
  **Alpha** : 0.05 ($p < 0.05$)
  **Effect size min**: *Cohen's d* $\ge$ 0.5 (Tingkat signifikansi praktis moderat).

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Bagaimana tingkat usabilitas fitur Kartu Hasil Studi (KHS) pada SIM UPB jika diukur menggunakan metode *System Usability Scale* (SUS) dibandingkan dengan standar *acceptable score*?
**Tipe eksperimen:** [x] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| **Control** | Nilai ambang batas (*threshold*) SUS yang divalidasi oleh literatur sebagai standar sistem layak pakai (*Acceptable*). | Nilai Uji (*Test Value*) = 68 | Standar global evaluasi (Bangor et al., 2009). |
| **Treatment** | Observasi kuantitatif terhadap mahasiswa pengguna fitur KHS pada sistem yang berjalan. | Interaksi dengan UI KHS SIM UPB | 10 item kuesioner SUS dan skenario instruksi tugas konstan. |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah *fair*.

| Kriteria | Status | Detail |
|----------|--------|--------|
| **Dataset identik** | ✅ Setara | Sampel responden ditarik dari populasi yang sama (mahasiswa UPB aktif) yang memiliki beban kepentingan yang sama terhadap KHS. |
| **Preprocessing setara** | ✅ Setara | Perlakuan pembersihan data (*data cleaning*) diberlakukan sama pada semua entri responden sebelum diolah dengan Python. |
| **Tuning effort setara** | ✅ Setara | Tidak ada manipulasi antarmuka/bantuan tambahan (*prompting*) yang diberikan kepada responden saat mereka mengerjakan skenario tugas. |
| **Environment identik** | ✅ Setara | Instruksi tugas dan skenario navigasi dikunci agar setiap responden memulai evaluasi dengan beban kognitif awal yang sama. |
| **Metrik evaluasi sama** | ✅ Setara | Pembandingan dilakukan secara persis antara skor komposit SUS (0-100) melawan nilai target standar (68). |

**Ada yang tidak fair?** [ ] Ya / [x] Tidak
> **Jika ya, bagaimana cara memperbaikinya?** (Dalam desain observasi eksperimental ini, kondisi pengujian sudah diisolasi dengan baik melalui penyeragaman instrumen pengukuran).

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| **Internal** | Responden kebingungan dengan pertanyaan genap SUS yang menggunakan kalimat bernada negatif (*negative phrasing*). | Menyertakan penjelasan singkat di bagian *header* formulir, dan mengeliminasi data responden yang skornya saling bertolak belakang ekstrim. |
| **External** | Desain fitur KHS berubah di tengah-tengah masa penyebaran kuesioner karena *update patch* dari kampus. | Membatasi durasi pengambilan data survei (maksimal 1-2 minggu) untuk memastikan sistem yang diuji tidak mengalami *update version*. |
| **Construct** | Responden menjawab asal-asalan karena merasa kuesionernya terlalu panjang atau tidak ada untungnya bagi mereka (*Survey Fatigue*). | Menjaga agar kuesioner tetap ringkas (hanya 10 item inti SUS + 1 kolom saran) tanpa menambah variabel pengganggu lainnya. |
| **Conclusion** | Kesalahan penarikan kesimpulan akibat salah menghitung pola skor inversi (pertanyaan ganjil dikurangi 1, pertanyaan genap 5 dikurangi nilai jawaban). | Menggunakan *template/formula* perhitungan otomatis yang sudah terverifikasi (misalnya perhitungan bawaan Python untuk standar SUS) daripada menghitung manual. |

**Ancaman mana yang paling sulit dimitigasi?** **External Threat** (Perubahan sistem tanpa pemberitahuan dari *developer* kampus).
**Mengapa?**
> Karena penelitian kita berada di posisi *end-user* observasional dan kita tidak memiliki kontrol terhadap jadwal pemeliharaan ( *maintenance/update*) sistem akademik kampus. Jika UI/UX diubah oleh *developer* tepat di tengah masa survei, setengah data responden kita menjadi tidak relevan karena menilai antarmuka yang sudah usang, merusak validitas eksperimen.

---

## Refleksi

> Sebuah paper melaporkan "sistem/metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. **Apakah pemilihan *baseline*-nya jujur (*fair*)?** (Apakah sistem tersebut dibandingkan dengan standar kelayakan industri yang sesungguhnya (seperti SUS 68) atau hanya dibandingkan dengan *straw man* / sistem lama yang memang sudah cacat dan usang?).
2. **Apakah metrik yang digunakan benar-benar valid (*Construct Validity*)?** (Apakah klaim "mengalahkan" itu didasarkan pada skor pengalaman pengguna (*user experience*) yang objektif atau hanya opini subjektif dari pengembangnya sendiri tanpa kuesioner terstandar?).
3. **Apakah klaim signifikansi didukung oleh ukuran sampel dan uji statistik yang memadai (*Conclusion Validity*)?** (Apakah peningkatan tersebut diuji dengan pengujian statistik seperti *T-Test* dengan *p-value* $< 0.05$ dan jumlah sampel minimal, atau perbedaannya terjadi hanya karena kebetulan acak dari 5 orang penguji saja?).