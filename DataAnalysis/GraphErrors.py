import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
file_path = r"C:\Users\Jesus\Downloads\forecasting\Weather-Forecasting-Scraping\Forecasting_Code\recordedValues.csv"
data = pd.read_csv(file_path)

# Convert 'ds' column to datetime
data['ds'] = pd.to_datetime(data['ds'])

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(data['ds'], data['RealVal'], label='RealVal', marker=',')
plt.plot(data['ds'], data['PatchTST'], label='PatchTST', marker='.', color='green')
#plt.plot(data['ds'], data['LSTM'], label='LSTM', marker='.')

plt.xlabel('Datetime')
plt.ylabel('Values')
plt.title('Comparison of real values and PatchTST')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
