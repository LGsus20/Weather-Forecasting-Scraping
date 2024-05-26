from statsforecast import StatsForecast
from statsforecast.models import HistoricAverage, SimpleExponentialSmoothing, SeasonalNaive, AutoRegressive, AutoTheta
import pandas as pd
import numpy as np

PATH = r"https://raw.githubusercontent.com/LGsus20/Weather-Forecasting-Scraping/main/DATASETS/DATASET_Modified_Monthly_2021-2023.csv"

Y_df = pd.read_csv(PATH).assign(unique_id=np.ones(len(pd.read_csv(PATH))))
print("DATA:\n")
print(Y_df)


season_length = 24 # Define season length as 24 hours for hourly data
horizon = 6 # Forecast horizon is set to 6 hours

# Define a list of models for forecasting
models = [
    AutoRegressive(lags=1, include_mean=True),
    HistoricAverage(),
    SeasonalNaive(season_length=season_length),
    SimpleExponentialSmoothing(alpha=0.1)
]

# Instantiate StatsForecast class with models, data frequency ('h' for hourly),
# and parallel computation on all CPU cores (n_jobs=-1)
sf = StatsForecast(
    models=models, # models for forecasting
    freq='h',  # frequency of the data
    n_jobs=6  # number of jobs to run in parallel, -1 means using all processors
)

# Generate forecasts for the specified horizon using the sf object
Y_hat_df = sf.forecast(df=Y_df, h=horizon) # forecast data
# Display the first few rows of the forecast DataFrame
print(Y_hat_df.head()) # preview of forecasted data
