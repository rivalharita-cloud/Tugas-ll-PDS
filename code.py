import pandas as pd
# Baca file CSV
df = pd.read_csv('calon_tni.csv')
df.columns = [c.strip().lower() for c in df.columns]
def kategori_tinggi(h):
    if h < 170:
        return 'Pendek'
    elif h <= 180:
        return 'Sedang'
    else:
        return 'Tinggi'
df['kategori'] = df['tinggi'].apply(kategori_tinggi)
print("=== Statistik Tinggi Badan ===")
print(df['tinggi'].describe())
mean_tinggi = df['tinggi'].mean()
print("\nRata-rata tinggi:", round(mean_tinggi, 2))
print("\n=== Calon di atas rata-rata tinggi ===")
print(df[df['tinggi'] > mean_tinggi])
print("\n=== Urutan dari Tertinggi ke Terendah ===")
print(df.sort_values(by='tinggi', ascending=False))
print("\n=== Urutan dari Terendah ke Tertinggi ===")
print(df.sort_values(by='tinggi', ascending=True))
print("\n=== Jumlah Calon per Kategori ===")
print(df['kategori'].value_counts())
print("\nStandar Deviasi :", round(df['tinggi'].std(), 2))
print("Variansi :", round(df['tinggi'].var(), 2))
calon_tertinggi = df.loc[df['tinggi'].idxmax()]
calon_terendah = df.loc[df['tinggi'].idxmin()]
print("\n=== Calon dengan Tinggi Badan Tertinggi ===")
print(calon_tertinggi)
print("\n=== Calon dengan Tinggi Badan Terendah ===")
print(calon_terendah)
