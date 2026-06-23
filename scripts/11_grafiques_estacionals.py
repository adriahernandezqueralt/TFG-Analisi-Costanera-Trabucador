import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("BOYA.csv", sep=r"\s+", skiprows=2, header=None, engine="python")

df.columns = [
    "Any", "Mes", "Dia", "Hora", "Hs", "Tm02", "Tp", "Hmax", "Tmax",
    "Canal1", "DirMedia", "DirPico", "Dispersion", "Canal2"
]

df = df.apply(pd.to_numeric, errors="coerce")

df["Data"] = pd.to_datetime(
    df[["Any", "Mes", "Dia", "Hora"]].rename(columns={
        "Any": "year",
        "Mes": "month",
        "Dia": "day",
        "Hora": "hour"
    })
)

df = df[
    (df["Hs"] != -9999.9) & (df["Hs"] != 0) &
    (df["Tp"] != -9999.9) & (df["Tp"] != 0)
]

for any_ in range(2005, 2026):

    df_any = df[
        (df["Data"].dt.year == any_) &
        (df["Data"].dt.month.isin([9, 10, 11]))
    ].sort_values("Data").copy()

    if df_any.empty:
        continue

    df_any["Flux energia"] = df_any["Hs"]**2 * df_any["Tp"]
    df_any["Flux energia acumulat"] = df_any["Flux energia"].cumsum()

    for columna, titol, ylabel in [
        ("Flux energia", "Flux energia", "Hs²·Tp"),
        ("Flux energia acumulat", "Flux energia acumulat", "Σ(Hs²·Tp)")
    ]:
        plt.figure(figsize=(14, 5))
        plt.plot(df_any["Data"], df_any[columna], linewidth=1)

        plt.title(f"{titol} - Set-Oct-Nov {any_}")
        plt.xlabel("Data")
        plt.ylabel(ylabel)
        plt.grid(True)

        ax = plt.gca()
        ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m"))

        if columna == "Flux energia":
            plt.ylim(0, 700)

        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()




