from textblob import TextBlob
import pandas as pd
def analyzeSentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    
    if sentiment_score > 0:
        return 'Positive'
    elif sentiment_score < 0:
        return 'Negative'
    else:
        return 'Neutral' 
df = pd.read_csv('data.csv')

product_id = 'AVqkIhwDv8e3D1O-lebb' #or any id you want to search for 

df_product = df[df['product_id'] == product_id]

product_name = df_product['name'].iloc[0]

df_product['sentiment'] = df_product['reviews.text'].apply(analyze_sentiment)

positive = (df_product['sentiment'] == 'Positive').sum()
negative = (df_product['sentiment'] == 'Negative').sum()
neutral = (df_product['sentiment'] == 'Neutral').sum()

print(f"The product with Name {product_name} has {positive} positive reviews, {negative} negative reviews, and {neutral} neutral reviews")
