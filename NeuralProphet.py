import pandas as pd
import matplotlib.pyplot as plt
from neuralprophet import NeuralProphet, set_log_level
import kaleido

set_log_level("ERROR")

PATH = r"C:\Users\Jesus\Downloads\Book1.csv"

df = pd.read_csv(PATH)
df["ds"] = pd.to_datetime(df["ds"], errors="coerce")
df["y"] = pd.to_numeric(df["y"], errors="coerce")
# df["RAFAGA DEL VIENTO (Km/h):"] = pd.to_numeric(df["RAFAGA DEL VIENTO (Km/h):"], errors="coerce")


#plt = df.plot(x="ds", y="y", figsize=(15, 5))
# plt = df.plot(x="ds", y="y", figsize=(15, 5))

# plt.plot(df["ds"], df["y"])
# plt.xlabel("Tiempo")
# plt.ylabel("y")
# plt.title("Velocidad del Viento en función del Tiempo")
# plt.grid(True)
# plt.savefig("wind_speed_plot.png")
# plt.show()

duplicates = df.duplicated(subset=["ds"])

# If duplicates are found, drop them
if duplicates.any():
    df = df[~duplicates]

m = NeuralProphet()
m.set_plotting_backend("plotly-static")
metrics = m.fit(df)
df_future = m.make_future_dataframe(df, n_historic_predictions=True, periods=60)
forecast = m.predict(df_future)
m.plot(forecast)
