# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

`Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)`

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
Bab 2 (Problem) → | memperkenalkan masalah X + evidensi |
                  | ↓ menimbulkan pertanyaan: "apa akar gap-nya?"
Bab 3 (Gap)     → | menjawab pertanyaan tadi + membuka "lalu apa yang perlu diteliti?" |
                  | ↓
Bab 4 (RQ/H)    → | menjawab gap dengan pertanyaan spesifik + prediksi terukur |
                  | ↓
Bab 5-7 (Method)→ | menjawab RQ melalui desain eksperimen yang tepat |

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

---

## Template A.8 — Integration Checklist

**PROPOSAL INTEGRATION CHECKLIST**

**Koneksi Vertikal (Flow Atas-Bawah):**
  [x] **Problem → Gap:** masalah ketiadaan evaluasi empiris KHS terdokumentasi dan divalidasi oleh literatur (Context/Method Gap).
  [x] **Gap → RQ:** pertanyaan spesifik mengukur nilai SUS untuk menjawab gap ketiadaan data kelayakan.
  [x] **RQ → Hypothesis:** hipotesis memprediksi bahwa nilai SUS KHS > 68 (Sistem layak).
  [x] **Hypothesis → Metric:** metrik SUS secara presisi mengukur tingkat usabilitas (kelayakan) dalam hipotesis.
  [x] **Metric → System:** komponen sistem kuesioner merekam skala Likert dan mengonversinya menjadi skor komposit metrik.
  [x] **System → Experiment:** desain eksperimen komparatif menggunakan instrumen kuesioner tersebut melawan *baseline* 68.

**Koneksi Horizontal (Konsistensi):**
  [x] Istilah sama di semua bagian (Konsisten menggunakan "Fitur KHS SIM UPB" dan "System Usability Scale").
  [x] Variabel di RQ = variabel di hipotesis = metrik di desain.
  [x] Scope tidak berubah dari masalah ke eksperimen (Tetap fokus pada tahap Evaluasi, tidak melompat ke Perancangan/Figma).

**Cognitive Trap Checklist:**
  [x] Tidak ada paragraf "promosi" di pendahuluan (hanya memaparkan data penggunaan KHS & gap evaluasi).
  [x] Metodologi disesuaikan ke RQ, bukan *copy-paste* textbook.
  [x] Timeline sudah ditambah *buffer* 30-50% dari estimasi awal (Terutama untuk durasi pengumpulan sampel responden).
  [x] Proposal mengakui kemungkinan H₀ tidak ditolak (*honest uncertainty* - bisa jadi sistem memang belum layak).
  [x] Tidak ada klaim "pasti berhasil" atau "meningkatkan signifikan" (karena sifatnya observasional).

**Rubrik Self-Assessment:**

| Kriteria     | 1 (Lemah)                                        | 2 (Cukup)                                     | 3 (Baik)                                           | Skor |
|------------- |--------------------------------------------------|-----------------------------------------------|----------------------------------------------------|------|
| **Koherensi** | >2 koneksi vertikal terputus                     | 1-2 koneksi lemah, argumen masih bisa diikuti | Semua 6 koneksi terhubung, *red thread* jelas      | 3    |
| **Specificity** | Variabel/metrik masih abstrak, tidak ada angka   | Sebagian metrik terdefinisi numerik           | Semua metrik + threshold (68) + unit pengukuran jelas| 3    |
| **Feasibility** | Timeline >6 bulan tanpa memperhitungkan sumber   | Timeline 3-6 bulan dengan asumsi tertentu     | Timeline 1-3 bulan realistis dengan rencana detail | 3    |
| **Rigor** | Baseline tidak jelas atau straw man              | 1-2 baseline dengan justifikasi partial       | 2+ baseline SOTA (SUS) + justifikasi lengkap       | 3    |

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal.

