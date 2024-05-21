import pandas as pd
from statsmodels.tsa.stattools import acf
import matplotlib.pyplot as plt

# Read the CSV file
PATH = "https://raw.githubusercontent.com/LGsus20/Weather-Forecasting-Scraping/main/DATASETS/DATASET_Modified_Monthly_2021-2024.csv"
df = pd.read_csv(PATH)

print(df.head())
data = df['y']

autocorr = acf(data, nlags=24)

print(autocorr)

plt.figure(figsize=(10, 6))
plt.stem(range(len(autocorr)), autocorr)
plt.title('Autocorrelation of Wind speed', fontsize=16)
plt.xlabel('Lag (hour)')
plt.ylabel('Autocorrelation')
plt.show()
plt.savefig('autocorrelation_plot.png')

