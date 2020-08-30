#import library
import pandas as pd

#utk permudah tampilan row data
pd.options.display.max_columns = 50 

#import dataset
df_load = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/dqlab_telco.csv')



# Masukkan variable
for col_name in list(['gender','SeniorCitizen','Partner','Dependents','PhoneService','MultipleLines','InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod','Churn']):

    print('\nUnique Values Count \033[1m' + 'Before Standardized \033[0m Variable',col_name)


print("\n ---------- \n")


print(df_load[col_name].value_counts())






print("\n ---------- \n")


## Menstandarisasi Variable Kategorik

df_load = df_load.replace(['Wanita','Laki-Laki','Churn','Iya'],['Female','Male','Yes','Yes'])

# Masukkan variable
for col_name in list(['gender','Dependents','Churn']):

    print('\nUnique Values Count \033[1m' + 'After Standardized \033[0mVariable',col_name)

print(df_load[col_name].value_counts())