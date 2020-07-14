import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Grab the csv file
covid_weekly_death_toll_file = pd.ExcelFile('covid_deaths.xlsx')

# Navigate to the correct Sheet on csv file
weekly_figures = pd.read_excel(covid_weekly_death_toll_file, 'Weekly figures 2020')

# Create dataframe from csv file
df = pd.DataFrame(data=weekly_figures)

# Select the rows we want
df = df.loc[[4, 16, 17]]

# transpose data set so the we have the correct headers
df = df.T

# rename the headers
headers = df.iloc[0]
df = df[1:]
df.columns = headers

# reset the index
df = df.reset_index(drop=True).dropna()
df = df.set_index('Week ended', drop=True)

# seaborn wants dataframe to be of float datatype
df = df.astype(float)
print(df)

sns.lineplot(data=df)
plt.show()
