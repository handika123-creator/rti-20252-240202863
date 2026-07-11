# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

> Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---|---|---|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix (Contoh Kasus):**

| Elemen | Intro | Method | Result | Discuss | Conclude |
|---|:---:|:---:|:---:|:---:|:---:|
| RQ1 | ✓ | ✓ | ✓ | ✓ | ✓ |
| RQ2 | ✓ | ✓ | ✓ | ✗ (Miss) | ✓ |
| Metrik-X | ✗ (Miss) | ✗ (Miss) | ✓ | ✗ (Miss) | ✗ (Miss) |

**Masalah pada contoh di atas:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|---|---|---|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---|---|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

**PAPER STRUCTURE CHECKLIST**

- **Title :** Evaluasi Pengalaman Pengguna pada Fitur Kartu Hasil Studi (KHS) SIM Universitas Pelita Bangsa Menggunakan System Usability Scale (SUS)
- **Target :** [ ] Jurnal  [ ] Konferensi  [x] Laporan / Tugas Akhir

**Section Check:**
  [x] Abstract — masalah, metode, hasil utama, kontribusi (max 250 kata)
  [x] Introduction — konteks → gap → RQ → kontribusi → struktur paper
  [x] Related Work — concept-centric, gap positioning
  [x] Method — reproducible: desain, variabel, metrik, setup, prosedur
  [x] Results — tabel + grafik + observasi (tanpa interpretasi)
  [x] Discussion — interpretasi, perbandingan, implikasi, limitation
  [x] Conclusion — jawaban RQ, kontribusi, future work

**Consistency Matrix:**
  [x] RQ di Introduction = RQ di Method = RQ di Conclusion
  [x] Variabel di Method = variabel di Results
  [x] Klaim di Discussion didukung data di Results
  [x] Limitasi di Discussion di-address di Conclusion/Future Work

**Writing Quality:**
  [x] Clarity — mudah dipahami tanpa re-read
  [x] Precision — tidak ada istilah ambigu
  [x] Conciseness — tidak ada kalimat redundan

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama (2-3 kalimat) | Target Kata |
|---|---|---|
| **Abstract** | Portal akademik SIM UPB krusial bagi aktivitas mahasiswa, namun fitur KHS sering memicu keluhan terkait kemudahan akses nilainya. Studi ini mengevaluasi tingkat *usability* fitur KHS menggunakan instrumen System Usability Scale (SUS) yang disebar secara acak terkontrol kepada 30 mahasiswa aktif pengguna portal. Hasil analisis kuantitatif menghasilkan rata-rata skor SUS sebesar 63.33, yang menunjukkan kualitas antarmuka berada di bawah batas kelayakan kelulusan global (> 68.0). | 200-250 |
| **Introduction** | Konteks: Pentingnya portal akademik digital dalam ekosistem kampus modern untuk efisiensi informasi nilai. Gap: Evaluasi mandiri terhadap antarmuka spesifik KHS SIM UPB belum pernah terdokumentasi secara empiris di tengah keluhan mahasiswa di lapangan. RQ: Bagaimana tingkat *usability* serta kenyamanan interaksi pengguna pada fitur KHS SIM UPB jika diukur dengan instrumen standar? | 500-700 |
| **Related Work** | Tinjauan terhadap studi terdahulu mengenai evaluasi sistem informasi kampus menggunakan SUS. Penjabaran posisi penelitian yang memfokuskan amatan pada sub-modul transaksional (KHS) daripada penilaian portal secara menyeluruh untuk presisi rekomendasi perbaikan. | 700-1000 |
| **Method** | Eksperimen berbasis pengujian survei terkontrol dengan skenario tugas instruksional (mengakses nilai semester). Menggunakan instrumen baku kuesioner SUS 10-item berskala Likert 1-5 dengan melibatkan 30 responden riil lewat *purposive sampling*. Analisis inferensial dijalankan dengan metode *One-Sample T-Test* menggunakan skrip Python. | 800-1200 |
| **Results** | Penyajian tabel deskriptif data mentah respons pengguna dan ringkasan konversi skor SUS individual (Min: 40.0, Max: 90.0, Median: 66.25). Menampilkan grafik histogram 2D visualisasi sebaran frekuensi data yang memperlihatkan konsentrasi skor mayoritas sampel di bawah 68.0. | 500-800 |
| **Discussion** | Interpretasi atas rata-rata skor final 63.33 yang masuk dalam kategori *Marginal Passive* dengan peringkat *OK/Poor*. Analisis kualitatif terhadap kolom kritik/saran mengungkap kendala utama ada pada responsivitas tabel di *mobile screen*. Pembahasan limitasi sampel riset kuantitatif skala kecil (n=30). | 600-900 |
| **Conclusion** | Kesimpulan tegas menjawab RQ bahwa fitur KHS SIM UPB belum mencapai target kelayakan *usability*. Kontribusi riset berupa penyediaan data empiris pertama bagi tim developer internal kampus untuk melakukan *redesign* berbasis hierarki informasi. | 200-400 |

