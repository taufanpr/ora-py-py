#Importing General packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, classification_report

import pickle

from pathlib import Path


#import dataset
df_load = pd.read_csv("https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/dqlab_telco_final.csv")



####################################



### B.3.3.3. Melakukan Exploratory Data Analysis (EDA)
print ('\n\n ########## B.3.3.3. Melakukan Exploratory Data Analysis (EDA) ######### \n\n')

## Exploratory Data Analysis
print ('\n\n ########## Exploratory Data Analysis ######### \n\n')


# import matplotlib dan seaborn
import matplotlib.pyplot as plt
import seaborn as sns




#############



## Memvisualisasikan Prosentase Churn
print ('\n\n ########## Memvisualisasikan Prosentase Churn ######### \n\n')


from matplotlib import pyplot as plt
import numpy as np

#Your codes here
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')

labels = ['Yes','No']
churn = df_load.Churn.value_counts()
ax.pie(churn, labels=labels, autopct='%.0f%%')
plt.show()


##################


## Exploratory Data Analysis (EDA) Variabel Numerik
print ('\n\n ########## Exploratory Data Analysis (EDA) Variabel Numerik ######### \n\n')


from matplotlib import pyplot as plt
import numpy as np

# creating bin in chart
numerical_features = ['MonthlyCharges','TotalCharges','tenure']
fig, ax = plt.subplots(1, 3, figsize=(15, 6))

# Use the following code to plot two overlays of histogram per each numerical_features,
df_load[df_load.Churn == 'No'][numerical_features].hist(bins=20, color='blue', alpha=0.5, ax=ax)

df_load[df_load.Churn == 'Yes'][numerical_features].hist(bins=20, color='orange', alpha=0.5, ax=ax)

plt.show()


#######################


## Exploratory Data Analysis (EDA) Variabel Kategorik
print ('\n\n ########## Exploratory Data Analysis (EDA) Variabel Kategorik ######### \n\n')




from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
sns.set(style='darkgrid')

# Your code goes here
fig, ax = plt.subplots(3, 3, figsize=(14, 12))

sns.countplot(data=df_load, x='gender', hue='Churn', ax=ax[0][0])
sns.countplot(data=df_load, x='Partner', hue='Churn', ax=ax[0][1])
sns.countplot(data=df_load, x='SeniorCitizen', hue='Churn', ax=ax[0][2])
sns.countplot(data=df_load, x='PhoneService', hue='Churn', ax=ax[1][0])
sns.countplot(data=df_load, x='StreamingTV', hue='Churn', ax=ax[1][1])
sns.countplot(data=df_load, x='InternetService', hue='Churn', ax=ax[1][2])
sns.countplot(data=df_load, x='PaperlessBilling', hue='Churn', ax=ax[2][1])

plt.tight_layout()
plt.show()



##############


### B.3.3.4. Melakukan Data PreProcessing
print ('\n\n ########## B.3.3.4. Melakukan Data PreProcessing ######### \n\n')

## Menghapus Unnecessary Columns dari data
print ('\n\n ########## Menghapus Unnecessary Columns dari data ######### \n\n')


# Remove the unnecessary columns customerID & UpdatedAt
cleaned_df = df_load.drop(['customerID','UpdatedAt'], axis=1)

print(cleaned_df.head())




#########


## Encoding Data
print ('\n\n ########## Encoding Data ######### \n\n')



from sklearn.preprocessing import LabelEncoder

# Convert all the non-numeric columns to numerical data types
for column in cleaned_df.columns:
    if cleaned_df[column].dtype == np.number: continue

# Perform encoding for each non-numeric column
cleaned_df[column] = LabelEncoder().fit_transform(cleaned_df[column])

print(cleaned_df.describe())


##########


## Splitting Dataset
print ('\n\n ########## Splitting Dataset ######### \n\n')


from sklearn.model_selection import train_test_split

# Predictor dan target
X = cleaned_df.drop('Churn', axis = 1)
y = cleaned_df['Churn']

# Splitting train and test
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Print according to the expected result
print('Jumlah baris dan kolom dari x_train adalah:', x_train.shape,', sedangkan Jumlah baris dan kolom dari y_train adalah:', y_train.shape)

print('Prosentase Churn di data Training adalah:')
print(y_train.value_counts(normalize=True))

print('Jumlah baris dan kolom dari x_test adalah:', x_test.shape,', sedangkan Jumlah baris dan kolom dari y_test adalah:', y_test.shape)

print('Prosentase Churn di data Testing adalah:')
print(y_test.value_counts(normalize=True))




print ('\n\n##########  #########\n\n')

# Code di bawah ini gabisa. Dari B.3.3.5. Modelling: Logistic Regression 

#from sklearn.linear_model import LogisticRegression
#log_model = LogisticRegression().fit(x_train, y_train)

#print('Model Logistic Regression yang terbentuk adalah: \n',log_model)




