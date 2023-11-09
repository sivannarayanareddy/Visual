import pandas as pd
import matplotlib.pyplot as plt

# Load the listings data
listings_df = pd.read_csv('listings.csv')

# Select the columns for the scatterplot
x_values = listings_df['review_scores_rating']
y_values = listings_df['price']

# Create a scatterplot
plt.figure(figsize=(10, 6))
plt.scatter(x_values, y_values, alpha=0.5, color='blue')

# Set plot labels and title
plt.xlabel('Review Scores Rating')
plt.ylabel('Price')
plt.title('Scatterplot of Review Scores Rating vs. Price')

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()
