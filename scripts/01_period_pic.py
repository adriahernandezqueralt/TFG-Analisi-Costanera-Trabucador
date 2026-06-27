

import pandas as pd
import matplotlib.pyplot as plt


variable_plot = 'Periodo de Pico(s)'

#Tambe es pot fer amb "PUNTO SIMAR"
df = pd.read_csv("BOYA.csv", sep="\t", skiprows=1)
df = df[['Fecha (GMT)', variable_plot]]


df = df[(df[variable_plot] != -9999.9) & (df[variable_plot] != 0)]


df['Fecha (GMT)'] = pd.to_datetime(df['Fecha (GMT)'], format="%Y %m %d %H")


plt.figure(figsize=(10, 5))
plt.plot(df['Fecha (GMT)'], df[variable_plot])


plt.title("Període de Pic")
plt.xlabel("Data i hora (GMT)")
plt.ylabel("Període de pic (s)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
