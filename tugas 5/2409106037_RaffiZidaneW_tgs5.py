import pandas as pd
import matplotlib.pyplot as plt

# Pastikan path file sesuai
file_path = "Top10VideoGameStocks.csv"  # Ganti dengan path file Anda

# Membaca file CSV
try:
    df = pd.read_csv(file_path)
    print("File berhasil dibaca!")
    print(df.head())  # Menampilkan data pertama
except FileNotFoundError:
    print("File tidak ditemukan! Periksa path file Anda.")
except pd.errors.ParserError:
    print("Terjadi kesalahan saat membaca file CSV. Periksa format file Anda.")

# Visualisasi sederhana jika file berhasil dibaca
if 'Company' in df.columns and 'Close' in df.columns and 'Date' in df.columns:
    # Pastikan Date dalam format datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Filter data untuk perusahaan tertentu
    selected_companies = ['Sony Interactive Entertainment', 'Nintendo', 'Microsoft']
    df_filtered = df[df['Company'].isin(selected_companies)]

    # Visualisasi harga penutupan saham
    plt.figure(figsize=(12, 6))
    for company in selected_companies:
        company_data = df_filtered[df_filtered['Company'] == company]
        plt.plot(company_data['Date'], company_data['Close'], label=company)

    # Menambahkan detail pada grafik
    plt.title("Performa Harga Saham", fontsize=16)
    plt.xlabel("Tanggal", fontsize=12)
    plt.ylabel("Harga Penutupan (USD)", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("Kolom penting tidak ditemukan dalam file CSV!")
