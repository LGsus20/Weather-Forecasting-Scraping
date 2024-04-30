from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA, AutoETS, AutoTheta, AutoRegressive
import pandas as pd
import numpy as np
import winsound

PATH = r"C:\Users\Jesus\Downloads\forecasting\Weather-Forecasting-Scraping\Forecasting_Code\DATASET_Modified_Monthly_2022-2024.csv"

Y_df = pd.read_csv(PATH).assign(unique_id=np.ones(len(pd.read_csv(PATH))))
print("DATA:\n")
print(Y_df)


season_length = 24 # Define season length as 24 hours for hourly data
horizon = 6 # Forecast horizon is set to 6 hours

# Define a list of models for forecasting
models = [
    AutoARIMA(season_length=season_length), # ARIMA model with automatic order selection and seasonal component
    AutoRegressive(lags=6, include_mean=True),
    AutoTheta(season_length=season_length), # Theta model with automatic seasonality detection
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

sf.fit(df=Y_df)  # Fit the models to the data using the fit method of the StatsForecast object

Y_hat_df = sf.predict(h=horizon)  # Predict or forecast 'horizon' steps ahead using the predict method

print("Prediccion: \n")  # View First forecasted rows
print(Y_hat_df.head(6))

sf.save()

winsound.Beep(2500, 1000)
