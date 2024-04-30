from neuralforecast import NeuralForecast
from neuralforecast.models import NBEATS, LSTM
import pandas as pd
import numpy as np
from random import randint

PATH = r"C:\Users\Jesus\Downloads\forecasting\Weather-Forecasting-Scraping\Forecasting_Code\DATASET_Modified_Monthly_2022-2024.csv"
Y_df = pd.read_csv(PATH).assign(unique_id=np.ones(len(pd.read_csv(PATH))))
Y_df['ds'] = pd.to_datetime(Y_df['ds'])
#Y_df['ds'] = Y_df['ds'].astype(int)
print("DATA:\n")
print(Y_df)

nf = NeuralForecast(
    models = [NBEATS(input_size=216, h=6, max_steps=2000), LSTM(input_size=216, h=6, max_steps=2000)],
    freq = 'h'
)

nf.fit(df=Y_df)

print(nf.predict())

try:
    nf.save("WindForecasting.h5")
except:
    nf.save(f"WindForecasting{randint(1, 1000)}.h5")