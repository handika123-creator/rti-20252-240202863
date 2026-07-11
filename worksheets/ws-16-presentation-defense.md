# WS-16: Presentation & Defense (UAS)

> **Bab 16 — Presentasi & Pertahanan Ilmiah**

---

## Ringkasan Materi

### Scientific Defense Model

```
Research Work → Presentation → Questioning → Defense → Evaluation → Acceptance
```

### Presentasi ≠ Ringkasan Paper

| Paper | Presentasi |
|-------|-----------|
| Dibaca (self-paced) | Didengar (presenter-paced) |
| Detail lengkap | Ide kunci + highlight |
| Tabel numerik detail | Grafik visual + angka kunci |
| Pembaca bisa re-read | Audiens dengar sekali |

**Prinsip:** Presentasi membutuhkan **reformulasi**, bukan kompresi. Medium berbeda = pendekatan berbeda.

### Claim-Evidence-Reasoning (CER)

Setiap jawaban defense harus memiliki:
1. **Claim** — Pernyataan yang dijawab
2. **Evidence** — Data/fakta pendukung
3. **Reasoning** — Logika yang menghubungkan evidence ke claim

**Contoh:**

| Pertanyaan | Bad Answer | Good Answer (CER) |
|-----------|-----------|-------------------|
| "Kenapa hanya 3 dataset?" | "Tiga sudah cukup" | "3 dataset mewakili variasi: small-clean, medium-clean, medium-noisy [E]. Generalisasi perlu validasi lanjut — listed as limitation [R]" |
| "Hasil DS-3 menurun?" | "Itu outlier" | "Ya, karena distribusi heavy-tail melanggar asumsi Gaussian [E]. Ini menunjukkan boundary condition metode [R]" |
| "Effect size?" | "p=0.003, jadi signifikan" | "Cohen's d=1.2 (large effect) [E] — bukan hanya signifikan tapi substansial [R]" |

### Slide Design — One Slide, One Message

**Optimal 9-Slide Plan (15 menit):**

| # | Slide | Waktu | Pesan |
|---|-------|-------|-------|
| 1 | Title + context | 1 min | Apa ini tentang apa |
| 2 | Problem + motivation | 2 min | Mengapa penting |
| 3 | Gap + RQ | 1.5 min | Apa yang belum terjawab |
| 4 | Method overview | 2 min | Bagaimana dijawab (diagram) |
| 5 | Key result — tabel | 2 min | Temuan utama |
| 6 | Key result — grafik | 2 min | Pola visual |
| 7 | Interpretation + failure | 2 min | Apa artinya |
| 8 | Limitation + future | 1.5 min | Batasan & arah |
| 9 | Conclusion + contribution | 1 min | Closing message |

### Anticipatory Defense

Prediksi pertanyaan berdasarkan kategori:

| Kategori | Contoh Pertanyaan |
|---------|------------------|
| Problem | "Mengapa masalah ini penting?" |
| Gap | "Bagaimana dengan studi X yang sudah menjawab ini?" |
| Method | "Mengapa metode ini, bukan Y?" |
| Results | "Bagaimana menjelaskan anomali di DS-3?" |
| Generalization | "Apakah bisa diterapkan di domain lain?" |

### Tiga Prinsip Jawaban

1. **Direct** — Jawab dulu, elaborasi kemudian
2. **Data-based** — Tunjuk evidence spesifik
3. **Honest** — Akui limitasi jika memang ada

### Jebakan Kognitif

1. "Presentasi = semua yang ada di paper" → terlalu padat
2. "Slide cantik = presentasi bagus" → konten > estetika
3. "Tidak bisa jawab = gagal" → "I don't know, but..." menunjukkan kejujuran
4. "Tidak perlu latihan — saya paham riset saya" → latihan = menemukan celah

---

## Template A.16 — Defense Preparation Sheet

