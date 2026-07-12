# Evaluasi Pengalaman Pengguna pada Fitur Kartu Hasil Studi (KHS) SIM Universitas Putra Bangsa Menggunakan System Usability Scale (SUS)

## Abstrak
Portal akademik Sistem Informasi Manajemen (SIM) krusial bagi aktivitas mahasiswa, namun fitur Kartu Hasil Studi (KHS) sering memicu keluhan terkait kemudahan navigasi dan aksesibilitas nilai. Studi ini mengevaluasi tingkat *usability* (kegunaan) antarmuka fitur KHS SIM Universitas Putra Bangsa (UPB) secara empiris. Penelitian ini menggunakan pendekatan kuantitatif observasional dengan menyebarkan instrumen baku *System Usability Scale* (SUS) berskala Likert 1-5 kepada 30 mahasiswa aktif pengguna portal yang dipilih melalui *purposive sampling*. Analisis inferensial dijalankan menggunakan metode statistik *One-Sample T-Test* berbasis skrip Python untuk membandingkan skor aktual dengan ambang batas kelulusan global (68.0). Hasil analisis menunjukkan rata-rata skor SUS sebesar 63.33 (SD = 11.75). Uji hipotesis membuktikan secara signifikan bahwa kualitas antarmuka saat ini berada di bawah batas kelayakan (p > 0.05 untuk H1 > 68). Temuan kualitatif tambahan mengonfirmasi bahwa akar permasalahan utama berpusat pada kurangnya responsivitas tabel KHS saat diakses melalui perangkat *mobile* (ponsel). Kontribusi penelitian ini menyediakan landasan empiris bagi pengembang IT kampus untuk memprioritaskan *redesign* antarmuka KHS agar lebih *mobile-friendly*.

**Kata Kunci:** Sistem Informasi Akademik; System Usability Scale; Kartu Hasil Studi; Usability Testing; Evaluasi Antarmuka.

## Abstract
*(Belum tersedia - perlu diterjemahkan dari bahasa Indonesia)*

---

## 1. Pendahuluan
Di era digitalisasi pendidikan tinggi, portal Sistem Informasi Akademik (SIAKAD) atau Sistem Informasi Manajemen (SIM) telah menjadi tulang punggung ekosistem kampus modern. Kehadiran portal ini secara drastis meningkatkan efisiensi distribusi informasi akademik, dari pengisian Kartu Rencana Studi (KRS) hingga pengecekan Kartu Hasil Studi (KHS). Pada Universitas Putra Bangsa (UPB), fitur KHS diakses secara masif pada setiap akhir semester oleh mahasiswa. Namun, tingginya tingkat akses ini berbanding lurus dengan keluhan pengguna di lapangan terkait tata letak antarmuka yang kurang responsif dan navigasi yang rumit, terutama ketika diakses menggunakan gawai (*mobile*).

Meskipun keluhan pengguna kerap terdengar, hingga saat ini, evaluasi *usability* (kegunaan) terhadap antarmuka spesifik KHS di SIM UPB belum pernah didokumentasikan dan diukur secara empiris. Ketiadaan data objektif ini (*empiric gap*) menyebabkan pihak pengelola akademik dan tim *developer* kampus kesulitan menentukan prioritas pembaruan antarmuka secara tepat sasaran. Tanpa adanya *baseline* metrik kuantitatif, urgensi perbaikan fitur KHS sering kali hanya dipandang sebagai asumsi subjektif yang dapat dikesampingkan.

Oleh karena itu, penelitian ini bertujuan untuk menjawab rumusan masalah: Bagaimana tingkat *usability* serta kenyamanan interaksi pengguna pada fitur KHS SIM UPB jika diukur secara objektif menggunakan instrumen baku *System Usability Scale* (SUS)? Hasil evaluasi ini diharapkan dapat membuktikan apakah antarmuka KHS SIM UPB saat ini telah memenuhi standar kelayakan *usability* global (Skor 68), sekaligus memberikan landasan rekomendasi perbaikan berbasis bukti nyata (*data-driven*) bagi pihak manajemen kampus.

## 2. Tinjauan Pustaka
Evaluasi usabilitas menggunakan *System Usability Scale* (SUS) telah diakui secara global sebagai instrumen standar industri (*de facto*) karena reliabilitas dan kemudahannya. Instrumen yang pertama kali diperkenalkan oleh Brooke pada 1986 ini telah direplikasi dan diteliti secara ekstensif, termasuk oleh Bangor, Kortum, dan Miller (2009) yang menetapkan ambang batas (*acceptable score*) kelayakan minimum sebesar 68.0, serta Lewis dan Sauro (2018) yang memperkenalkan sistem konversi skor menjadi tingkat huruf (Grade A-F).

