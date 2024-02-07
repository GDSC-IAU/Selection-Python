# Sentiment Analyzer 🚀

## Table of Contents 📋

- [Sentiment Analyzer 🚀](#sentiment-analyzer-)
  - [Table of Contents 📋](#table-of-contents-)
  - [Introduction 🌐](#introduction-)
  - [Dependencies 📌](#dependencies-)
  - [Installation ⚙️](#installation-️)

## Introduction 🌐

Text Sentiment Analyzer is a Python application with a purpose of analyzing the sentiment on a large dataset of product reviews, with a focus on a specific singular product: the All-New Fire HD 8 Tablet, with 8 HD Display, Wi-Fi, and 16 GB Ram.  It uses the TextBlob library such that the application takes a string input and returns a sentiment score and a sentiment label. The sentiment analyzer function employs a simple rule-based classifier applying a set of predefined rules (i.e., a threshold on the polarity value) to classify the sentiment which categorizes each review as good, negative, or neutral based on the language of the reviews. A few statistics regarding the reviews are also computed by the algorithm and their results were then analyzed and displayed in multiple graphs, these statistics include the polarity and average length of positive and negative reviews. Further, the code uses lambda functions as to be able to efficiently apply the sentiment analyzer and TextBlob library to each review in the dataset, without having to write a separate function for each operation.

## Dependencies 📌

This code requires the following libraries:

• pandas

• numpy

• matplotlib

• seaborn

• textblob

The code begins by reading a dataset from a CSV file and selecting the relevant columns. It then extracts all the reviews for the product and calculates some basic statistics about the data, such as the number of columns and rows, and the length of the shortest review. The code uses lambda functions to apply the sentiment analyzer to each review in the dataset, in particular, the line ```productDF['review_polarity'] = productDF['review_text'].apply(lambda x: TextBlob(x).sentiment.polarity)``` uses a lambda function to calculate the polarity of each review in the review_text column. The lambda function takes in a review text as input, and returns the polarity of the text as calculated by the TextBlob library's sentiment.polarity attribute.

Similarly, the line ```productDF['review_category'] = productDF['review_text'].apply(lambda x: sentimentAnalyzer(x))``` uses a lambda function to apply the sentiment analyzer to each review in the dataset. The lambda function takes in a review text as input, and returns the sentiment category of the text as calculated by the sentimentAnalyzer function. The results were plotted and visualized as a Histogram and a Pie chart.

The code then identifies false positives and false negatives in the sentiment analysis. A false positive is a review that has a positive sentiment but a rating less than 3. A false negative is a review that has a negative sentiment but a rating greater than 4. The code calculates the average polarity of false positives and false negatives, and the average length of false positives and false negatives.

## Installation ⚙️

To install this project, simply clone the repository and run the `sentimentAnalyzer` function with a string of text as input. The function will return the sentiment of the text as a string.
