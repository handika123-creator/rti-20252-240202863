# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi 

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
**Domain & Konteks**
*   **Domain:** Interaksi Manusia dan Komputer (HCI) / Sistem Informasi
*   **Konteks:** Evaluasi Usabilitas Antarmuka Sistem Informasi Akademik

**System Context**
*   **Input:** Interaksi klik dan navigasi dari mahasiswa pada platform SIM UPB.
*   **Process:** Sistem merender tata letak informasi dan data akademik semester.
*   **Output:** Antarmuka visual halaman Kartu Hasil Studi (KHS).
*   **Outcome:** Mahasiswa berhasil mengakses, membaca, dan memahami nilai akademiknya secara mandiri.
*   **Constraints:** Evaluasi berfokus pada sisi antarmuka pengguna (front-end UI/UX), tanpa mengakses atau mengubah basis data (backend).
*   **Stakeholders:** Mahasiswa (end-user), Pengelola Akademik (pengambil keputusan).

**Fenomena → Problem**
*   **Fenomena yang diamati:** Mahasiswa rutin mengakses fitur KHS setiap akhir semester, namun sering muncul keluhan non-formal terkait tata letak atau kesulitan teknis saat mengunduh/membaca data.
*   **Gejala (symptom) yang terukur:** Ketiadaan metrik kelayakan yang jelas; keluhan masih bersifat subjektif dan sporadis.
*   **Masalah yang didiagnosis:** Belum adanya evaluasi empiris yang mengukur tingkat usabilitas fitur KHS pada SIM UPB secara standar dan terpusat.
*   **Masalah riset (researchable):** Bagaimana tingkat usabilitas fitur KHS pada SIM UPB jika diukur menggunakan metode standar *System Usability Scale* (SUS)?
*   **Variabel yang terukur:** Skor komposit *System Usability Scale* (skala 0-100).

**Problem Quality Check**
*   [x] **Clarity** — Apakah satu orang membaca akan paham?
*   [x] **Measurability** — Apakah ada metrik kuantitatif?
*   [x] **Relevance** — Apakah penting untuk domain?
*   [x] **Testability** — Apakah bisa gagal?
*   [x] **Impact** — Apakah ada kontribusi jika terjawab?

**Problem Statement (1 paragraf):**
Fitur Kartu Hasil Studi (KHS) pada Sistem Informasi Manajemen (SIM) UPB merupakan instrumen vital bagi mahasiswa di setiap akhir semester, namun ketiadaan evaluasi usabilitas yang empiris menyebabkan kelayakan antarmuka sistem saat ini tidak diketahui secara pasti (*Empiric Gap*). Tanpa adanya pengukuran yang terstandar, keluhan pengguna terkait navigasi dan tata letak informasi hanya menjadi asumsi subjektif yang sulit ditindaklanjuti. Oleh karena itu, riset ini akan mengevaluasi tingkat usabilitas fitur KHS menggunakan instrumen *System Usability Scale* (SUS) untuk menghasilkan data kuantitatif yang mengidentifikasi hambatan interaksi secara objektif, guna merumuskan rekomendasi perbaikan berbasis data bagi pengelola akademik.

---

## Latihan 1 — Dari Topik ke Masalah Riset

**Topik awal:** Evaluasi Antarmuka Sistem Informasi Manajemen (SIM) UPB

| Tahap | Hasil |
|-------|-------|
| **Reality** | Mahasiswa secara masif menggunakan fitur KHS di SIM UPB setiap periode akhir semester. |
| **Observed Issue (Symptom)** | Terdapat indikasi kebingungan dalam navigasi, pembacaan hierarki informasi (seperti perbedaan IPS dan IPK), atau kendala pencetakan dokumen KHS. |
| **Diagnosed Problem (Root Cause)** | Institusi belum memiliki rekam data objektif terkait kepuasan dan kemudahan pengguna spesifik pada fitur KHS tersebut. |
| **Researchable Problem** | Berapa tingkat kelayakan usabilitas (skor SUS) fitur KHS SIM UPB saat ini jika dibandingkan dengan standar global *acceptable score*? |
| **Measurable Variable** | Nilai kuantitatif *System Usability Scale* (0-100) dan respons item kuesioner. |

