import torch
from datetime import datetime
from neuralforecast import NeuralForecast
from neuralforecast.models import LSTM, PatchTST
import pandas as pd
import numpy as np

print("Starting run, current time:", datetime.now().time())

PATH = r"https://raw.githubusercontent.com/LGsus20/Weather-Forecasting-Scraping/main/DATASETS/DATASET_Modified_Monthly_2021-2023.csv"
Y_df = pd.read_csv(PATH).assign(unique_id=np.ones(len(pd.read_csv(PATH))))
Y_df['ds'] = pd.to_datetime(Y_df['ds'])
print("DATA:\n")
print(Y_df)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print("Device:", device)

models = [
    PatchTST(input_size=216, h=6, max_steps=2000).to(device),
    LSTM(input_size=216, h=6, max_steps=2000).to(device)
]

nf = NeuralForecast(
    models=models,
    freq='h',
)

nf.fit(df=Y_df)

print(nf.predict())

nf.save("WindForecasting")

print("Finished, current time:", datetime.now().time())
