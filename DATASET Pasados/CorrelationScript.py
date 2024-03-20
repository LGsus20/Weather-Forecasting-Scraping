import pandas as pd

# Read data from Excel file
data = pd.read_excel(r"C:\Users\Jesus\Downloads\DATASET-2023-clima (1).xlsx")
df = pd.DataFrame(data)

# Choose the columns for which you want to calculate autocorrelation
column_name1 = 'VELOCIDAD DEL VIENTO (Km/h):'  # Replace 'your_first_column_name' with the actual first column name
column_name2 = 'RAFAGA DEL VIENTO (Km/h):'  # Replace 'your_second_column_name' with the actual second column name

# Calculate autocorrelation between the chosen columns
autocorrelation = df[column_name1].autocorr(df[column_name2])

# Save the autocorrelation to a .txt file
with open(r"C:\Users\Jesus\Downloads\autocorrelation_result.txt", 'w') as file:
    file.write(f"Autocorrelation between {column_name1} and {column_name2}: {autocorrelation:.3f}")

print(f"Autocorrelation between {column_name1} and {column_name2}: {autocorrelation:.3f}")

