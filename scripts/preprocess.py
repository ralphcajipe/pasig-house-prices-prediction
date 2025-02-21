import pandas as pd

# Load csv data
df = pd.read_csv('data/PH_houses_v2.csv')

df.columns
df.dtypes
df.describe()
df.isnull().sum()

# Drop the 'descriptions' and 'link' columns
df = df.drop(columns=['Description', 'Link'])

# Filter rows where 'Location' is 'Pasig'
df_pasig = df[df['Location'] == 'Pasig']

# Save the dataframe with only 'Pasig' locations to a new csv file
df_pasig.to_csv('data/PH_houses_Pasig.csv', index=False)
