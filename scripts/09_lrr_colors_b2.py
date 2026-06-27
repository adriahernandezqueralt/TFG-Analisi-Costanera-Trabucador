import pandas as pd
import matplotlib.pyplot as plt

archivo = "Tu URL"

df = pd.read_excel(archivo, sheet_name="B2", header=3)
df.columns = df.columns.str.strip()
df = df.dropna(subset=["TransOrder", "LRR"]).sort_values("TransOrder")

plt.figure(figsize=(11, 6))

plt.plot(df["TransOrder"], df["LRR"], marker="o", linewidth=2, alpha=0.8)
plt.axhline(0, color="black", linewidth=1.6)

plt.axvline(61, color="red", linestyle="--", linewidth=1.8)
plt.axvline(96, color="blue", linestyle="--", linewidth=1.8)
plt.axvspan(61, 96, color="#d8cc74", alpha=0.4)

plt.fill_between([38, 66], -2, 1.5, color="#8e63ce", alpha=0.35)
plt.fill_between([100, 107], -2, 1.5, color="#7fd0db", alpha=0.45)

plt.text(78, 3.5, "Barra del Trabucador", fontsize=16, fontweight="bold", ha="center")

plt.title("LRR Rates Baseline B", fontsize=17)
plt.xlabel("Transecte", fontsize=12)
plt.ylabel("LRR", fontsize=12)

plt.xlim(df["TransOrder"].min() - 2, df["TransOrder"].max() + 2)
plt.grid(True, alpha=0.5)
plt.tight_layout()

plt.savefig("LRR_estil_tfg.png", dpi=300)
plt.show()
