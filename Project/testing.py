from textblob import TextBlob
import pandas as pd
# Create a TextBlob object
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    
    if sentiment_score > 0:
        return 'Positive'
    elif sentiment_score < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Read the CSV file
df = pd.read_csv('data.csv')

# Specify the product ID for analysis
product_id = 'AVqkIhwDv8e3D1O-lebb'

# Filter the dataframe for the specific product ID
df_product = df[df['product_id'] == product_id]

# Get the name of the product
product_name = df_product['name'].iloc[0]

# Apply the sentiment analysis function to each text in the filtered dataframe
df_product['sentiment'] = df_product['reviews.text'].apply(analyze_sentiment)

# Count the number of each sentiment
positive = (df_product['sentiment'] == 'Positive').sum()
negative = (df_product['sentiment'] == 'Negative').sum()
neutral = (df_product['sentiment'] == 'Neutral').sum()

print(f"The product with Name {product_name} has {positive} positive reviews, {negative} negative reviews, and {neutral} neutral reviews")