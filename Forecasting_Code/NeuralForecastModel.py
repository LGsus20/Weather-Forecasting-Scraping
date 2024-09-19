import torch
from datetime import datetime
from neuralforecast import NeuralForecast
from neuralforecast.models import LSTM, PatchTST, Autoformer, VanillaTransformer, Informer
import pandas as pd
import numpy as np

print("Starting run, current time:", datetime.now().time())

PATH = r"C:\Users\Jesus\Downloads\forecasting\Weather-Forecasting-Scraping\DATASETS\DATASET_Modified_Monthly_2021-2024.csv"
Y_df = pd.read_csv(PATH).assign(unique_id=np.ones(len(pd.read_csv(PATH))))
Y_df['ds'] = pd.to_datetime(Y_df['ds'])
print("DATA:\n")
print(Y_df)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print("Device:", device)

models = [
    Autoformer(input_size=24, h=6, max_steps=500).to(device),
    PatchTST(input_size=24, h=6, max_steps=500).to(device),
    LSTM(input_size=24, h=6, max_steps=500).to(device),
    Informer(input_size=24, h=6, max_steps=500).to(device),
#    VanillaTransformer(input_size=24, h=6, max_steps=500).to(device),
]

nf = NeuralForecast(
    models=models,
    freq='h',
)

nf.fit(df=Y_df)

print(nf.predict())

nf.save("WindForecasting24hrs")

print("Finished, current time:", datetime.now().time())
