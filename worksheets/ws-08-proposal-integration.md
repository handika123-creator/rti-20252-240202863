# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

```
Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)
```

| Koneksi | Pertanyaan Verifikasi |
|---------|----------------------|
| Problem → Gap | Apakah gap muncul dari analisis literatur terhadap masalah? |
| Gap → RQ | Apakah RQ langsung menjawab gap yang teridentifikasi? |
| RQ → Metrik | Apakah setiap variabel di RQ punya metrik terdefinisi? |
| Metrik → Sistem | Apakah setiap metrik bisa diukur oleh komponen sistem? |
| Sistem → Eksperimen | Apakah desain eksperimen menggunakan sistem sebagai instrumen? |

### Koherensi Vertikal + Horizontal

- **Vertikal** — Alur logis atas-ke-bawah (problem → experiment). Setiap section menjawab pertanyaan yang diangkat section sebelumnya dan memunculkan pertanyaan baru.
- **Horizontal** — Konsistensi terminologi (nama variabel di RQ = di hipotesis = di metrik = di desain)

**Operasionalisasi Red Thread** (benang merah):
```
Bab 2 (Problem) → | memperkenalkan masalah X + evidensi |
                          ↓ menimbulkan pertanyaan: "apa akar gap-nya?"
Bab 3 (Gap)     → | menjawab pertanyaan tadi + membuka "lalu apa yang perlu diteliti?" |
                          ↓
Bab 4 (RQ/H)    → | menjawab gap dengan pertanyaan spesifik + prediksi terukur |
                          ↓
Bab 5-7 (Method)→ | menjawab RQ melalui desain eksperimen yang tepat |
```
Jika ada lompatan (section B tidak menjawab pertanyaan section A), red thread putus.

### Jebakan Kognitif

| Jebakan | Deskripsi |
|---------|----------|
| "Selling" Introduction | Menulis promosi, bukan menyajikan data dan gap |
| Copy-paste Methodology | Menyalin deskripsi tekstbook tanpa menyesuaikan ke RQ |
| Optimistic Timeline | Meremehkan waktu implementasi; selalu tambah buffer 30-50% |
| No Possibility of Failure | Mengimplikasikan hasil pasti sukses — proposal jujur mengakui H₀ mungkin tidak ditolak |

### Struktur Proposal

1. **Pendahuluan** — Latar belakang + problem statement (Bab 1-2)
2. **Tinjauan Pustaka** — Literature review + gap + baseline (Bab 3)
3. **RQ / Kontribusi / Hipotesis** — (Bab 4)
4. **Metodologi** — Metrik + sistem + desain eksperimen (Bab 5-7)
5. **Timeline & Output**

### Istilah Penting

- **Integration Map** — Diagram 6 koneksi kritis antar komponen proposal
- **Vertical Coherence** — Alur logis atas-ke-bawah
- **Horizontal Coherence** — Konsistensi terminologi di semua bagian
- **Checkpoint** — Titik self-assessment sebelum transisi dari desain ke eksekusi

---

## Template A.8 — Integration Checklist

```
PROPOSAL INTEGRATION CHECKLIST

Koneksi Vertikal (Flow Atas-Bawah):
  [x] Problem → Gap: masalah terdokumentasi di literatur
  [x] Gap → RQ: pertanyaan menjawab gap spesifik
  [x] RQ → Hypothesis: hipotesis memprediksi jawaban
  [x] Hypothesis → Metric: metrik mengukur variabel dalam hipotesis
  [x] Metric → System: komponen sistem menghasilkan/mengukur metrik
  [x] System → Experiment: desain eksperimen menggunakan sistem

Koneksi Horizontal (Konsistensi):
  [x] Istilah sama di semua bagian
  [x] Variabel di RQ = variabel di hipotesis = metrik di desain
  [x] Scope tidak berubah dari masalah ke eksperimen

Cognitive Trap Checklist:
  [x] Tidak ada paragraf "promosi" di pendahuluan (hanya data & gap)
  [x] Metodologi disesuaikan ke RQ, bukan copy-paste textbook
  [x] Timeline sudah ditambah buffer 30-50% dari estimasi awal
  [x] Proposal mengakui kemungkinan H0 tidak ditolak (honest uncertainty)
  [x] Tidak ada klaim "pasti berhasil" atau "meningkatkan signifikan"

Rubrik Self-Assessment:
| Kriteria     | 1 (Lemah)                                        | 2 (Cukup)                                     | 3 (Baik)                                           | Skor |
|------------- |--------------------------------------------------|-----------------------------------------------|----------------------------------------------------|------|
| Koherensi    | >2 koneksi vertikal terputus                     | 1-2 koneksi lemah, argumen masih bisa diikuti | Semua 6 koneksi terhubung, red thread jelas        |      |
| Specificity  | Variabel/metrik masih abstrak, tidak ada angka   | Sebagian metrik terdefinisi numerik           | Semua metrik + threshold + unit pengukuran jelas   |      |
| Feasibility  | Timeline >6 bulan tanpa memperhitungkan sumber   | Timeline 3-6 bulan dengan asumsi tertentu     | Timeline 1-3 bulan realistis dengan rencana detail |      |
| Rigor        | Baseline tidak jelas atau straw man              | 1-2 baseline dengan justifikasi partial       | 2+ baseline SOTA + justifikasi pemilihan lengkap   |      |
```

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal.

