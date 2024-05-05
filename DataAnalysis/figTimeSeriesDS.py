import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PATH = "https://raw.githubusercontent.com/LGsus20/Weather-Forecasting-Scraping/main/DATASETS/DATASET_Modified_Monthly_2021-2023.csv"

Y_df = pd.read_csv(PATH)
Y_df = Y_df.assign(unique_id=np.ones(len(Y_df)))
Y_df['ds'] = pd.to_datetime(Y_df['ds'])

plt.figure(figsize=(12, 8))
plt.plot(Y_df['ds'], Y_df['y'], marker='o', linestyle='-', markersize=3, linewidth=1)
plt.title('Wind Time Series Data')
plt.xlabel('Date')
plt.ylabel('Wind Km/h')
plt.grid(True)

plt.savefig('WindDataSet.png')

plt.show()
