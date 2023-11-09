import pandas as pd
import matplotlib.pyplot as plt

# Load the listings data
listings_df = pd.read_csv('listings.csv')

# Select the 'price' column
price_data = listings_df['price']

# Create a histogram
plt.figure(figsize=(10, 6))
plt.hist(price_data, bins=30, edgecolor='k', color='skyblue')

# Set plot labels and title
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Price Distribution')

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()
