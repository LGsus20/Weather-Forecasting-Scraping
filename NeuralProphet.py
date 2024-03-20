import pandas as pd
import matplotlib

PATH = r"C:\Users\Jesus\Downloads\Book1.csv"

df = pd.read_csv(PATH)
df["Tiempo:"] = pd.to_datetime(df["Tiempo:"], errors="coerce")
df["VELOCIDAD DEL VIENTO (Km/h):"] = pd.to_numeric(df["VELOCIDAD DEL VIENTO (Km/h):"], errors="coerce")
df["RAFAGA DEL VIENTO (Km/h):"] = pd.to_numeric(df["RAFAGA DEL VIENTO (Km/h):"], errors="coerce")


#plt = df.plot(x="ds", y="y", figsize=(15, 5))
plt = df.plot(x="Tiempo:", y="VELOCIDAD DEL VIENTO (Km/h):", figsize=(15, 5))


