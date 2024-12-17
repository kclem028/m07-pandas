import pandas as pd
#Reading From CSV
df = pd.read_csv('telco_churn.csv')

#Creating a Dictionary
tempdict = {'coll':[1,2,3], 'col2':[4,5,6], 'col3':[7,8,9]}
dictdf = pd.DataFrame.from_dict(tempdict)

df = pd.read_csv('telco_churn.sv')
#Read Top/Bottom 5 Rows
df.head(5)

dictdf.head()

df.tail(5)
#Show Columns/datatypes
df.columns

df.dtypes

#Summary Statistics
df.describe()
df.describe(include="object")

#Column Filtering
df.State

df['International Plan']

df[['State', 'International Plan']]

df.Churn.unique()

#filters rows
df.head()

df[df['International plan']=='No']

df[(df['International plan']=='No') & (df['Churn']==True)]

#iloc indexing

df.iloc[14]

#false indexing
df.iloc[14,-1]

#range indexing
df.iloc[22:33]

#loc indexing

state = df.copy()
state.set_index('State', inplace=True)

state.head()

state.loc['OH']

#Dropping Rows

df.isnull().sum()

df.dropna(inplace=True)

df.isnull().sum()

#Dropping columns

df.drop('Area code', axis=1)

#Creating new calculated columns

df['New Column'] = df['Total night minutes'] + df['Total intl minutes']

df.head()

#Column updates
df['New Column'] = 100

df.head()

df.iloc[0,-1] = 10

df.head()

#Condition based Updating via Apply

df['Churn Binary'] = df['Churn'].apply(lambda x: 1 if x==True else 0)

df[df['Churn']==True].head()

#Delete/Output

#Output to CSV
df.to_csv('output.csv')

#Output to JSON
df.to_json()

#Output to HTML
df.to_html()

#Delete Dataframe
del df