---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

| Elemen Riset | Intro | Method | Result | Discussion | Conclusion |
|---|:---:|:---:|:---:|:---:|:---:|
| RQ1: Tingkat Usability KHS | ✓ | ✓ | ✓ | ✓ | ✓ |
| Metrik Utama: Skor SUS | ✓ | ✓ | ✓ | ✓ | ✓ |
| Variabel IV: Desain Antarmuka KHS | ✓ | ✓ | ✓ | ✓ | ✓ |
| Variabel DV: Skor Sikap Pengguna | ✓ | ✓ | ✓ | ✓ | ✓ |
| Temuan: Skor Rata-rata 63.33 | ✗ | ✗ | ✓ | ✓ | ✓ |
| Rekomendasi: Perbaikan UI Mobile | ✗ | ✗ | ✗ | ✓ | ✓ |

- **Isi setiap sel:** ✓ (ada & konsisten), ✗ (missing), ~ (ada tapi inkonsisten)

**Inkonsistensi yang ditemukan:**
> Tidak ditemukan inkonsistensi fatal. Temuan skor (63.33) dan rekomendasi perbaikan UI secara logis memang tidak boleh muncul di bagian Introduction dan Method karena merupakan produk luaran dari hasil analisis data di bagian akhir.

**Tindakan perbaikan:**
> Menjaga penulisan istilah agar tetap seragam sepanjang bab (misal: konsisten menggunakan istilah "fitur KHS", bukan berganti menjadi "menu nilai akademik" secara tiba-tiba).

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> Dari hasil survei yang disebarkan kemarin ke teman-teman mahasiswa diperoleh data respons kuesioner di mana nilainya setelah dihitung pakai rumus SUS rata-ratanya ketemunya cuma 63.33. Angka ini lumayan jelek dan kurang memuaskan karena target awal kita kan maunya lulus di atas 68 sesuai teori dari buku. Jadi bisa dibilang aplikasinya masih membingungkan buat user.

| Kriteria | Evaluasi | Perbaikan |
|---|---|---|
| **Clarity** | Kalimat terlalu kasual dan mencampurkan proses pengumpulan serta hasil dalam satu nafas kalimat panjang. | Memisahkan kalimat proses dengan kalimat kesimpulan numerik secara bertahap. |
| **Precision** | Istilah "kemarin", "teman-teman", "lumayan jelek", dan "sesuai teori dari buku" sangat tidak ilmiah dan ambigu. | Mengubah menjadi bahasa baku akademik: menyebut jumlah responden, nama instrumen, p-value, dan referensi pustaka resmi. |
| **Conciseness** | Banyak kata pengisi (*filler words*) seperti "kan maunya", "ketemunya cuma", dan "bisa dibilang". | Menghapus kata pengisi untuk langsung menembak fokus poin kesimpulan data. |

**Paragraf setelah perbaikan:**
> Analisis data terhadap 30 responden mahasiswa aktif menghasilkan nilai rata-rata (*mean*) skor akhir System Usability Scale (SUS) sebesar 63.33 dengan standar deviasi 11.75. Berdasarkan pengujian inferensial *One-Sample T-Test*, skor tersebut secara statistik terbukti signifikan berada di bawah batas ambang kelayakan global sebesar 68.0 (p < 0.05). Hasil evaluasi empiris ini mengindikasikan bahwa antarmuka fitur KHS SIM UPB saat ini masih menghadapi kendala *usability* yang nyata dalam interaksi pengguna.

---

## Refleksi

> **Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?**

Menulis "tentang" riset cenderung bersifat deskriptif-naratif layaknya sebuah diari atau laporan kronologis biasa, di mana fokusnya hanya menceritakan apa saja langkah yang sudah dilakukan peneliti tanpa bobot kritis. Sebaliknya, menulis sebagai sebuah "argumen" riset adalah membangun jembatan logika yang kokoh demi meyakinkan pembaca. Dalam riset KHS ini, argumennya adalah pembuktian ilmiah bahwa sistem memiliki masalah interaksi riil, yang didukung secara empiris lewat penolakan hipotesis baku oleh angka statistik.

Menerapkan urutan penulisan non-linear (Method & Results → Discussion → Introduction) sangat mengubah kualitas tulisan menjadi jauh lebih objektif. Jika saya memaksakan menulis Introduction di awal sebelum data terkumpul, saya akan terjebak bias kognitif untuk mencocok-cocokkan narasi latar belakang agar mendukung asumsi pribadi. Dengan menulis Method dan Results terlebih dahulu, saya memegang kebenaran data mentah yang kokoh sebagai jangkar berpikir. Baru kemudian saya bisa membingkai narasi Introduction secara jujur, akurat, dan tajam berdasarkan realitas temuan di lapangan.