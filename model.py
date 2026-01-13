import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class MusicRecommender:
    def __init__(self, csv_path):  # <-- fixed constructor name here
        self.df = pd.read_csv(csv_path)
        self.model = LinearRegression()
        self._train_model()

    def _train_model(self):
        features = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 
                    'instrumentalness', 'liveness', 'valence', 'tempo']
        self.df.dropna(subset=features + ['popularity'], inplace=True)
        X = self.df[features]
        y = self.df['popularity']
        self.model.fit(X, y)

    def recommend(self, genre, top_n=10):
        filtered = self.df[self.df['track_genre'] == genre].copy()
        if filtered.empty:
            return []

        features = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 
                    'instrumentalness', 'liveness', 'valence', 'tempo']
        filtered['score'] = self.model.predict(filtered[features])
    
        songs = filtered.to_dict(orient='records')
        sorted_songs = self._merge_sort(songs)
        return sorted_songs[:top_n]

    def _merge_sort(self, songs):
        if len(songs) <= 1:
            return songs
        mid = len(songs) // 2
        left = self._merge_sort(songs[:mid])
        right = self._merge_sort(songs[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i]['score'] >= right[j]['score']:  # Descending
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
