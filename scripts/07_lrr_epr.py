import pandas as pd
import matplotlib.pyplot as plt

archivo = "Tu URL"

df = pd.read_excel(archivo, sheet_name="B2", header=3)
df.columns = df.columns.str.strip()
df = df.sort_values("TransOrder")

plt.figure(figsize=(8, 5))
plt.plot(df["TransOrder"], df["LRR"], marker="o")
plt.axhline(0)

plt.title("LRR Rates Baseline B")
plt.xlabel("Transecte")
plt.ylabel("LRR")
plt.grid(True)
plt.tight_layout()
plt.savefig("LRR_transectes.png", dpi=300)
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(df["TransOrder"], df["EPR"], marker="o")
plt.axhline(0)

plt.title("EPR Rates Baseline B")
plt.xlabel("Transecte")
plt.ylabel("EPR")
plt.grid(True)
plt.tight_layout()
plt.savefig("EPR_transectes.png", dpi=300)
plt.show()

