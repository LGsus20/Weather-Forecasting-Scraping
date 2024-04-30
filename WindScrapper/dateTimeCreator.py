import csv
from datetime import datetime, timedelta

start_datetime = datetime(2024, 3, 11, 0, 0)
filename = "datetime_values.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    current_datetime = start_datetime
    for _ in range(960):
        writer.writerow([current_datetime.strftime("%m/%d/%Y %H:%M")])
        current_datetime += timedelta(hours=1)

print("CSV file created successfully.")
