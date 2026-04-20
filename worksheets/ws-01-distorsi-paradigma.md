# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (DSR). Penting untuk membedakan keduanya:

| Paradigma | Cara Kerja | Contoh di TI |
|-----------|-----------|---------------|
| **Positivis** | Uji hipotesis dengan eksperimen terkontrol | Apakah CNN lebih akurat dari RF pada dataset X? |
| **Design Science Research** | Bangun artefak (sistem/model/framework) untuk menguji proposisi | Dapatkah arsitektur hybrid CNN+LSTM membuktikan peningkatan recall ≥5%? |
| **Interpretivis** | Pahami makna melalui konteks & kualitatif | Bagaimana peneliti manafsirkan anomali data sensor IoT? |

Dalam DSR, artefak **bukan tujuan akhir** — ia adalah instrumen untuk menghasilkan pengetahuan. Pertanyaan riset tetap harus difalsifikasi.

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : HANDIKA DWI ARDIYANTO
Tanggal          : 20/04/2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Bagaimana karakteristik responden atau sampel mahasiswa yang digunakan untuk menguji validitas desain tersebut, dan apakah instrumen pengukurannya (seperti kuesioner) sudah teruji reliabilitasnya?
   - Data yang dibutuhkan untuk verifikasi: Skor System Usability Scale (SUS) dari pengguna, data perbandingan waktu pengerjaan tugas (time on task) antara sistem lama dan sistem baru, serta rincian demografi responden.

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [ ] Interpretivis  [x] Design Science  [ ] Mixed
   - Alasan: Riset ini berfokus pada pembuatan artefak berupa prototype desain aplikasi mobile menggunakan Figma untuk memberikan solusi praktis atas permasalahan layanan informasi akademik.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Peneliti berasumsi bahwa mengubah platform dari berbasis web ke mobile device secara otomatis akan meningkatkan intensitas kunjungan dan pemahaman mahasiswa terhadap informasi akademik.
   - Sumber bias potensial: Selection bias saat wawancara awal, di mana keluhan "kurang menarik dan membosankan" mungkin hanya mewakili opini segelintir mahasiswa dan bersifat sangat subjektif.
   - Langkah mitigasi: Melakukan pengujian usabilitas secara formal kepada kelompok mahasiswa yang lebih luas dan menggunakan metrik standar (seperti SUS) untuk mengubah opini kualitatif menjadi data kuantitatif yang objektif.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Hasil umpan balik negatif dari pengguna mengenai kekurangan prototype dan data statistik jumlah pengunjung website My CIC yang sebenarnya.
   - Batasan yang diakui sejak awal: Penelitian ini hanya terbatas pada perancangan desain UI/UX (prototype) dan tidak mencakup implementasi pengkodean (coding) atau integrasi basis data secara nyata. 
