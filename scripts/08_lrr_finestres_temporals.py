
import pandas as pd
import matplotlib.pyplot as plt

archivo = r"C:\Users\FX506\Desktop\tfg python\Grafiques_tfg.xlsx"

df = pd.read_excel(archivo, sheet_name="B2_1994-1945", header=3)
df.columns = df.columns.str.strip()
df = df.sort_values("TransOrder")

plt.figure(figsize=(8, 5))
plt.plot(df["TransOrder"], df["LRR"], marker="o")
plt.axhline(0)

plt.title("LRR Baseline B 1994-1945")
plt.xlabel("Transecte")
plt.ylabel("LRR")
plt.grid(True)
plt.tight_layout()

plt.savefig("LRR_B_1994_1945.png", dpi=300)
plt.show()

