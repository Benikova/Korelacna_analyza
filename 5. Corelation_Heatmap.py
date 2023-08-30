# Deskripcia dát

import pandas as pd

file_path = 'Datakorelacia.csv'
df = pd.read_csv(file_path)

print(df.head())
print(df.info())
print(df.describe())


# Korelácia z priemerovaných dát

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'Datakorelacia.csv'
df = pd.read_csv(file_path)

df = df.drop(columns=['Year'])

korelacia1 = df['GDP'].corr(df['AVG_wages'])
korelacia2 = df['GDP'].corr(df['AVG_price'])
korelacia3 = df['AVG_price'].corr(df['AVG_wages'])

print(f"Korelačný koeficient medzi GDP a AVG_wages: {korelacia1}")
print(f"Korelačný koeficient medzi GDP a AVG_price: {korelacia2}")
print(f"Korelačný koeficient medzi AVG_wages a AVG_price: {korelacia3}")


# Korelačná matica

correlation_matrix = df.corr()
print(correlation_matrix)

sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
plt.title("Pearson's Correlation Coefficient")
plt.show()
