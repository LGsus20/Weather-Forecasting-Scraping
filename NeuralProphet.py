import pandas as pd
import matplotlib

PATH = r"Z:\Python\Weather-Forecasting-Scraping\DATASET-2023-2024.csv"

df = pd.read_csv(PATH)

# plt = df.plot(x="Tiempo:", y="VELOCIDAD DEL VIENTO (Km/h):", figsize=(15, 5))
print(df.dtypes)
print(df.head())

