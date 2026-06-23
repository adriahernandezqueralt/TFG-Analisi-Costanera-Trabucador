import pandas as pd
import matplotlib.pyplot as plt

archivo = r"C:\Users\FX506\Desktop\tfg python\Grafiques_tfg.xlsx"

df = pd.read_excel(archivo, sheet_name="A2", header=3)
df.columns = df.columns.str.strip()
df = df.dropna(subset=["TransOrder", "LRR"]).sort_values("TransOrder")

plt.figure(figsize=(12, 6))

plt.plot(df["TransOrder"], df["LRR"], marker="o", linewidth=2, alpha=0.85)

plt.axhline(0, color="black", linewidth=1.7)
plt.axhline(5, color="gray", linestyle="--", linewidth=1.5)
plt.axhline(-5, color="gray", linestyle="--", linewidth=1.5)

plt.axvline(70, color="red", linestyle="--", linewidth=1.8)
plt.axvline(109, color="blue", linestyle="--", linewidth=1.8)
plt.axvspan(70, 109, color="#d8cc74", alpha=0.4)

plt.fill_between([38, 55], 3, 6.5, color="#63d39b", alpha=0.65)
plt.fill_between([105, 112], -6, -3.2, color="#ff7b7b", alpha=0.65)
plt.fill_between([181, 189], 8.7, 11.5, color="#556ee6", alpha=0.7)

plt.text(89.5, 12.5, "Barra del Trabucador", fontsize=18, fontweight="bold", ha="center")

plt.title("LRR Rates Baseline A", fontsize=18)
plt.xlabel("Transecte", fontsize=13)
plt.ylabel("LRR", fontsize=13)

plt.grid(True, alpha=0.45)
plt.ylim(-13, 18)
plt.xlim(df["TransOrder"].min() - 5, df["TransOrder"].max() + 5)
plt.gca().invert_xaxis()

plt.tight_layout()
plt.savefig("LRR_Baseline_A.png", dpi=300)
plt.show()