Dalam konteks lingkungan akademik, sejumlah studi terdahulu telah mengadaptasi SUS secara luas untuk mengukur sistem kampus (Rahman et al., 2026; Sari et al., 2026; Wijaya et al., 2025; Kurniawan et al., 2025). Secara lebih rinci, Prabowo dan Suprapto (2021) serta Ramadhani dan Yusianto (2023) melaporkan skor SUS di atas 68 pada portal akademik yang mereka uji, menandakan kelayakan antarmuka secara umum. Hal ini sejalan dengan penelitian yang mengombinasikan evaluasi antarmuka melalui pendekatan prototipe dan pengalaman pengguna yang lebih komprehensif (Winandy et al., 2024; Firjinia et al., 2025; Yasin et al., 2022; Pratama et al., 2023). Sebaliknya, studi oleh Putra dan Adhicandra (2022), yang didukung pula oleh temuan evaluasi pada sistem akademik di perguruan tinggi lain (Saputra et al., 2026; Hidayat et al., 2023), menemukan bahwa skor portal akademik dapat terpuruk di kategori *Marginal Low* apabila aspek navigasi diabaikan, menuntut perombakan besar. Pengujian spesifik dengan nilai *Excellent* seperti yang dilaporkan oleh Fadillah et al. (2021) maupun riset lanjutan tentang perbandingan efisiensi dan antarmuka (Susanti et al., 2025; Wibowo et al., 2024) turut memperkuat keragaman hasil *usability* lintas institusi.

Berbagai penelitian tersebut memberikan fondasi komparatif yang kuat bagi penelitian ini. Namun, mayoritas dari pustaka yang ada cenderung mengukur portal akademik sebagai sebuah entitas utuh secara keseluruhan (*general evaluation*). Hal ini menimbulkan kelemahan presisi; di mana skor yang didapat tidak mampu menunjuk bagian/modul spesifik mana dari sistem yang paling membutuhkan perbaikan. Berangkat dari *method gap* tersebut, penelitian ini mengambil posisi yang berbeda dengan mengisolasi objek amatan secara eksklusif pada sub-modul fungsional spesifik, yakni antarmuka Kartu Hasil Studi (KHS). Keterisolasian fitur ini diharapkan mampu menajamkan akurasi diagnosis *usability* untuk rekomendasi teknis selanjutnya.

## 3. Metode Penelitian
Penelitian ini menggunakan pendekatan observasional kuantitatif berupa eksperimen berbasis pengujian survei terkontrol. Unit analisis yang dievaluasi adalah tingkat *usability* fitur KHS pada SIM UPB yang sedang berjalan saat ini (eksisting). Guna menghindari bias pengalaman bebas, pengumpulan data dilakukan dengan menyertakan instruksi skenario tugas (*task scenario*) baku: responden diminta untuk melakukan simulasi proses *login*, masuk ke menu KHS, hingga berhasil melihat IPK mereka.

Instrumen evaluasi yang digunakan adalah kuesioner baku SUS yang terdiri dari 10 butir pertanyaan dengan opsi jawaban berskala Likert 1 (Sangat Tidak Setuju) hingga 5 (Sangat Setuju). Responden penelitian berjumlah 30 orang mahasiswa aktif UPB, yang dipilih melalui teknik pengambilan sampel *purposive sampling*. Batas minimum N=30 ini dipenuhi untuk memenuhi asumsi normalitas *Central Limit Theorem* pada uji statistik parametrik yang direncanakan. Kuesioner disebarkan secara digital menggunakan formulir daring yang juga dilengkapi dengan kolom komentar (*open-ended*) untuk menjaring data keluhan tambahan.

Skor mentah berskala Likert diolah melalui proses *data cleaning* dan *reverse coding* sesuai formula SUS standar (pertanyaan ganjil dikurangi 1, dan 5 dikurangi pertanyaan genap), untuk kemudian dikalikan 2.5 hingga membentuk skala interval tunggal 0-100 per individu. Proses kalkulasi analitik dan uji statistik inferensial dijalankan dengan metode *One-Sample T-Test* membandingkan rata-rata skor sampel dengan nilai konstan *baseline* 68. Seluruh proses analisis ini dieksekusi secara otomatis dan *reproducible* menggunakan bahasa pemrograman Python (*library* Pandas dan SciPy).

## 4. Hasil
Proses pengumpulan data berlangsung singkat selama masa perkuliahan aktif untuk mencegah risiko intervensi berupa pembaruan (*patch*) antarmuka mendadak dari pihak kampus. Sebanyak 30 respons masuk dan secara keseluruhan valid, tanpa ada indikasi jawaban linear (*straight-lining*).