```

---

## Latihan 1 — Identifikasi Distorsi

analisis mendalam terhadap jurnal "Perancangan UI/UX My CIC".

**Paper yang dipilih:**
> Judul: Perancangan UI/UX Aplikasi My CIC Layanan Informasi Akademik Mahasiswa Menggunakan Aplikasi Figma
> Penulis (Tahun): M. Agus Muhyidin, Muhammad Afif Sulhan, Agus Sevtiana (2020)
> Sumber/Link DOI: JURNAL DIGIT Vol. 10, No.2

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengumpulkan keluhan mahasiswa melalui wawancara mengenai tampilan website yang membosankan dan informasi yang kurang lengkap. | Sampling Bias: Peneliti hanya mengambil data dari "beberapa mahasiswa" , sehingga tidak merepresentasikan populasi seluruh mahasiswa Universitas CIC. |
| Data → Processing |Mengelompokkan masalah ke dalam kategori desain antarmuka (UI) yang kurang menarik dan fitur yang belum lengkap (seperti KRS, jadwal, dan nilai).|Confirmation Bias: Peneliti mengarahkan masalah agar bisa diselesaikan melalui desain (Figma), mengabaikan kemungkinan masalah pada backend sistem.|
| Processing → Analysis |Menggunakan elemen desain (warna, tipografi, ukuran) untuk merancang solusi visual yang minimalis dan modern.|Halo Effect: Adanya asumsi bahwa desain yang terlihat "modern" secara otomatis meningkatkan kinerja dan kualitas pelayanan tanpa pengujian metrik.|
| Analysis → Inference |Merumuskan bahwa solusi masalah adalah dengan merancang prototype aplikasi berbasis mobile device.|Asumsi Kausalitas: Peneliti menyimpulkan bahwa aplikasi mobile adalah solusi mutlak untuk meningkatkan kunjungan, tanpa membandingkan jika web yang diperbaiki sudah cukup.|
| Inference → Knowledge |Menyimpulkan bahwa Figma efektif untuk mendesain tampilan aplikasi My CIC yang menarik dan modern sesuai kebutuhan mahasiswa.|Overgeneralization: Pengetahuan yang dihasilkan baru sebatas kemampuan alat desain, bukan efektivitas nyata aplikasi terhadap performa akademik mahasiswa.|

**Distorsi paling besar di tahap:** Reality → Data dan Inference → Knowledge.
**Dua distorsi spesifik yang teridentifikasi:**
1. Selection Bias pada Data Awal: Peneliti mendasarkan seluruh perancangan pada wawancara dengan "beberapa mahasiswa" tanpa rincian jumlah responden, sehingga data ketidakpuasan bersifat sangat subjektif dan rawan bias.
2. Ketiadaan Validitas Eksternal (Usability Testing): Meskipun menghasilkan prototype , penelitian ini tidak menyertakan pengujian pengguna secara formal (seperti kuesioner SUS) untuk membuktikan secara ilmiah bahwa desain baru lebih mudah dipahami daripada desain lama.

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Peneliti harus tetap melaporkan keberadaan outlier tersebut karena dalam riset UI/UX, outlier sering kali mewakili pengguna dengan kebutuhan khusus atau hambatan teknis yang nyata. Menghapus data ini tanpa penjelasan logis berarti mengabaikan realitas pengalaman pengguna. |
| Transparansi |Peneliti wajib memaparkan hasil desain sebelum dan sesudah data tersebut diolah, serta memberikan alasan teknis mengapa outlier itu muncul (misalnya: anomali pada perangkat mahasiswa atau kesalahan saat pengisian instrumen).|
| Peer review |Dengan menyajikan data secara utuh, penguji atau penelaah jurnal dapat memvalidasi apakah solusi desain yang ditawarkan benar-benar inklusif untuk semua mahasiswa atau hanya efektif untuk kelompok mayoritas saja.|

**Keputusan akhir dan justifikasi:**
> Peneliti harus melaporkan kedua versi hasil tersebut. Dalam pengembangan aplikasi pendidikan seperti My CIC, data outlier sangat berharga untuk mengidentifikasi pain points ekstrem yang mungkin tidak dirasakan pengguna lain. Menghapus data hanya demi signifikansi statistik melanggar prinsip objektivitas dan menghambat pengembangan fitur yang benar-benar solutif bagi seluruh civitas akademika.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Perancangan UI/UX Aplikasi My CIC Layanan Informasi Akademik Mahasiswa Menggunakan Aplikasi Figma.

> **Skala 1–5:** 1 = tidak sesuai sama sekali dengan topik ini, 5 = sangat sesuai dan dominan digunakan pada riset bertopik serupa.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 3 — Sesuai jika riset bertujuan menguji hipotesis efisiensi sistem melalui angka atau statistik. | 4 — Sesuai karena riset ini diawali dengan menggali persepsi mahasiswa mengenai tampilan yang "membosankan". | 5 — Sangat sesuai karena fokus utama riset adalah membangun artefak (prototype aplikasi) untuk memecahkan masalah. |
| Jenis data yang dikumpulkan | Metrik kuantitatif seperti jumlah pengunjung website atau skor kuesioner. | Hasil wawancara mengenai pengalaman subjektif dan pemahaman mahasiswa terhadap tombol/menu | Dokumentasi perancangan, elemen visual UI, alur kerja desain (workflow), dan purwarupa sistem. |
| Limitasi paradigma |Angka statistik tidak mampu menjelaskan secara mendalam alasan psikologis di balik ketidakpuasan pengguna.|Temuan riset sangat bergantung pada konteks subjektif mahasiswa Universitas CIC sehingga sulit digeneralisasi. |Artefak yang dihasilkan (prototype) belum tentu diimplementasikan secara teknis pada sistem backend universitas.|

**Paradigma yang dipilih:** Design Science Research (DSR).
**Alasan:** Riset ini mengedepankan proses penciptaan sebuah artefak teknologi informasi berupa rancangan desain UI/UX mobile apps My CIC sebagai solusi atas masalah tampilan dan kelengkapan informasi pada platform web sebelumnya. Melalui paradigma ini, desain yang dibuat (Figma) berfungsi sebagai instrumen untuk menghasilkan pengetahuan baru mengenai kebutuhan antarmuka mahasiswa.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Sebelum mempelajari materi tentang rantai distorsi ini, saya cenderung menerima klaim seperti "desain ini lebih menarik dan modern" atau "aplikasi ini 100% lebih baik" secara mentah-mentah, terutama jika tampilan visual rancangannya (seperti pada Figma) memang terlihat memanjakan mata. Saya sering kali terjebak pada Halo Effect, di mana tampilan yang bagus dianggap otomatis menyelesaikan masalah usability tanpa mempertanyakan asal-usul kesimpulan tersebut.

> Namun, setelah memahami bagaimana data bisa mengalami distorsi di setiap tahapannya—dari Reality hingga menjadi Knowledge—pola pikir saya sebagai peneliti berubah. Sekarang, setiap kali membaca paper yang mengklaim keberhasilan sebuah metode atau desain, pertanyaan utama yang akan langsung saya ajukan adalah:

      "Mana bukti objektifnya?" (Apakah klaim "mudah digunakan" ini dibuktikan dengan metrik yang valid seperti System Usability Scale (SUS), atau hanya opini subjektif peneliti?)

      "Siapa yang mengujinya?" (Apakah sampel pengujian terhindar dari Sampling Bias? Berapa banyak respondennya dan apakah mereka merepresentasikan end-user yang sebenarnya?)

      "Apakah ada asumsi tersembunyi?" (Apakah ada faktor lain yang membuat sistem lama terlihat buruk yang sengaja tidak disebutkan untuk menonjolkan sistem baru?)