#import library
import pandas as pd

#utk permudah tampilan row data
pd.options.display.max_columns = 50 

#import dataset
df_load = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/dqlab_telco.csv')

#Tampilkan jumlah baris dan kolom
print(df_load.shape)

print("\n ---------- \n")

#Tampilkan 5 data teratas
print(df_load.head(5))

print("\n ---------- \n")

#Jumlah ID yang unik
print(df_load.customerID.nunique())