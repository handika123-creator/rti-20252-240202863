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
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Sistem Informasi Akademik / Desain UI/UX.
  Konteks  : Perancangan antarmuka aplikasi My CIC dari platform berbasis web menjadi mobile device menggunakan software Figma.

System Context
  Input       : Interaksi pengguna (mahasiswa) saat mencari informasi akademik seperti biodata, nilai, jadwal kuliah, atau KRS.
  Process     : Navigasi antarmuka (user flow) dalam mencari dan memproses informasi akademik melalui tombol dan menu yang dirancang.
  Output      : Tampilan visual informasi akademik mahasiswa secara lengkap dan terstruktur pada layar smartphone.
  Outcome     : Mahasiswa merasa lebih nyaman, mudah, dan tidak kebingungan saat menggunakan layanan informasi akademik My CIC.
  Constraints : Solusi yang dirancang sebatas purwarupa (prototype) visual, menargetkan audiens mahasiswa Universitas Catur Insan Cendekia secara spesifik, dan wajib berbasis mobile.
  Stakeholders: Mahasiswa sebagai pengguna utama dan Universitas Catur Insan Cendekia sebagai penyedia layanan.

Fenomena → Problem
  Fenomena yang diamati             : Tingkat kunjungan mahasiswa ke website My CIC hanya meningkat pada saat-saat tertentu saja.
  Gejala (symptom) yang terukur     : Terdapat keluhan dari beberapa mahasiswa bahwa tampilan antarmuka membosankan, kurang menarik, dan beberapa menu/tombol tidak dipahami.
  Masalah yang didiagnosis          : Sistem saat ini masih berbasis web (bukan mobile), desain UI kurang efektif/efisien, serta fitur akademik yang disajikan tidak lengkap (misal: belum ada KRS dan jadwal kuliah).
  Masalah riset (researchable)      : Bagaimana merancang purwarupa (prototype) aplikasi My CIC berbasis mobile device dengan UI/UX yang lebih terstruktur, menarik, dan memenuhi kebutuhan kelengkapan informasi akademik mahasiswa?
  Variabel yang terukur             : Kualitas elemen antarmuka (UI) dan kemudahan/kenyamanan pengalaman pengguna (UX) dalam mengakses menu.

Problem Quality Check
  [x] Clarity — Apakah satu orang membaca akan paham?
  [ ] Measurability — Apakah ada metrik kuantitatif?
  [x] Relevance — Apakah penting untuk domain?
  [x] Testability — Apakah bisa gagal?
  [x] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
  Layanan informasi akademik My CIC saat ini masih berbasis web dan memiliki antarmuka yang kurang efektif, membosankan, serta memiliki beberapa tombol navigasi yang tidak dipahami oleh pengguna. Kondisi ini diperparah dengan tidak lengkapnya fitur administrasi penting seperti Kartu Rencana Studi (KRS) dan jadwal kuliah, yang berujung pada minimnya tingkat kunjungan mahasiswa di luar periode tertentu. Oleh karena itu, penelitian ini bertujuan merancang prototype aplikasi My CIC berbasis mobile device menggunakan Figma untuk menghasilkan solusi antarmuka (UI/UX) yang lebih modern, minimalis, lengkap, dan nyaman digunakan oleh mahasiswa Universitas Catur Insan Cendekia.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

**Topik awal:** Perancangan Antarmuka Aplikasi Akademik Mobile.

| Tahap | Hasil |
|-------|-------|
| Reality | Website My CIC kurang aktif dikunjungi oleh mahasiswa. |
| Observed Issue (Symptom) | Mahasiswa menganggap website membosankan dan bingung dengan beberapa tombol di dalamnya. |
| Diagnosed Problem (Root Cause) |Layanan belum adaptif untuk mobile device dan informasi yang disajikan (seperti administrasi keuangan dan KRS) tidak lengkap. |
| Researchable Problem |Bagaimana cara merancang desain antarmuka aplikasi sistem informasi berbasis mobile yang sesuai dengan kebutuhan mahasiswa Universitas Catur Insan Cendekia? |
| Measurable Variable |Kualitas pengalaman pengguna (UX) dan kejelasan visual elemen desain (UI).|

