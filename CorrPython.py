# Grafické znázornenie otázky č. 4 - Percentuálny medziročný nárast HDP, miezd a cien v ČR za obdobie 2008-2018

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'percentualna_zmena.csv'
df = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['percentage_change_GDP'], label='percentage_change_GDP')
plt.plot(df['Year'], df['Percentage_change_wages'], label='Percentage_change_wages')
plt.plot(df['Year'], df['Percentage_change_price'], label='Percentage_change_price')



plt.xlabel('Rok')
plt.ylabel('Percenta (%)')
plt.title('Percentuálny medziročný nárast HDP, miezd a cien za obdobie 2008-2018')
plt.legend()

plt.show()
