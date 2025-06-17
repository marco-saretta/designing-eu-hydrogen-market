import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path 
import matplotlib.dates as mdates

data_dir = Path(__file__).resolve().parent.parent / 'data' / 'data.csv'
raw_data = pd.read_csv(data_dir, index_col=0, parse_dates=True)
df = raw_data.sort_index()

# Pass to GW
df = df/1e6

# Display March only 
df = df[df.index.month == 4]

# Prepare the plot
fig, ax = plt.subplots(figsize=(16, 6))

green_zone_color = '#60D394'
light_green_zone = '#ffd87d'
orage_zone_color = '#f79c69'
red_zone_color = '#EE6055'
alpha = 0.7

# Background shaded zones
ax.fill_between(df.index, df['Red Border Min (kWh)'], df['Orange Border Min (kWh)'], color=red_zone_color, alpha=alpha, label = 'Red zone')
ax.fill_between(df.index, df['Orange Border Min (kWh)'], df['Light Green Border Min (kWh)'], color=orage_zone_color, alpha=alpha, label = 'Orange zone')
ax.fill_between(df.index, df['Light Green Border Min (kWh)'], df['Green Border Min (kWh)'], color=light_green_zone, alpha=alpha, label = 'Yellow zone')
ax.fill_between(df.index, df['Green Border Min (kWh)'], df['Green Border Max (kWh)'], color=green_zone_color, alpha=alpha, label = 'Green zone')
ax.fill_between(df.index, df['Green Border Max (kWh)'], df['Light Green Border Max (kWh)'], color=light_green_zone, alpha=alpha)
ax.fill_between(df.index, df['Light Green Border Max (kWh)'], df['Orange Border Max (kWh)'], color=orage_zone_color, alpha=alpha)
ax.fill_between(df.index, df['Orange Border Max (kWh)'], df['Red Border Max (kWh)'], color=red_zone_color, alpha=alpha)

ax.axhline(y=0, color='grey', linestyle='dashed', alpha = 0.4, linewidth = '0.8', label='SBS equilibrium')

# Plot lines
ax.plot(df.index, df['SBS Position (kWh)'], color='black', marker='^', label='SBS Position')
ax.plot(df.index, df['Sum Causers (kWh)'], color='red', label='Sum Causers')
ax.plot(df.index, df['Sum Helpers (kWh)'], color='teal', label='Sum Helpers')

# Hide specific spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Set y-axis limits
ax.set_ylim(-70, 70)

# Set x-axis limits
ax.set_xlim(df.index.min(), df.index.max())

# Formatting
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d, %I%p'))
ax.set_ylabel('GWh')
#plt.xticks(rotation=45)
ax.legend(ncol=2, loc='upper right')

# Adjust layout
plt.tight_layout(pad=0)  # minimal internal padding

# Save the plot to file
out_path = Path(__file__).resolve().parent.parent / 'figures' / 'SBS_plot.pdf'
fig.savefig(out_path, bbox_inches='tight')

# If you want to display it directly, use plt.show()
plt.show()