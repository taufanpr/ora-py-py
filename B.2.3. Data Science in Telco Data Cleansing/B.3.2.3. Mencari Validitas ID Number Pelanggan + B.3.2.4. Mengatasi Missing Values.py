#import library
import pandas as pd

#utk permudah tampilan row data
pd.options.display.max_columns = 50 

#import dataset
df_load = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/dqlab_telco.csv')


"""
* Panjang karakter adalah 11-12.
* Terdiri dari Angka Saja, tidak diperbolehkan ada karakter selain angka.
* Diawali angka 45 pada 2 digit pertama.

My Desc:
	* count() = hitung banyaknya rows Customer ID, 
	* str.match() & regex = mencocokan dgn kriteria diatas. 
	* astype() = merubah tipe datanya yg semula numeric

"""

df_load['valid_id'] = df_load['customerID'].astype(str).str.match(r'(45\d{9,10})')

df_load = (df_load[df_load['valid_id'] == True]).drop('valid_id', axis = 1)

print('Hasil jumlah ID Customer yang terfilter adalah',df_load['customerID'].count())


print("\n --------- \n")


"""
# Memfilter Duplikasi ID Number Pelanggan
"""

# Drop Duplicate Rows
df_load.drop_duplicates()

# Drop duplicate ID sorted by Periode
df_load = df_load.sort_values('UpdatedAt', ascending=False).drop_duplicates(['customerID'])

print('Hasil jumlah ID Customer yang sudah dihilangkan duplikasinya (distinct) adalah',df_load['customerID'].count())


print("\n --------- \n")
"""
# B.3.2.4. [SMP SINI] Mengatasi Missing Values
"""


print('Total missing values data dari kolom Churn',df_load['Churn'].isnull().sum())

# Dropping all Rows with spesific column (churn)
df_load.dropna(subset=['Churn'],inplace=True)

print('Total Rows dan kolom Data setelah dihapus data Missing Values adalah',df_load.shape)



print("\n --------- \n")



"""
* Tenure pihak data modeller meminta setiap rows yang memiliki missing values untuk Lama berlangganan di isi dengan 11
* Variable yang bersifat numeric selain Tenure di isi dengan median dari masing-masing variable tersebut

Tentukan :
* Apa masih ada data yg missing values
* Jumlah Missing Values dari masing-masing variable
* Tangani Missing Valuesnya
"""


print('Status Missing Values :',df_load.isnull().values.any())

print('\nJumlah Missing Values masing-masing kolom, adalah:')
print(df_load.isnull().sum().sort_values(ascending=False))

# handling missing values Tenure fill with 11
df_load['tenure'].fillna(11, inplace=True)

# Handling missing values num vars (except Tenure)
for col_name in list(['MonthlyCharges','TotalCharges']):
	median = df_load[col_name].median()
df_load[col_name].fillna(median, inplace=True)

print('\nJumlah Missing Values setelah di imputer datanya, adalah:')

print(df_load.isnull().sum().sort_values(ascending=False))


