**Apakah terjebak solution-first thinking?** [ ] Ya / [x] Tidak
> **Jika ya, kembali ke tahap mana?** — (Tidak terjebak, karena rumusan masalah difokuskan pada pengukuran/evaluasi keadaan saat ini, bukan langsung menawarkan pembuatan desain baru).

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| **Input** | Aksi pengguna (mahasiswa) melakukan login, navigasi menu, dan interaksi pada halaman KHS. |
| **Process** | Sistem memproses permintaan, menarik (*query*) data nilai mahasiswa, dan menyajikannya dalam format tampilan *web*. |
| **Output** | Tampilan visual antarmuka (UI) halaman KHS yang berisi tabel mata kuliah dan nilai. |
| **Outcome** | Pemahaman mahasiswa mengenai status capaian akademik secara cepat, akurat, dan tanpa frustrasi. |
| **Constraints** | Penelitian dibatasi hanya pada pengukuran persepsi pengguna akhir (usabilitas) dan tidak menyentuh optimasi basis data atau modifikasi kode sistem secara langsung. |
| **Stakeholders** | Responden mahasiswa sebagai penguji, dan pihak manajemen kampus sebagai penerima rekomendasi perbaikan. |

**Komponen mana yang paling relevan dengan masalah riset?** Output (antarmuka visual) dan Outcome (kemudahan pemahaman pengguna).

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| **Clarity** | 5 | Sangat jelas. Fokus spesifik hanya pada fitur KHS pada SIM UPB dan metrik yang digunakan sudah disebutkan (SUS). |
| **Measurability** | 5 | Menggunakan skor kuesioner SUS yang memproduksi data numerik interval (0-100) yang siap diuji secara statistik. |
| **Relevance** | 5 | Sangat relevan di bidang Sistem Informasi untuk memastikan fungsionalitas sistem berjalan selaras dengan kebutuhan *User Experience* (UX). |
| **Testability** | 5 | Bersifat *falsifiable*. Hipotesis bahwa sistem sudah "layak" bisa terbukti salah jika skor SUS ternyata jatuh di bawah standar *acceptable* (misal: di bawah 68). |
| **Impact** | 5 | Menghasilkan rekomendasi perbaikan yang nyata (*data-driven*) bagi pihak universitas, menghilangkan tebak-tebakan dalam pengembangan *update* sistem berikutnya. |

**Skor total:** **25** / 25

**Problem statement versi final (1 paragraf):**
> Fitur Kartu Hasil Studi (KHS) pada Sistem Informasi Manajemen (SIM) UPB merupakan instrumen vital bagi mahasiswa di setiap akhir semester, namun ketiadaan evaluasi usabilitas yang empiris menyebabkan kelayakan antarmuka sistem saat ini tidak diketahui secara pasti (*Empiric Gap*). Tanpa adanya pengukuran yang terstandar, keluhan pengguna terkait navigasi dan tata letak informasi hanya menjadi asumsi subjektif yang sulit ditindaklanjuti. Oleh karena itu, riset ini akan mengevaluasi tingkat usabilitas fitur KHS menggunakan instrumen *System Usability Scale* (SUS) untuk menghasilkan data kuantitatif yang mengidentifikasi hambatan interaksi secara objektif, guna merumuskan rekomendasi perbaikan berbasis data bagi pengelola akademik.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Masalah *coding* (*Engineering Problem*) seperti *bug* atau fitur yang *error* didefinisikan sebagai kegagalan sistem dalam berfungsi sesuai instruksi. Pendekatannya bersifat solutif seketika: mencari penyebab teknis di baris kode dan memperbaikinya agar sistem kembali berjalan (*solve it*). Keberhasilannya diukur dari apakah *error* tersebut hilang atau tidak.
> Sebaliknya, masalah riset (*Research Problem*) tidak selalu berarti ada yang "rusak". Masalah riset didefinisikan sebagai ketidaktahuan (*knowledge gap*)—misalnya, kita memiliki sistem akademik yang berfungsi, tapi kita tidak tahu apakah itu mudah digunakan oleh mahasiswa awam. Pendekatannya bersifat investigatif: mendesain pengukuran (seperti kuesioner SUS) untuk menghasilkan bukti empiris. Tujuan utamanya bukan untuk langsung mereparasi sistem, melainkan untuk memberikan pemahaman baru (*understand & prove it*) yang tervalidasi secara ilmiah.