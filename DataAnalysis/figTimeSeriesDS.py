import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PATH = "https://raw.githubusercontent.com/LGsus20/Weather-Forecasting-Scraping/main/DATASETS/DATASET_Modified_Monthly_2021-2024.csv"

df = pd.read_csv(PATH)

# Convert the 'ds' column to datetime format
df['ds'] = pd.to_datetime(df['ds'])

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df.loc[:26281, 'ds'], df.loc[:26281, 'y'], color='#0083B6', label='Training')

# Plot the data after 26281 with a different color
plt.plot(df.loc[26281:, 'ds'], df.loc[26281:, 'y'], color='#00975F', label='Test')


# Add labels and title
plt.xlabel('Date', fontsize=16)
plt.ylabel('Wind speed (km/h)', fontsize=16)
plt.title('Wind Speed 2021-2024 March', fontsize=18)

# Change color after value 26281
change_color_index = 26281
plt.axvline(df.loc[change_color_index, 'ds'], color='#B16B38', linestyle='--')

# Add legend
plt.legend(fontsize=12)

plt.savefig('WindDataSet_2021-2024March.png')
plt.show()
