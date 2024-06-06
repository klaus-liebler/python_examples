import pandas as pd
bauteile = pd.read_csv("bauteile.csv")
print("Maximale Bauteileanzahl", bauteile["Menge"].max())
