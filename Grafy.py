# Vizualizácia priemerných miezd, cien a HDP za roky 2008-2018


  # Vytvorenie grafu Priemerná mzda za roky 2008-2018

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Datakorelacia.csv'
df = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))      
plt.plot(df['Year'], df['AVG_wages'], label='AVG_wages')

plt.xlabel('Rok')
plt.ylabel('Kč')
plt.title('Priemerná mzda za roky 2008-2018')
plt.legend()

plt.show()



  # Vytvorenie grafu Priemerná cena potravín za obdobie 2008-2018

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Datakorelacia.csv'
df = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['AVG_price'], label='AVG_price')

plt.xlabel('Rok')
plt.ylabel('Kč')
plt.title('Priemerná cena potravín za obdobie 2008-2018')
plt.legend()

plt.show()




  # Vytvorenie grafu Priemer HDP v ČR za roky 2008-2018

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Datakorelacia.csv'
df = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))            
plt.plot(df['Year'], df['GDP'], label='GDP')

plt.xlabel('Rok')
plt.ylabel('Mld. (Kč)')
plt.title('Priemer HDP v ČR za roky 2008-2018')
plt.legend()

plt.show()
