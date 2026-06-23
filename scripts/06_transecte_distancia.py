import pandas as pd
import matplotlib.pyplot as plt


archivo = r"C:\Users\FX506\Desktop\tfg python\Grafiques_tfg.xlsx"


df = pd.read_excel(archivo, sheet_name="DISTANCIA B2", header=4)


transecte = df[df["TransectId"] == 105].sort_values("ShorelineID")


plt.figure(figsize=(8, 5))
plt.plot(transecte["ShorelineID"], transecte["Distance"], marker="o")


plt.title("Transecte 105 B")
plt.xlabel("Any")
plt.ylabel("Distància")
plt.grid(True)
plt.tight_layout()
plt.show()
