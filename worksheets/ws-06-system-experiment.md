# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

`RQ → Variable → System Component → Experimental Setup → Output`

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

**SYSTEM-EXPERIMENT MAPPING**

**Research Question:** Bagaimana tingkat usabilitas fitur Kartu Hasil Studi (KHS) pada SIM UPB jika diukur menggunakan metode *System Usability Scale* (SUS) dibandingkan dengan standar *acceptable score*?

**Variable → Component Mapping:**
| Variabel | Tipe | Komponen Sistem / Instrumen | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
| Fitur KHS SIM UPB | IV | Antarmuka KHS (Sistem Berjalan) | Dibuat konstan; responden dipandu ke URL/Menu KHS yang sama. |
| Tingkat Usabilitas | DV | Instrumen Evaluasi (Google Form SUS) | Skala Likert 1-5 direkam otomatis menjadi data *spreadsheet* interval. |
| Beban Kognitif | CV | Modul Skenario Tugas (*Task Setup*) | Teks instruksi tugas dikunci (*hardcoded*) pada awal formulir. |

**4 Prinsip Desain:**
  [x] **Traceability** — Setiap instrumen pengukuran bisa ditelusuri ke variabel riset.
  [x] **Variable Isolation** — Objek (SIM UPB) terpisah dari alat ukur (Form SUS).
  [x] **Measurement Integration** — Pengukuran DV (*scoring*) rekap otomatis.
  [x] **Reproducibility** — Setup skenario dan instrumen bisa direkonstruksi kapan saja.

**Experimental Setup:**
  **Input data** : Interaksi *user* merespons pertanyaan kuesioner pasca-penggunaan sistem.
  **Parameter** : 10 Butir Pertanyaan SUS baku dengan *alternating tone* (positif/negatif).
  **Output format** : Tabel *Spreadsheet* (*.csv / .xlsx*) berisi *raw score* tiap responden.

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Bagaimana tingkat usabilitas fitur Kartu Hasil Studi (KHS) pada SIM UPB jika diukur menggunakan metode *System Usability Scale* (SUS)?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| Objek Sistem Akademik | IV | Layar Antarmuka KHS SIM UPB | Menjaga kondisi sistem agar tidak berubah selama periode pengambilan data (konstan). |
| Tingkat Usabilitas Pengguna | DV | Komponen Kuesioner SUS | Menggunakan fitur *auto-calculation* di Excel/Sheets untuk mengubah Likert 1-5 menjadi skor 0-100. |
| Kesetaraan Pengujian | CV | Skenario Instruksi Tugas (*Task*) | Instruksi baku: "Login -> Pilih Menu KHS -> Ganti Semester -> Cari Nilai IPK". |

**Apakah semua variabel bisa di-map?** [x] Ya / [ ] Tidak
> **Jika tidak, komponen apa yang perlu ditambahkan?** (Semua variabel telah berhasil dipetakan ke dalam arsitektur eksperimen observasional UI/UX).

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| **Traceability** | ✅ Terpenuhi | Variabel "Usabilitas" langsung terlacak ke instrumen 10-item SUS. |
| **Modularity** | ✅ Terpenuhi | Instrumen form SUS terpisah dari SIM UPB; jika ingin menguji fitur KRS, form tidak perlu diubah ulang. |
| **Controllability** | ⚠️ Parsial | Instruksi (CV) dapat dikunci, namun perangkat (*device/browser*) yang digunakan responden saat uji berada di luar kendali (*uncontrolled environment*). |
| **Measurability** | ✅ Terpenuhi | Skala Likert pada Google Form memberikan *output* data terstruktur (CSV) tanpa intervensi manual. |

**Prinsip mana yang paling sulit dipenuhi?** Controllability.
**Strategi untuk mengatasinya:**
> Menambahkan pertanyaan prasyarat (*screening*) di awal kuesioner untuk mengelompokkan responden berdasarkan perangkat yang digunakan (*Mobile* vs *Desktop*) sebagai data demografi tambahan untuk melacak anomali jika terjadi.

---

## Latihan 3 — Ablation Study Planning

*(Adaptasi UX Evaluation: Ablation Study dalam pengujian antarmuka diterjemahkan sebagai isolasi Skenario Tugas (Task Isolation) untuk menemukan komponen UI mana yang paling menurunkan usabilitas).*

| Kondisi (Skenario) | Komponen A (Navigasi Menu) | Komponen B (Tabel Nilai) | Komponen C (Fungsi Cetak/PDF) | Hasil yang Diharapkan |
|---------|-----------|-----------|-----------|----------------------|
| **Full Task** | ✅ (*Login & Akses*) | ✅ (*Baca Nilai & IPK*) | ✅ (*Download PDF*) | *Baseline* skor SUS gabungan seluruh fitur KHS. |
| **– A** | ❌ (*Lewati Navigasi, beri URL langsung*) | ✅ | ✅ | Menguji apakah navigasi menu/sidebar yang bikin rumit. |
| **– B** | ✅ | ❌ (*Tabel disembunyikan*) | ✅ | Menguji seberapa mudah tombol *Cetak* ditemukan tanpa distraksi tabel. |
| **– C** | ✅ | ✅ | ❌ (*Tanpa instruksi Cetak*) | Menguji kenyamanan baca tabel secara visual saja tanpa fungsi aksi. |

**Komponen mana yang diprediksi paling berkontribusi (pada penurunan skor usabilitas)?** Komponen C (Fungsi Cetak/PDF) dan Navigasi.
**Mengapa?**
> Seringkali antarmuka akademik menampilkan tabel dengan baik (Komponen B biasanya standar), namun peletakan tombol aksi (*Download/Print*) kerap tersembunyi atau menghasilkan *output* cetak yang terpotong. Mengisolasi tugas ini akan membuktikan asumsi tersebut.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Dalam konteks pengujian UI/UX, jika kita mengevaluasi sebuah sistem informasi secara monolitik (misalnya, menyuruh responden menilai "SIM UPB" secara keseluruhan tanpa isolasi fitur), kita akan mendapatkan satu skor SUS "gelondongan". Jika skornya rendah, peneliti tidak akan tahu fitur mana yang menjadi biang keroknya (apakah KHS, KRS, Profil, atau Jadwal?). 
> 
> Arsitektur yang modular (memecah instrumen pengujian berdasarkan fitur spesifik) sangat penting agar eksperimen memiliki daya telusur (*traceability*). Hal ini memungkinkan kita menemukan akar masalah (*root cause*) secara presisi dan menghasilkan rekomendasi perbaikan yang tepat sasaran, bukan sekadar asumsi buta.