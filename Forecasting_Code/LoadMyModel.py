from statsforecast import StatsForecast
from neuralforecast import NeuralForecast

horizon = 6

def LoadMyModel(new_data):
    MODEL_PATH = r"C:\Users\Jesus\Downloads\forecasting\Weather-Forecasting-Scraping\Forecasting_Code\StatsForecast_2021-2023.pkl"

    sf = StatsForecast.load(path=MODEL_PATH)
    Y_hat_df = sf.predict(h=horizon).reset_index()
    # Y_hat_df = sf.predict(X_df=new_data, h=horizon).reset_index()
    return Y_hat_df

def LoadMyNeuralModel(new_data):
    MODEL_PATH = "WindForecasting216hrs"
    nf2 = NeuralForecast.load(path=MODEL_PATH)
    Y_hat_df = nf2.predict(new_data).reset_index()
    return Y_hat_df
