# Music-Recommender
A lightweight music recommendation system built using Flask and a simple machine learning model. The system reads a dataset of songs and predicts popularity scores, then sorts songs within a selected genre to recommend the top results.

# Functionality
1-Loads track data from a CSV file  
2-Trains a Linear Regression model to predict popularity using audio feature columns  
3-Filters tracks by genre and generates ranked recommendations  
4-Uses a custom Merge Sort implementation for ordering songs by predicted score  
5-Flask backend with an interactive web interface for user selection

# Tools and Libraries used
Python  
Flask  
scikit learn  
pandas  
HTML with template rendering  
CSS for UI styling  

# How it functions
The model uses the aspects like danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, and tempo. When a user selects a genre, the backend predicts scores for all songs within that genre and returns the top recommended tracks. The frontend displays them in an interactive UI format.

# How to run
1-Install dependencies
2-Run app.py
3-Open the local server in browser and select a genre to receive recommendations

# Structure overview

app.py contains backend routes and API for recommendations  
model.py contains data loading, model training and merge sorting logic  
templates folder contains index.html for rendering UI  
static folder contains CSS styling for a glass effect theme  
Data folder contains the music dataset used for training (This data has been trimmed to a smaller number in order to save space, and respresents the actual format)
