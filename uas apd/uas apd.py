import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Membaca data dari dataset
file_path = "hg00.csv"  # Pastikan file berada di direktori yang sama

data = pd.read_csv(file_path)

# 2. Menampilkan deskripsi data
print("Deskripsi Data:")
print(data.describe(include='all'))

# 3. Menampilkan 10 data pertama menggunakan iterrows
print("\n10 Data Pertama:")
for index, row in data.iterrows():
    if index < 10:
        print(row)

# 4. Mengurutkan data berdasarkan Release Date secara ascending
sorted_data = data.sort_values(by='Release Date', ascending=True)
print("\nData Setelah Diurutkan (Berdasarkan Release Date):")
print(sorted_data.head(10))

# 5. Menampilkan jumlah data yang kosong/tidak ada
data_missing = data.isnull().sum()
print("\nJumlah Data Kosong di Setiap Kolom:")
print(data_missing)

# 6. Membuat 2 visualisasi
plt.figure(figsize=(10, 6))

# Visualisasi 1: Distribusi Tahun Rilis (Release Date)
data['Release Year'] = data['Release Date'].str[:4]  # Mengambil tahun dari kolom Release Date
sns.histplot(data['Release Year'], bins=20, kde=False, color='green')
plt.title('Penyebaran Tahun Rilis')
plt.xlabel('Tahun Rilis')
plt.ylabel('Jumlah Produk')
plt.xticks(rotation=45)
plt.show()

# Visualisasi 2: Jumlah Produk Berdasarkan Tahun Rilis (Bentuk Pie Chart)
release_counts = data['Release Year'].value_counts().sort_index()
plt.figure(figsize=(8, 8))
plt.pie(release_counts.values, labels=release_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('viridis', len(release_counts)))
plt.title('Persentase Produk Berdasarkan Tahun Rilis')
plt.axis('equal')
plt.show()