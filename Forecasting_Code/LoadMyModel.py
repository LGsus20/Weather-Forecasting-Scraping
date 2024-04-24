from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA, AutoETS, AutoTheta, AutoCES

PATH = r"C:\Users\Jesus\Downloads\forecasting\Weather-Forecasting-Scraping\Forecasting_Code\StatsForecast_2023-2024.pkl"
# PATH = the route of your model/s, should end in .pkl
LAGS = 6

def LoadMyModel():

    season_length = 24 # Define season length as 24 hours for hourly data
    horizon = LAGS # How many hours will it predict?
    models = [
        AutoARIMA(season_length=season_length), # ARIMA model with automatic order selection and seasonal component
        AutoETS(season_length=season_length), # ETS model with automatic error, trend, and seasonal component
        AutoTheta(season_length=season_length), # Theta model with automatic seasonality detection
        AutoCES(season_length=season_length), # CES model with automatic seasonality detection
    ]

    sf = StatsForecast(
        models=models, # models for forecasting
        freq='h',  # frequency equals hourly
        n_jobs=-1  # number of jobs to run in parallel, -1 means using all processors but doesn't work for some reason
    )

    sf = StatsForecast.load(path=PATH) # Load the model (your .pkl)
    Y_hat_df = sf.predict(h=horizon).reset_index() # Predicts 6 lags

    return Y_hat_df # Returns  results in pandas dataFrame

