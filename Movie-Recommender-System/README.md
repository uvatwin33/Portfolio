# Movie-Recommender-System

# **Content-Based Movie Recommender System**

This project is a Python implementation of a content based movie recommender system with the well-known MovieLens datasets. There are two common types of recommender systems:

- **content-based recommender system** - relies on the similarity of movies when recommending the movies to users
- **collaborative recommender system –** recommends items based on how similar users liked the items.

This project is a hybrid in nature but mostly based on the content-based recommender.
#
**Packages Used**

- Numpy
- Pandas
- Re
- TfidfVectorizer
- Cosine\_similarity
- Ipywidgets
- Display

#
**Data**

- Movies.csv
- Ratings.csv

#
**Build Search Engine**

First, the titles of movies are converted into numeric variables, using 'term frequency' method or 'Tfid' vectorizer. And then, cosine similarity is used to build the recommender system by calculating the similarity between movies. Cosine similarity provides a way to measure how similar users, items, or content is (Stieber, 2018).

#
**Create A Movie Recommender System**

Another dataset 'ratings.csv' is used to find similar users by ratings. And then, create a content-based movie recommender based on finding users who are similar to you, finding only the movies greater than 10% or more of users who are similar to us, finding how much all of our users like movies rated highly, finding what percentage of all users who watch the recommended movies, creating score by recommendations from similar users divided by all, and displaying top ten movies.

#
**Widget for Movie Input**

A widget package 'ipywidgets' is used to take a user input and display output using an on-type function.

#
**Results**

When a movie title is input in the box, the recommender system displays 10 recommended movies that are similar to what you like.

#
**References:**

Paruchuri, V. (2022, May 27). _Movie Recommendation System With Python And Pandas: Data Project_ [Video]. Dataquest YouTube. [https://www.youtube.com/watch?v=eyEabQRBMQA](https://www.youtube.com/watch?v=eyEabQRBMQA)

Jeong, Y. (2021, April 5). Making a Content-Based Movie Recommender With Python. _Geek Culture_. [https://medium.com/geekculture/creating-content-based-movie-recommender-with-python-7f7d1b739c63](https://medium.com/geekculture/creating-content-based-movie-recommender-with-python-7f7d1b739c63)

Stieber, B. (2018, December 31). Recommending Songs Using Cosine Similarity in R. _Deeper Data Digressions_. [https://bgstieber.github.io/post/recommending-songs-using-cosine-similarity-in-r/](https://bgstieber.github.io/post/recommending-songs-using-cosine-similarity-in-r/)

**Copyright**

Portfolio photo credit: <a href="https://www.istockphoto.com">Image by iStock.com</a> on iStock by Getty Images

