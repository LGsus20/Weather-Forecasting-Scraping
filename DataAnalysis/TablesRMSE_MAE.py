import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Data for RMSE and MAE
rmse_data = [
    ['PatchTST', 2.197199636408283],
    ['LSTM', 2.2272168372123335],
    ['PSO', 2.2287]
]
mae_data = [
    ['PatchTST', 1.5561490477558406],
    ['LSTM', 1.56134208053825],
    ['PSO', 1.5726]
]
columns_rmse = ['Model', 'RMSE']
columns_mae = ['Model', 'MAE']

# Create a figure with two subplots
fig, axes = plt.subplots(2, 1, figsize=(4, 3))

# RMSE Table
axes[0].xaxis.set_visible(False)
axes[0].yaxis.set_visible(False)
axes[0].set_frame_on(False)
rmse_table = axes[0].table(cellText=rmse_data, colLabels=columns_rmse, cellLoc='center', loc='center')
for i in range(len(columns_rmse)):
    cell = rmse_table[(0, i)]
    cell.set_text_props(weight='bold', color='black')
    cell.set_facecolor(mcolors.CSS4_COLORS['lightgrey'])

# MAE Table
axes[1].xaxis.set_visible(False)
axes[1].yaxis.set_visible(False)
axes[1].set_frame_on(False)
mae_table = axes[1].table(cellText=mae_data, colLabels=columns_mae, cellLoc='center', loc='center')
for i in range(len(columns_mae)):
    cell = mae_table[(0, i)]
    cell.set_text_props(weight='bold', color='black')
    cell.set_facecolor(mcolors.CSS4_COLORS['lightgrey'])

# Adjust layout
plt.tight_layout()

# Display the plot with the tables
plt.show()