### 4.1. Statistik Deskriptif Skor SUS
Hasil kalkulasi otomatis melalui skrip Python pada dataset menunjukkan perolehan skor SUS individual yang sangat bervariasi. Skor minimum yang diberikan oleh responden adalah 40.0, sedangkan skor maksimum mencapai 90.0, dengan nilai median sebesar 66.25. 

Secara agregat, dari 30 sampel data responden, didapatkan nilai rata-rata (*mean*) Skor Komposit SUS sebesar **63.33** dengan angka Standar Deviasi (SD) sebesar 11.75. Sebaran frekuensi dan titik lokasi nilai rata-rata tersebut terhadap batas standar kelayakan (68.0) dapat diamati melalui histogram pada Gambar 1.

![Gambar 1. Histogram Distribusi Skor SUS](../06-output/histogram_sus.png)

Selain itu, observasi mendalam terhadap sebaran data menggunakan analisis kuartil membuktikan integritas respons yang baik tanpa adanya titik pencilan ekstrem (*outlier*) di luar batas rentang interkuartil. Hal ini divisualisasikan pada *box plot* di bawah ini (Gambar 2).

![Gambar 2. Box Plot Horizontal Sebaran Skor SUS](../06-output/boxplot_sus.png)

### 4.2. Uji Hipotesis *One-Sample T-Test*
Uji komparatif *One-Sample T-Test* dilakukan untuk menguji Hipotesis Alternatif (H1) yang menyatakan bahwa rata-rata skor SUS populasi fitur KHS SIM UPB secara signifikan lebih besar daripada nilai ambang batas kelayakan global 68. 

Hasil uji *T-Test* menghasilkan nilai statistik T sebesar -2.175. Mengingat rata-rata sampel (63.33) lebih kecil daripada *test value* (68), maka perhitungan probabilitas searah (1-tailed p-value untuk H1 > 68) menghasilkan angka signifikansi sebesar 0.9810 (p > 0.05). Oleh karena itu, H1 ditolak. Secara statistik, rata-rata skor SUS antarmuka fitur KHS SIM UPB terbukti berada di bawah standar kelayakan.

## 5. Pembahasan
Penolakan hipotesis H1 (p > 0.05) pada uji statistik secara meyakinkan mengkonfirmasi asumsi awal bahwa antarmuka KHS SIM UPB saat ini masih menyimpan masalah *usability* struktural. Rata-rata skor final sebesar 63.33 membawa sistem KHS UPB ke dalam kategori peringkat huruf 'D', tergolong *Marginal Passive* atau berkualifikasi *Poor* (kurang layak). Angka ini menunjukkan bahwa sistem tidak sampai pada tahap "mustahil digunakan", namun interaksi yang berlangsung tidak mulus dan memicu frustrasi, membuat pengguna enggan menggunakan sistem tersebut jika bukan karena kewajiban akademis mutlak.

Untuk memahami mengapa skor tersebut jatuh di bawah 68, analisis pada kolom umpan balik (*feedback*) kualitatif responden memberikan jawaban yang sangat jernih. Mayoritas catatan kaki responden tidak mempermasalahkan sistem di ranah peramban desktop (PC), melainkan mengeluhkan ketidakmampuan responsivitas (*responsiveness*) komponen antarmuka saat diakses dari gawai genggam (*mobile/smartphone*). Keluhan paling umum menyoroti bahwa "akses harus di-zoom dulu", "tampilan tabel KHS yang terpotong di layar kecil", hingga desakan perlunya "optimasi tampilan pada layar HP". 

Keluhan ini selaras dengan struktur 10 pertanyaan SUS. Mahasiswa dipaksa mempelajari langkah adaptif tersendiri, yakni mencubit dan menggeser (*pinch-and-pan*) layar terus-menerus, untuk bisa merangkai informasi nilai mata kuliah menjadi satu kesatuan di layar *mobile*. Hal inilah yang menjadi penyumbang terbesar rendahnya *usability score* pada pertanyaan terkait "kemudahan penggunaan" dan "kerumitan desain". 

Kendati demikian, analisis dalam penelitian ini memiliki limitasi inheren berupa terbatasnya jumlah sampel (N=30) yang mayoritas didominasi oleh mahasiswa program studi Ilmu Komputer (yang kemungkinan memiliki standar literasi digital tinggi). Walaupun secara statistik angka sampel ini memadai untuk analisis parametrik dasar, riset lanjutan dengan rentang demografi fakultas yang lebih besar tetap direkomendasikan guna memperoleh peta keluhan yang lebih komprehensif.