| Komponen | Sumber | Isi (1-2 kalimat) |
|----------|--------|-------------------|
| Problem Statement | WS-02 | Akses SIAKAD melalui mobile browser memicu kesalahan klik (fat-finger error) dan navigasi yang berlebihan karena tata letaknya masih berorientasi desktop, sehingga menurunkan efisiensi. |
| Gap | WS-03 | Belum ada studi yang membandingkan performa secara head-to-head antara web SIAKAD eksisting dengan desain mobile native berpusat pada pengguna melalui desain eksperimen berpasangan. |
| RQ | WS-04 | Apakah implementasi purwarupa aplikasi mobile native SIAKAD meningkatkan skor usabilitas dan mereduksi durasi penyelesaian tugas secara signifikan dibandingkan web eksisting? |
| Hipotesis | WS-04 | H1: Purwarupa aplikasi mobile native menghasilkan peningkatan skor System Usability Scale (SUS) dan penurunan waktu Time on Task yang signifikan dibandingkan web eksisting. |
| Variabel & Metrik | WS-05 | IV = Platform sistem (Web eksisting vs. Purwarupa Mobile). DV = Kepuasan subjektif (Skor SUS 0-100) dan Efisiensi fisik (Time on Task dalam detik). |
| Sistem | WS-06 | High-fidelity interactive prototype SIAKAD yang dirancang menggunakan platform Figma, mensimulasikan fitur pengisian KRS dan pengecekan transkrip nilai secara dinamis. |
| Desain Eksperimen | WS-07 | Within-Subjects Design menggunakan teknik counterbalancing. Partisipan (mahasiswa S1 Ilmu Komputer) mengeksekusi 3 skenario tugas pada kedua platform secara bergantian di bawah observasi waktu. |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| Problem → Gap | ✅ | Masalah navigasi seluler sudah terdokumentasi, dan literatur di Bab 3 mengonfirmasi kurangnya pengujian komparatif langsung untuk solusi mobile native. |
| Gap → RQ | ✅ | RQ secara spesifik mempertanyakan komparasi langsung antara sistem lama dengan sistem baru hasil Design Thinking. |
| RQ → Hypothesis | ✅ | Hipotesis secara tegas memprediksi bahwa sistem mobile native (intervensi) akan lebih unggul dari sistem web (kontrol). |
| Hypothesis → Metric | ✅ | Variabel kepuasan diukur melalui instrumen SUS (0-100) dan variabel efisiensi diukur menggunakan Time on Task (detik/stopwatch). |
| Metric → System | ✅ | Purwarupa Figma memiliki alur fungsional yang memungkinkan partisipan melakukan klik dan navigasi sehingga durasi waktu operasionalnya bisa diukur secara konkret. |
| System → Experiment | ✅ | Eksperimen mewajibkan partisipan berinteraksi langsung dengan purwarupa Figma (mobile) dan Google Chrome (web) sebagai objek utama instrumen pengujian. |

**Koneksi mana yang paling lemah?** Koneksi Metric - System.
**Bagaimana cara memperkuatnya?**
> Memastikan purwarupa Figma diakses melalui aplikasi Figma Mirror di gawai dengan semua aset visual telah dimuat (pre-cached) sebelumnya. Hal ini mencegah gangguan koneksi internet yang dapat membiaskan perhitungan metrik durasi murni (Time on Task).

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [x] Ya / [ ] Tidak
> Jika tidak, di bagian mana terjadi inkonsistensi? _________

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| Koherensi | 3 (Baik) | Seluruh 6 koneksi terhubung kuat. Benang merah dari masalah tata letak web hingga metode Paired Sample T-Test sangat koheren dan mengalir logis. |
| Specificity | 3 (Baik) | Variabel dan metrik terdefinisi dengan sangat kuantitatif (Skala Likert untuk SUS 0-100 dan pengukuran stopwatch milidetik untuk Time on Task). |
| Feasibility | 3 (Baik) | Jadwal 4 bulan (Timeline) sangat realistis, detail, dan sudah memperhitungkan alokasi satu bulan penuh untuk pengumpulan data serta counterbalancing di laboratorium. |
| Rigor | 3 (Baik) | Eksperimen memiliki baseline yang sangat konkret (SIAKAD Web saat ini) dan didukung oleh komparasi 15 literatur standar APA 7th. |

**Skor total:** 12 / 12

**Apakah proposal siap untuk fase eksekusi?** [x] Ya / [ ] Belum
> Jika belum, apa yang perlu diperbaiki? __________________

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** Mengidentifikasi masalah (Problem Statement) dan merumuskan metrik ukur, karena kendala usabilitas pada platform akademik eksisting sangat sering dialami secara langsung oleh mahasiswa di lapangan.
**Bagian tersulit:** Menyusun desain eksperimen, khususnya memastikan bahwa eksperimen Within-Subjects tidak bias akibat efek pembelajaran (learning effect), sehingga memerlukan penerapan metode counterbalancing yang ketat.
**Yang akan dilakukan berbeda:**
> Jika memulai dari awal, saya akan mengalokasikan waktu observasi kualitatif (empathize) yang lebih panjang sebelum melompat ke fase desain antarmuka, untuk memastikan tidak ada fitur minor yang terlewat saat proses penyusunan skenario tugas akademik.