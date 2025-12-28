import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Read the CSV file
df = pd.read_csv('signal_data.csv')

print(f"Data shape: {df.shape}")
print(f"Time range: {df['UTC Time'].iloc[0]} to {df['UTC Time'].iloc[-1]}")
print(f"Power range: {df['Signal Power (dB)'].min():.2f} to {df['Signal Power (dB)'].max():.2f} dB")

# Convert UTC Time to datetime
df['UTC Time'] = pd.to_datetime(df['UTC Time'])

# Extract power values
power_values = df['Signal Power (dB)'].values

# Reshape into 2D grid (time bins x frequency bins)
# Adjust grid_width to change aspect ratio of heatmap
grid_width = int(np.sqrt(len(power_values)))  # Square grid
grid_height = len(power_values) // grid_width

# Trim data to fit grid
trimmed_length = grid_width * grid_height
power_grid = power_values[:trimmed_length].reshape(grid_height, grid_width)

# Create heatmap
fig, ax = plt.subplots(figsize=(14, 8))

# Plot heatmap
im = ax.imshow(power_grid, cmap='viridis', aspect='auto', origin='lower', 
               interpolation='bilinear')

# Labels and title
ax.set_xlabel('Frequency Bin', fontsize=12)
ax.set_ylabel('Time Bin', fontsize=12)
ax.set_title('2D Heat Map: Signal Power Over Time', fontsize=14, fontweight='bold')

# Add colorbar
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Signal Power (dB)', fontsize=12)

# Add grid
ax.grid(True, alpha=0.3, linestyle='--')

plt.tight_layout()
plt.savefig('heatmap.png', dpi=150, bbox_inches='tight')
print("\n✓ Heat map saved as 'heatmap.png'")

# Create alternative: Time-series plot with color gradient
fig2, ax2 = plt.subplots(figsize=(14, 6))

# Create scatter plot with color based on power
scatter = ax2.scatter(range(len(power_values)), power_values, 
                     c=power_values, cmap='plasma', s=20, alpha=0.7)

ax2.set_xlabel('Measurement Index', fontsize=12)
ax2.set_ylabel('Signal Power (dB)', fontsize=12)
ax2.set_title('Signal Power Over Time (Color-Coded)', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3)

cbar2 = plt.colorbar(scatter, ax=ax2)
cbar2.set_label('Signal Power (dB)', fontsize=12)

plt.tight_layout()
plt.savefig('power_timeline.png', dpi=150, bbox_inches='tight')
print("✓ Timeline plot saved as 'power_timeline.png'")

plt.show()