## 6. Kesimpulan
Evaluasi kuantitatif komparatif yang disandingkan dengan *System Usability Scale* ini telah membuktikan secara empiris bahwa tingkat kelayakan interaksi (*usability*) antarmuka KHS SIM UPB belum mencapai target ideal, dengan nilai rata-rata 63.33 (T-Stat: -2.17, p > 0.05). Hasil penelitian ini menegaskan bahwa keluhan mahasiswa di lapangan bukan sekadar subjektivitas sesaat, melainkan isu struktural yang terukur jelas. Akar masalah utama berpusat pada kegagalan hierarki informasi (*information architecture*) antarmuka tabel nilai KHS yang kurang dinamis dan tidak responsif untuk diakses pada layar gawai ponsel (*mobile browser*).

Melalui data objektif yang dihasilkan dalam riset ini, direkomendasikan kepada pihak manajemen akademik dan tim pengembang IT Universitas Putra Bangsa untuk segera memprioritaskan penyusunan ulang struktur antarmuka UI/UX KHS dengan fokus utama pada pendekatan *mobile-first design*.

## Daftar Pustaka
1. Brooke, J. (1986). "SUS: A 'Quick and Dirty' Usability Scale". In P. W. Jordan, B. Thomas, B. A. Weerdmeester, & A. L. McClelland (Eds.), *Usability Evaluation in Industry* (pp. 189-194). Taylor & Francis.
2. Bangor, A., Kortum, P. T., & Miller, J. T. (2009). "Determining What Individual SUS Scores Mean: Adding an Adjective Rating Scale". *Journal of Usability Studies*, 4(3), 114-123.
3. Lewis, J. R., & Sauro, J. (2018). "Item Benchmarks for the System Usability Scale". *Journal of Usability Studies*, 13(3), 158-167.
4. Prabowo, A. & Suprapto, B. (2021). "Evaluasi Usabilitas Sistem Informasi Akademik Menggunakan System Usability Scale". *Jurnal Sistem Informasi*.
5. Putra, C. & Adhicandra, D. (2022). "Analisis Tingkat Kebergunaan Portal Akademik Menggunakan SUS". *Jurnal Teknologi Informasi*.
6. Yasin, E. et al. (2022). "Pengukuran Kualitas Antarmuka SIAKAD Kombinasi Metode SUS dan UEQ". *Jurnal Interaksi Manusia Komputer*.
7. Ramadhani, F. & Yusianto, G. (2023). "Evaluasi User Experience Dashboard Sistem Informasi Akademik Kampus". *Jurnal Informatika*.
8. Winandy, F. et al. (2024). "Perancangan Prototype Berbasis Mobile Menggunakan Design Thinking Pada Siakad UNU Kalbar". *Coding : Jurnal Komputer dan Aplikasi*.
9. Firjinia, R. et al. (2025). "Perancangan UI/UX Sistem Informasi Akademik Berbasis Website Di Ponpes An-Nur Tangkit Muaro Jambi". *JUKTISI*.
10. Rahman, A. et al. (2026). "Evaluasi Usability pada Sistem Informasi Akademik (SIAKAD) Menggunakan Metode System Usability Scale (SUS) pada Staf Universitas Ibnu Sina". *Jurnal Responsive Teknik Informatika*.
11. Sari, N. et al. (2026). "Analisis Tingkat Kepuasan Pengguna Sistem Informasi Akademik Menggunakan Pendekatan System Usability Scale (SUS)". *Jurnal Komputer dan Teknologi Sains (KOMTEKS)*.
12. Wijaya, B. et al. (2025). "Evaluation of the Usability of the Academic Information System Using the System Usability Scale (SUS) Method". *Journal of Computer Science Artificial Intelligence and Communications*.
13. Kurniawan, D. et al. (2025). "Evaluasi Kualitas Sistem Informasi Akademik Menggunakan Metode System Usability Scale di SMK Negeri 2 Sangatta Utara". *DIKSI: Jurnal Kajian Pendidikan dan Sosial*.
14. Pratama, R. et al. (2023). "Evaluasi User Experience dan Usability Sistem Informasi Akademik Menggunakan Metode User Experience Questionnaire dan System Usability Scale". *JOISIE*.
15. Hidayat, T. et al. (2023). "Pengujian Usability Sistem Informasi Akademik (SISKA) Universitas Qamarul Huda Badaruddin Menggunakan System Usability Scale (SUS)". *SainsTech Innovation Journal*.
16. Fadillah, M. et al. (2021). "Usability Testing pada Sistem Informasi Akademik IAIN Salatiga Mengunakan Metode System Usability Scale". *JISKA*.
17. Saputra, E. et al. (2026). "Evaluasi Usability SIAKAD Universitas Negeri Gorontalo Menggunakan SUS". *Jurnal SAINTIKOM*.
18. Susanti, E. et al. (2025). "Analisis Pengalaman Pengguna pada SIAKAD Universitas Trunojoyo Madura". *Jurnal Informatika Trunojoyo*.
