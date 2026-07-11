import pandas as pd
from scipy import stats
import os

def calculate_sus():
    # Pastikan script dijalankan dari dalam direktori 05-kode atau sesuaikan path-nya
    # Gunakan path relatif ke 04-data
    data_path = os.path.join('..', '04-data', 'Data_KHS_Raw.csv')
    
    if not os.path.exists(data_path):
        print(f"File tidak ditemukan: {data_path}")
        print("Harap jalankan skrip ini dari dalam folder '05-kode'")
        return

    # Membaca data CSV mentah
    df = pd.read_csv(data_path)
    
    # List untuk menyimpan hasil skor SUS
    sus_scores = []
    
    # Memproses setiap baris respons
    for index, row in df.iterrows():
        try:
            # Q1 (Col 4) s.d Q10 (Col 13) menggunakan 0-indexing
            # Pertanyaan Ganjil (Positif): Skor = Nilai - 1
            q1 = int(row.iloc[4]) - 1
            q3 = int(row.iloc[6]) - 1
            q5 = int(row.iloc[8]) - 1
            q7 = int(row.iloc[10]) - 1
            q9 = int(row.iloc[12]) - 1
            
            # Pertanyaan Genap (Negatif): Skor = 5 - Nilai
            q2 = 5 - int(row.iloc[5])
            q4 = 5 - int(row.iloc[7])
            q6 = 5 - int(row.iloc[9])
            q8 = 5 - int(row.iloc[11])
            q10 = 5 - int(row.iloc[13])
            
            # Kalkulasi Skor Akhir SUS
            raw_score = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10
            final_sus_score = raw_score * 2.5
            sus_scores.append(final_sus_score)
        except Exception as e:
            print(f"Ada kesalahan pembacaan data pada baris {index+1}: {e}")
            sus_scores.append(0)

    # Memasukkan skor SUS ke dalam Dataframe sebagai kolom baru
    df['Skor_SUS'] = sus_scores
    
    # Menyimpan hasil kalkulasi ke folder 06-output
    output_dir = os.path.join('..', '06-output')
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, 'Data_KHS_Processed.csv')
    df.to_csv(output_path, index=False)
    print(f"Berhasil! Data yang telah dihitung Skor SUS-nya disimpan di: {output_path}")
    
    # === ANALISIS STATISTIK ===
    print("\n" + "="*40)
    print("HASIL ANALISIS STATISTIK SUS")
    print("="*40)
    
    mean_sus = df['Skor_SUS'].mean()
    std_sus = df['Skor_SUS'].std()
    n = len(df['Skor_SUS'])
    
    print("\n--- 1. Statistik Deskriptif ---")
    print(f"N (Jumlah Responden): {n}")
    print(f"Rata-rata Skor SUS  : {mean_sus:.2f}")
    print(f"Standar Deviasi     : {std_sus:.2f}")
    
    # Penilaian Adjective Rating & Acceptability berdasarkan Skor SUS
    kategori = ""
    if mean_sus >= 80.3:
        kategori = "Excellent (Sangat Layak)"
    elif mean_sus >= 68:
        kategori = "Good (Layak)"
    elif mean_sus >= 51:
        kategori = "Poor (Kurang Layak)"
    else:
        kategori = "Awful (Sangat Tidak Layak)"
    
    print(f"Kategori Kelayakan  : {kategori}")
    
    # One-Sample T-Test melawan baseline 68
    baseline = 68
    # T-test 2-tailed (Standar SPSS)
    t_stat, p_value_2 = stats.ttest_1samp(df['Skor_SUS'], popmean=baseline)
    # T-test 1-tailed (H1: Rata-rata > 68) -> P-value 2-tailed dibagi 2 jika rata-rata lebih besar dari baseline
    p_value_1 = p_value_2 / 2 if t_stat > 0 else 1 - (p_value_2 / 2)
    
    print(f"\n--- 2. Uji One-Sample T-Test (Nilai Acuan = {baseline}) ---")
    print(f"Nilai T-Hitung      : {t_stat:.3f}")
    print(f"P-Value (2-tailed)  : {p_value_2:.4f}")
    print(f"P-Value (1-tailed)  : {p_value_1:.4f}  <-- Digunakan untuk hipotesis H1 (Skor > 68)")
    
    print("\n--- 3. Kesimpulan Hipotesis ---")
    if p_value_1 < 0.05 and mean_sus > baseline:
        print("Kesimpulan: H1 DITERIMA.")
        print(f"Rata-rata skor SUS sistem ({mean_sus:.2f}) secara signifikan secara statistik LEBIH TINGGI daripada standar kelayakan ({baseline}).")
    else:
        print("Kesimpulan: H1 DITOLAK.")
        print(f"Sistem tidak memenuhi standar kelayakan usabilitas secara signifikan secara statistik.")

if __name__ == "__main__":
    calculate_sus()
