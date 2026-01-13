from flask import Flask, render_template, request, jsonify
from model import MusicRecommender
import os

app = Flask(
    __name__,
    template_folder=r"C:\Users\ACER\OneDrive\Desktop\College\DAA_AAT\Backend\templates",
    static_folder=r"C:\Users\ACER\OneDrive\Desktop\College\DAA_AAT\Backend\static"
)

recommender = MusicRecommender(csv_path=r'C:\Users\ACER\OneDrive\Desktop\College\DAA_AAT\Backend\Data\music.csv')

@app.route('/')
def index():
    genres = sorted(recommender.df['track_genre'].dropna().unique())
    return render_template('index.html', genres=genres)

@app.route('/recommend', methods=['POST'])
def recommend():
    genre = request.json.get('genre')
    recommendations = recommender.recommend(genre)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
