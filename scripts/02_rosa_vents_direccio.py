import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

direction_col = 'Direcc. Media de Proced.(0=N,90=E)'

#Tambe es pot fer amb "PUNTO SIMAR"
df = pd.read_csv("BOYA.csv", sep="\t", skiprows=1)

df = df[(df[direction_col] != -9999.9) & (df[direction_col] != 0)]

bins = np.arange(0, 361, 30)
labels = [f"{i}°-{i+30}°" for i in range(0, 360, 30)]

df['bin'] = pd.cut(df[direction_col], bins=bins, right=False, labels=labels)
counts = df['bin'].value_counts().sort_index()

theta = np.deg2rad(np.arange(15, 360, 30))

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(8, 8))
ax.bar(theta, counts.values, width=np.deg2rad(30), edgecolor='black')

ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_title("Rosa dels vents - Direcció mitjana de l’onatge", va='bottom')

plt.show()