```
DEFENSE PREPARATION

Slide Deck Plan:
  Total slides   : 9 slide konten utama (10 dengan slide penutup)
  Time per slide : ~1.5 menit
  Total time     : 15 menit

**Slide Outline:**

| # | Pesan Utama | Visual | Waktu |
|---|---|---|---|
| 1 | Title | Logo Kampus + Judul Riset | 30s |
| 2 | Problem | Foto UI KHS + Kutipan keluhan mahasiswa | 2min |
| 3 | Gap + RQ | Skema riset (Fokus KHS vs Keseluruhan SIM) | 1.5min |
| 4 | Method | Diagram Purposive Sampling (N=30) & Instrumen SUS | 2min |
| 5 | Key Result (Data) | Tabel 10 Item Pertanyaan & Rata-rata 63.33 | 2min |
| 6 | Key Result (Grafik) | Histogram Distribusi Skor KHS (Garis Target 68) | 2min |
| 7 | Interpretation | Penjelasan Adjektif SUS (Marginal / Poor) | 2min |
| 8 | Limitation | Keterbatasan (Sample Size & Fokus Modul) | 1.5min |
| 9 | Conclusion | Rekomendasi redesign UI *Mobile Responsive* | 1.5min |

**Anticipatory Defense Matrix:**

| Kategori | Pertanyaan Potensial | Jawaban (CER) |
|---|---|---|
| Method | Mengapa hanya 30 responden? | **[C]** Cukup untuk statistik parametrik **[E]** N=30 adalah standar Central Limit Theorem agar berdistribusi normal **[R]** Uji T-Test sudah bisa memvalidasi signifikansi. |
| Method | Mengapa memakai skala SUS, bukan kuesioner buatan sendiri? | **[C]** Karena reliabilitasnya sudah teruji global **[E]** SUS memiliki standar benchmark baku (skor 68.0) **[R]** Menghindari bias validitas jika menyusun butir soal sendiri tanpa uji reliabilitas Alpha Cronbach. |
| Results | Skor 63.33 itu artinya gagal dong sistem kampusnya? | **[C]** Tidak gagal total, tapi perlu perbaikan **[E]** Menurut literatur Bangor (2008), masuk Grade D (Marginal) **[R]** Fitur fungsi dasar (*utility*) berjalan, tapi antarmuka (*usability*) membingungkan. |

**Latihan:**
- Latihan 1: H-3 UAS — Fokus durasi
- Latihan 2: H-2 UAS — Fokus kelancaran transisi antar slide
- Latihan 3: H-1 UAS — Simulasi Q&A
```

---

## Latihan 1 — Slide Outline

Rencanakan presentasi 15 menit untuk riset Anda.

| # | Pesan Utama | Visual yang Digunakan | Waktu |
|---|---|---|---|
| 1 | Judul & Konteks: Riset Usability SIM UPB | Title Slide formal | 1 min |
| 2 | Masalah: Portal kaku, mahasiswa bingung cek IPK/KHS di HP. | Screenshot antarmuka tabel KHS di layar mobile yang terpotong. | 2 min |
| 3 | RQ: Berapa skor aktual usabilitas fitur ini secara saintifik? | Teks rumusan masalah besar di tengah slide. | 1.5 min |
| 4 | Metode: 30 Responden, Instrumen SUS, Kalkulasi Statistik. | Ikon 30 user, Skema Likert (1-5), Logo Python. | 2 min |
| 5 | Hasil 1 (Deskriptif): Nilai Rata-rata cuma 63.33 | Angka 63.33 besar berwarna kuning/merah. | 1.5 min |
| 6 | Hasil 2 (Visualisasi): Meleset dari target global (68.0) | Histogram sebaran data dengan 2 garis vertikal (Mean vs Target). | 2 min |
| 7 | Analisis (Failure): Letak masalah pada responsivitas & navigasi | Word-cloud atau kutipan saran perbaikan dari responden. | 2 min |
| 8 | Limitasi: Hanya mengevaluasi 1 modul (KHS) | Bullet points batasan penelitian. | 1 min |
| 9 | Kesimpulan: Perlu UI Redesign | Ringkasan eksekutif poin temuan. | 2 min |

**Total waktu estimasi:** 15 menit

---

## Latihan 2 — Anticipatory Defense

Prediksi 5 pertanyaan yang mungkin diajukan penguji, lalu siapkan jawaban CER.

