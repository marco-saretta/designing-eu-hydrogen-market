import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path 
import matplotlib.dates as mdates

data_dir = Path(__file__).resolve().parent.parent / 'data' / 'capacity.csv'

raw_data = pd.read_csv(data_dir, index_col=0, parse_dates=True)
df = raw_data.sort_index()
df.drop(columns=['periodTo', 'operatorLabel', 'pointLabel', 'directionKey', 'unit'], inplace=True)

# Pass to GW
df = df/1e6

# Prepare the plot
fig, axs = plt.subplots(ncols=1, nrows=2, figsize=(12, 6))

alpha = 0.7

# Plot lines
axs[0].plot(df.index, df['Firm technical'], color='teal', label='Firm technical')
axs[0].plot(df.index, df['Firm Available'], color='green', label='Firm Available')
axs[0].plot(df.index, df['Firm Booked'], color='red', label='Firm Booked')
axs[0].grid(alpha=alpha, linestyle=':')
##plt.xticks(rotation=45)
axs[0].legend(ncol=1)

axs[1].plot(df.index, df['Allocation'], label='Allocation')
axs[1].plot(df.index, df['Nomination'], label='Nomination')
axs[1].plot(df.index, df['Physical flow'], label='Physical flow')
axs[1].plot(df.index, df['Renomination'], label='Renomination')
axs[1].grid(alpha=alpha, linestyle=':')
axs[1].legend(ncol=1)

# Hide specific spines
for ax in axs:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Set y-axis limits
    ax.set_ylim(0, 9)

    # Set x-axis limits
    ax.set_xlim(df.index.min(), df.index.max())

    # Formatting
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d, %I%p'))
    ax.set_ylabel('GWh/h')

# Adjust layout
plt.tight_layout(pad=0)  # minimal internal padding

# Save the plot to file
out_path =  Path(__file__).resolve().parent.parent / 'figures' / 'capacity_booking.pdf'
fig.savefig(out_path, bbox_inches='tight')