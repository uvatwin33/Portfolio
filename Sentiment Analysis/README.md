# Movie Sentiment Analysis

**This project performs a sentiment analysis on the movie data using the TextBlob Sentiment Analyzer.**

#
**Packages Used**

- Pandas
- Numby
- Nltk
- TextBlob
- Sklearn
- MultinominalNB (Naïve Bayes)

#
**Part 1: Using the TextBlob Sentiment Analyzer**

We download a labeled training dataset from [Bag of Words Meets Bags of Popcorn | Kaggle](https://www.kaggle.com/c/word2vec-nlp-tutorial/data) and use TextBlob to classify each movie review as positive or negative. We assume that a polarity score greater than or equal to zero is a positive sentiment and less than 0 is a negative sentiment.

#
**Part 2: Prepping Text for a Custom Model**

We use the following steps to run our model to classify text:

- Convert all text to lowercase letters.
- Remove punctuation and special characters from the text.
- Remove stop words.
- Apply NLTK's PorterStemmer.
- Create a bag-of-words matrix from our stemmed text where each row is a word-count vector for a single movie review. Display dimensions of your bag-of-words matrix where the number of rows in your original dataframe.
- Create a term frequency-inverse document frequency (tf-idf) matrix from your stemmed text for your movie reviews. Display the dimensions of your tf-idf matrix, which should be the same as your bag-of-words matrix.

#
**Results**

The prediction of the logistic regression model on the test results in terms of accuracy score was 0.8892 whereas the training score was 0.9286. The confusion matrix for the test set predictions is as follows:

[[2187 313]

[241 2259]]

And the accuracy score from the confusion matrix for validation was 0.8892.

When a Navie Bayes Model was applied to, The confusion matrix for the test set predictions is as follows:

[[2168 332]

[364 2136]]

where the accuracy from the Naïve Bayes Classifier applied-confusion matrix was 0.8608.