**Apakah terjebak solution-first thinking?** [x] Ya / [ ] Tidak
> Jika ya, kembali ke tahap mana? Kembali ke tahap Diagnosed Problem ke Researchable Problem. Jurnal ini sejak awal (bahkan di judul) langsung memaksakan "Menggunakan Aplikasi Figma" sebagai solusinya. Seharusnya, dalam riset, kita mencari solusi/metode perancangan terbaik (misal UCD atau Design Thinking) dan membuktikan efektivitas desainnya, bukan sekadar mendeklarasikan alat editing apa yang dipakai.

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Aksi interaktif pengguna seperti memasukkan data login atau menekan tombol navigasi menu. |
| Process |Pengorganisasian alur informasi dari halaman utama menuju detail akademik seperti KRS atau ujian online.|
| Output |Representasi visual (teks, tata letak grafis, warna) dari data akademik pada layar smartphone.|
| Outcome |Terciptanya interaksi dengan website/mobile apps yang mudah, menyenangkan, dan berguna bagi mahasiswa.|
| Constraints |Penelitian dibatasi hanya pada tahap pembuatan prototype desain visual menggunakan Figma.|
| Stakeholders |Mahasiswa sebagai target audiens dan institusi kampus (Universitas CIC).|

**Komponen mana yang paling relevan dengan masalah riset?** Output (tampilan antarmuka yang modern) dan Outcome (kenyamanan/kemudahan penggunaan).

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 4 |Akar masalah (UI buruk dan fitur kurang) serta solusi (mobile prototype) dijabarkan dengan sangat jelas.|
| Measurability |2|Jurnal tidak mengukur perbaikan desain secara statistik/metrik pasti. Klaim "menarik" dan "minimalis" sangat subjektif.|
| Relevance |5|Mengembangkan UI layanan akademik sangat krusial bagi digitalisasi institusi pendidikan.|
| Testability |3|Desain bisa diuji (falsifiable) ke mahasiswa, meski jurnal ini berhenti hanya sampai menampilkan gambar hasil desain.|
| Impact |4|Penyelesaian masalah ini secara langsung mempermudah urusan administrasi mahasiswa kampus tersebut.|

**Skor total:** 18 / 25

**Problem statement versi final (1 paragraf):**
> Layanan informasi akademik My CIC saat ini masih berbasis web dan memiliki antarmuka yang kurang efektif, membosankan, serta memiliki beberapa tombol navigasi yang tidak dipahami oleh pengguna. Kondisi ini diperparah dengan tidak lengkapnya fitur administrasi penting seperti Kartu Rencana Studi (KRS) dan jadwal kuliah, yang berujung pada minimnya tingkat kunjungan mahasiswa di luar periode tertentu. Oleh karena itu, penelitian ini bertujuan merancang prototype aplikasi My CIC berbasis mobile device menggunakan Figma untuk menghasilkan solusi antarmuka (UI/UX) yang lebih modern, minimalis, lengkap, dan nyaman digunakan oleh mahasiswa Universitas Catur Insan Cendekia.
---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Masalah engineering (seperti bug kode atau server error) memiliki batasan yang sangat jelas: sesuatu tidak berfungsi sebagaimana mestinya, dan tujuannya adalah memperbaikinya agar sistem berjalan (solve). Pendekatannya bersifat teknis dan solutif seketika. Sebaliknya, masalah riset (seperti "mengapa mahasiswa kebingungan melihat menu") adalah tentang celah pengetahuan (knowledge gap). Tujuannya bukan sekadar memperbaiki tombol, melainkan membuktikan dan memahami mengapa tata letak tertentu lebih efektif secara kognitif dibandingkan yang lain (understand & prove). Dalam riset UI/UX, kita memvalidasi interaksi manusia dengan sistem secara sistematis, bukan sekadar menambal kode yang rusak.