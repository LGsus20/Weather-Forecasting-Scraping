from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA, AutoETS, AutoTheta, AutoCES

PATH = r"C:\Users\Jesus\Downloads\forecasting\Weather-Forecasting-Scraping\Forecasting_Code\StatsForecast_2022_2024.pkl"
# PATH = the route of your model/s, should end in .pkl

def LoadMyModel():
    LAGS = 6
    season_length = 24  # Define season length as 24 hours for hourly data
    horizon = LAGS  # How many hours will it predict?
    sf = StatsForecast.load(path=PATH)  # Load the model (your .pkl)
    Y_hat_df = sf.predict(h=horizon).reset_index()  # Predicts 6 lags

    print(Y_hat_df)
    return Y_hat_df  # Returns  results in pandas dataFrame
