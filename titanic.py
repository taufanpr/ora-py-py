import pandas as pd

def concat_df(train_data, test_data):
    # Returns a concatenated df of training and test set
    return pd.concat([train_data, test_data], sort=True).reset_index(drop=True)

df_train = pd.read_csv('https://academy.dqlab.id/dataset/challenge/feature-engineering/titanic_train.csv')

df_test = pd.read_csv('https://academy.dqlab.id/dataset/challenge/feature-engineering/titanic_test.csv')

df_all = concat_df(df_train, df_test)


df_train.name = 'Training Set'

df_test.name = 'Test Set'
df_all.name = 'All Set'

dfs = [df_train, df_test]


df_train_corr = df_train.corr().abs()

print(df_train_corr.to_string())