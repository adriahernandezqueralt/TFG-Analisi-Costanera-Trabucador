

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("MAREAOGRAF.csv", sep=";")


df["Fecha (GMT)"] = pd.to_datetime(df["Fecha (GMT)"], errors="coerce")
df["Nivel medio (cm)"] = pd.to_numeric(df["Nivel medio (cm)"], errors="coerce")


df = df[
    (~df["Nivel medio (cm)"].isin([-9999.9, 999.9])) &
    (df["Fecha (GMT)"] >= "2011-05-30")
].dropna(subset=["Fecha (GMT)", "Nivel medio (cm)"])


df_max = df.loc[
    df.groupby(df["Fecha (GMT)"].dt.to_period("M"))["Nivel medio (cm)"].idxmax()
].reset_index(drop=True)


X = np.arange(len(df_max))
y = df_max["Nivel medio (cm)"].values


pendent, intercept = np.polyfit(X, y, 1)


print("Pendent (cm/mes):", pendent)
print("Pendent (mm/any):", pendent * 10 * 12)


plt.figure(figsize=(10, 5))
plt.plot(df_max["Fecha (GMT)"], y, label="Màxims mensuals")
plt.plot(df_max["Fecha (GMT)"], pendent * X + intercept, "--", label="Ajust lineal")


plt.xlabel("Data")
plt.ylabel("Nivell mitjà (cm)")
plt.title("Màxims mensuals i ajust lineal")
plt.legend()
plt.tight_layout()
plt.show()


df_max.to_csv("maxims_mensuals.csv", index=False, sep=";")
