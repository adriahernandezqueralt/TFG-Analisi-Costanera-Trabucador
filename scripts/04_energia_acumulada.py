import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


period_col = 'Periodo de Pico(s)'
height_col = 'Altura Signif. del Oleaje(m)'


df = pd.read_csv("BOYA.csv", sep="\t", skiprows=1)


df['Fecha (GMT)'] = pd.to_datetime(df['Fecha (GMT)'], format="%Y %m %d %H")


df = df[
    (df[period_col] != -9999.9) & (df[period_col] != 0) &
    (df[height_col] != -9999.9) & (df[height_col] != 0)
]


df['Energia proporcional'] = df[height_col]**2 * df[period_col]
df['Energia acumulada'] = df['Energia proporcional'].cumsum()


plt.figure(figsize=(12, 5))
plt.plot(df['Fecha (GMT)'], df['Energia acumulada'])


plt.title('Flux d’energia acumulada')
plt.xlabel('Data')
plt.ylabel('Flux d’energia acumulada')
plt.grid(True)


ax = plt.gca()
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.xticks(rotation=45)


plt.tight_layout()
plt.show()


