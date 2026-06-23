# TFG-Analisi-Costanera-Trabucador


# Codis del Treball de Fi de Grau (TFG)

Aquest repositori recull els scripts utilitzats per al tractament, anàlisi i representació gràfica de dades emprades en el Treball de Fi de Grau. Els codis permeten generar gràfiques relacionades amb l’onatge, l’energia de l’onatge, el nivell mitjà del mar i l’evolució de transectes costaners.


## Contingut del repositori

La proposta d’organització del repositori és la següent:

```text
TFG-codis/
│
├── README.md
├── requirements.txt
│
├── dades/
│   ├── BOYA.csv
│   ├── MAREAOGRAF.csv
│   └── Grafiques_tfg.xlsx
│
├── scripts/
│   ├── 01_period_pic.py
│   ├── 02_rosa_vents_direccio.py
│   ├── 03_energia_onatge.py
│   ├── 04_energia_acumulada.py
│   ├── 05_nivell_mitja_mar_pendent.py
│   ├── 06_transecte_distancia.py
│   ├── 07_lrr_epr.py
│   ├── 08_lrr_finestres_temporals.py
│   ├── 09_lrr_colors_b2.py
│   ├── 10_lrr_colors_a2.py
│   └── 11_grafiques_estacionals.py

## Descripció dels scripts

### `01_period_pic.py`
Genera una gràfica temporal del període de pic de l’onatge a partir del fitxer `BOYA.csv`.

### `02_rosa_vents_direccio.py`
Genera una rosa dels vents amb la direcció mitjana de procedència de l’onatge.

### `03_energia_onatge.py`
Calcula i representa l’energia proporcional de l’onatge mitjançant l’expressió:

```text
Energia proporcional = Hs² · Tp
```

on `Hs` és l’altura significativa de l’onatge i `Tp` és el període de pic.

### `04_energia_acumulada.py`
Calcula el flux d’energia acumulada de l’onatge al llarg del temps a partir de l’energia proporcional acumulada.

### `05_nivell_mitja_mar_pendent.py`
Analitza el nivell mitjà del mar a partir del fitxer `MAREAOGRAF.csv`, selecciona els màxims mensuals i calcula la tendència lineal. També exporta els resultats a `maxims_mensuals.csv`.

### `06_transecte_distancia.py`
Representa l’evolució de la distància d’un transecte concret al llarg dels anys a partir del fitxer `Grafiques_tfg.xlsx`.

### `07_lrr_epr.py`
Genera gràfiques dels indicadors `LRR` i `EPR` per als transectes d’una baseline.

### `08_lrr_finestres_temporals.py`
Representa el valor de `LRR` per a una finestra temporal concreta.

### `09_lrr_colors_b2.py`
Genera una gràfica de `LRR` per a la baseline B, incloent zones destacades i marques visuals per facilitar la interpretació dels resultats.

### `10_lrr_colors_a2.py`
Genera una gràfica de `LRR` per a la baseline A, també amb zones destacades i marques visuals.

### `11_grafiques_estacionals.py`
Genera gràfiques estacionals del flux d’energia i del flux d’energia acumulat per als mesos de setembre, octubre i novembre de cada any.
