import pandas as pd
import matplotlib.pyplot as plt

# Putting the data
calendar_df = pd.read_csv('calendar.csv')

# Change it to datatime.
calendar_df['date'] = pd.to_datetime(calendar_df['date'])

# Changing the price to numbers
calendar_df['price'] = calendar_df['price'].str.replace('[\$,]', '', regex=True).astype(float)

# Average for the date
average_price_by_date = calendar_df.groupby('date')['price'].mean()

# Making the line plot
plt.figure(figsize=(12, 6))
plt.plot(average_price_by_date.index, average_price_by_date.values, marker='o', linestyle='-')

# The labels and title of the plots
plt.xlabel('Date')
plt.ylabel('Average Price')
plt.title('Average Price by Date')

# See the lin
plt.grid(True)
plt.tight_layout()
plt.show()
