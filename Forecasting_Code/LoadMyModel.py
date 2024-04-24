from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA, AutoETS, AutoTheta, AutoCES
import pandas as pd
import numpy as np

PATH = r"C:\Users\Jesus\Downloads\forecasting\Weather-Forecasting-Scraping\Forecasting_Code\StatsForecast_2023-2024.pkl"
LAGS = 6

def LoadMyModel():

    season_length = 24 # Define season length as 24 hours for hourly data
    horizon = LAGS # Forecast horizon is set to 6 hours
    models = [
        AutoARIMA(season_length=season_length), # ARIMA model with automatic order selection and seasonal component
        AutoETS(season_length=season_length), # ETS model with automatic error, trend, and seasonal component
        AutoTheta(season_length=season_length), # Theta model with automatic seasonality detection
        AutoCES(season_length=season_length), # CES model with automatic seasonality detection
    ]

    sf = StatsForecast(
        models=models, # models for forecasting
        freq='h',  # frequency of the data
        n_jobs=-1  # number of jobs to run in parallel, -1 means using all processors
    )

    sf = StatsForecast.load(path=PATH)
    Y_hat_df = sf.predict(h=horizon).reset_index()
    print("Forecast of the models:")
    print(Y_hat_df.head(LAGS))

    return Y_hat_df

