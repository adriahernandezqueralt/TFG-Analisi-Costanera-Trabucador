import pandas as pd
import matplotlib.pyplot as plt


period_col = 'Periodo de Pico(s)'
height_col = 'Altura Signif. del Oleaje(m)'


df = pd.read_csv("BOYA.csv", sep="\t", skiprows=1)


df['Fecha (GMT)'] = pd.to_datetime(df['Fecha (GMT)'], format="%Y %m %d %H")


df = df[
    (df[period_col] != -9999.9) & (df[period_col] != 0) &
    (df[height_col] != -9999.9) & (df[height_col] != 0)
]


df['Energia proporcional'] = df[height_col]**2 * df[period_col]


plt.figure(figsize=(10, 5))
plt.plot(df['Fecha (GMT)'], df['Energia proporcional'])


plt.title("Energia proporcional de l’onatge")
plt.xlabel("Data i hora (GMT)")
plt.ylabel("Energia proporcional (m²·s)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