| # | Kategori | Pertanyaan | Claim | Evidence | Reasoning |
|---|---|---|---|---|---|
| 1 | Problem | KHS kan diakses setahun cuma 2x, kenapa repot diteliti? | Frekuensi rendah, kepentingannya tinggi (Krusial) | KHS syarat mutlak KRS semester depan | Jika proses KHS terhambat, siklus akademik mahasiswa tertunda, menimbulkan kepanikan *(UX bottleneck)*. |
| 2 | Method | Yakin tidak ada mahasiswa yang isi *Straight-lining* (Asal klik angka 3)? | Datanya bersih dan valid | Skor Standar Deviasi per baris responden > 0 di WS-11 | Tidak ada anomali tebak-tebakan, semua membaca soal dengan baik. |
| 3 | Results | Ini 63 kan mepet ke 68, harusnya bisa dibulatkan jadi bagus kan? | Tidak bisa, ini signifikan secara statistik | Uji One-Sample T-test menunjukkan p < 0.05 | Perbedaan angka bukan sekadar pembulatan, tapi gap nyata kualitas. |
| 4 | Genrzltn | Apa temuan KHS ini otomatis berlaku juga buat modul KRS? | Belum tentu, perlu riset terpisah | UI/UX fitur KRS memiliki kerumitan *(task flow)* berbeda dari KHS | Hasil ini spesifik untuk fitur pembacaan tabel nilai, bukan form input. |
| 5 | Solusi | Terus, apa saran konkrit kamu untuk pihak IT kampus? | Redesign tampilan Mobile (*Mobile-first*) | Responden mengeluhkan tabel yang harus digeser ke kanan-kiri di HP | Mayoritas mahasiswa mengakses SIM via *smartphone*, antarmuka KHS harus diubah jadi format *Card* atau tabel responsif. |

---

## Latihan 3 — Simulasi Q&A

Minta teman/kolega mengajukan 3 pertanyaan tentang riset Anda. Catat pertanyaan dan evaluasi jawaban Anda.

| # | Pertanyaan (Simulasi) | Jawaban Saya | Evaluasi |
|---|---|---|---|
| 1 | "Kamu nyebar kuesionernya random atau pilih-pilih?" | "Purposive pak/bu. Ada pertanyaan screening di awal Form. Kalau dia pilih belum pernah buka KHS, datanya tidak saya ikutkan ke hitungan akhir." | [x] Direct [x] Data-based [x] Honest |
| 2 | "Adakah dosen yang kamu libatkan sebagai responden?" | "Tidak ada. Fokus instrumen ini adalah untuk *end-user* utama fitur KHS, yaitu mahasiswa S1." | [x] Direct [x] Data-based [x] Honest |

**Pertanyaan yang paling sulit dijawab:**
> Kalau nilai 63.33 itu marginal, lalu bagian fitur KHS mana spesifiknya yang paling parah membuat skornya anjlok?

**Apa yang perlu disiapkan lebih baik:**
> Membuka kembali data CSV (Data_KHS_Raw), lalu mengecek rata-rata skor pada masing-masing pertanyaan (Q1 s/d Q10) untuk melihat pertanyaan mana yang paling sering mendapat nilai jelek dari responden.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-16 — dari paradigma riset hingga presentasi — bagian mana yang paling mengubah cara Anda berpikir tentang riset? Apa satu hal yang akan selalu Anda terapkan di riset berikutnya?

**Insight terbesar:**
Bagian yang paling mengubah cara pandang saya adalah *Failure Analysis* (WS-14) dan *Visualization Bias* (WS-12). Saya dulunya takut jika skor eksperimen saya "jelek" karena mengira risetnya gagal. Ternyata, membuktikan secara kuantitatif bahwa sebuah sistem memiliki *usability* buruk adalah kontribusi nyata yang berharga. Nilai jelek adalah temuan, bukan dosa.

**Yang akan selalu diterapkan:**
Konsep Data *Logging* yang ketat (WS-10 & WS-11) dan menjauhi kebiasaan menghapus data ekstrem secara diam-diam. Validitas hasil tidak ditentukan dari seberapa tinggi angka akhirnya, melainkan seberapa jujur *pipeline* *preprocessing* yang dilakukan.