| Komponen | Sumber | Isi (1-2 kalimat) |
|----------|--------|-------------------|
| **Problem Statement** | WS-02 | Fitur KHS SIM UPB sangat vital, namun ketiadaan evaluasi empiris membuat kelayakan antarmukanya tidak diketahui secara pasti, membiarkan keluhan mahasiswa tetap bersifat subjektif. |
| **Gap** | WS-03 | Belum ada evaluasi terisolasi menggunakan instrumen SUS khusus untuk fitur KHS di lingkungan Sistem Informasi Manajemen Universitas Putra Bangsa. |
| **RQ** | WS-04 | Bagaimana tingkat usabilitas fitur Kartu Hasil Studi (KHS) pada SIM UPB jika diukur menggunakan metode *System Usability Scale* (SUS) dibandingkan dengan standar *acceptable score*? |
| **Hipotesis** | WS-04 | **H₁**: Skor rata-rata SUS fitur KHS SIM UPB melampaui batas 68 (Sistem memenuhi standar kelayakan usabilitas secara signifikan). |
| **Variabel & Metrik** | WS-05 | **IV**: Fitur KHS SIM UPB eksisting; **DV**: Tingkat Usabilitas; **Metrik**: Skor komposit *System Usability Scale* (0-100). |
| **Sistem** | WS-06 | Instrumen pengukuran kuesioner terstandar (Google Form SUS 10-Item) dengan Skenario Tugas (CV) yang dikunci. |
| **Desain Eksperimen**| WS-07 | Pengujian observasional komparatif yang membandingkan skor SUS dari sampel mahasiswa melawan *baseline/threshold* kelayakan global (Skor 68). |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| **Problem → Gap** | ✅ Teralurkan | Gap (ketiadaan data kuantitatif KHS) lahir langsung dari akar masalah keluhan subjektif yang tidak terukur. |
| **Gap → RQ** | ✅ Teralurkan | RQ secara langsung bertanya tentang angka usabilitas menggunakan alat ukur untuk mengisi kekosongan data tersebut. |
| **RQ → Hypothesis** | ✅ Teralurkan | H₁ memberikan prediksi jawaban yang terukur (skor > 68) atas pertanyaan di RQ. |
| **Hypothesis → Metric**| ✅ Teralurkan | Metrik menggunakan sistem hitung SUS 0-100 yang secara presisi mengukur variabel kelayakan di dalam hipotesis. |
| **Metric → System** | ✅ Teralurkan | Sistem (kuesioner) secara mekanis mengumpulkan skala Likert dan merekapnya menjadi data siap hitung untuk metrik. |
| **System → Experiment**| ✅ Teralurkan | Eksperimen bergantung pada penyebaran sistem (kuesioner) tersebut kepada kelompok perlakuan untuk dibandingkan dengan *baseline*. |

**Koneksi mana yang paling lemah?** `System → Experiment`
**Bagaimana cara memperkuatnya?**
> Karena riset ini bersifat survei *online* (bukan *software testing* di lab terisolasi), kita tidak bisa memantau apakah responden benar-benar mengakses KHS sebelum mengisi form. Cara memperkuatnya adalah dengan memberikan instruksi skenario wajib di awal form dan menaruh satu pertanyaan penyaring (*screening question*) mengenai informasi spesifik di KHS untuk memastikan mereka benar-benar melakukan interaksi.

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [x] Ya / [ ] Tidak
> **Jika tidak, di bagian mana terjadi inkonsistensi?** (Seluruh proposal sudah konsisten. Tidak ada lagi lompatan ide tiba-tiba membahas "Figma", "Redesain", atau "Mobile Apps").

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| **Koherensi** | 3 | Seluruh argumen dari Latar Belakang hingga Eksperimen terhubung tanpa adanya pergeseran fokus atau intervensi topik baru (*red thread* sangat jelas). |
| **Specificity**| 3 | Penggunaan instrumen SUS memberikan *threshold* angka pasti (68) dan spesifikasi *grading scale* yang terdefinisi secara numerik. |
| **Feasibility**| 3 | Metode evaluasi survei SUS memangkas waktu riset drastis (hanya 1-2 bulan) karena tidak melibatkan beban implementasi *coding* atau iterasi perancangan UI. |
| **Rigor** | 3 | Menggunakan *baseline* literatur global yang sudah menjadi *gold standard* sejak 2009 (Bangor et al.) untuk justifikasi kelayakan. |

**Skor total:** **12** / 12

**Apakah proposal siap untuk fase eksekusi?** [x] Ya / [ ] Belum
> **Jika belum, apa yang perlu diperbaiki?** Proposal siap dieksekusi. Tahap selanjutnya tinggal menyusun 10 pertanyaan kuesioner ke dalam platform survei.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** Mengisi WS-05 (Variabel & Metrik), karena metode evaluasi yang dipilih (SUS) sudah memiliki aturan baku, rumus hitung yang pasti, dan sangat mudah dioperasionalisasikan menggunakan instrumen kuesioner umum.
**Bagian tersulit:** Mengisi WS-02 dan WS-03, yaitu proses menahan ego *Engineering*. Sangat sulit untuk tidak terjebak pada *Solution-First Thinking* (ingin langsung menawarkan solusi redesain antarmuka) saat menyusun rumusan masalah dan mencari gap riset.
**Yang akan dilakukan berbeda:**
> Jika mengulang dari awal, saya akan melakukan pembacaan literatur (*literature review*) dengan pendekatan *Concept-centric* sejak hari pertama. Daripada membuang waktu memikirkan solusi *software engineering* yang rumit, saya akan langsung mencari tahu celah (gap) evaluasi dan pengujian apa yang belum pernah dilakukan di lingkungan kampus saya, sehingga proses penentuan metrik dan eksperimen akan jauh lebih lurus dan koheren.