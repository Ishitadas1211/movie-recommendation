from flask import Flask, render_template, request
import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load dataset

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "movies.csv")
movies = pd.read_csv(file_path, encoding='latin-1')

# Preprocessing
movies['overview'] = movies['overview'].fillna('')
movies['genres'] = movies['genres'].fillna('')
movies['tags'] = movies['overview'] + " " + movies['genres']
movies['tags'] = movies['tags'].apply(lambda x: x.lower())

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

# Similarity
similarity = cosine_similarity(vectors)

# Recommendation function
def recommend(movie):
    movie = movie.lower()
    index = movies[movies['title'].str.lower() == movie].index[0]
    distances = similarity[index]

    movie_list = sorted(list(enumerate(distances)),
                        reverse=True,
                        key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

@app.route("/", methods=["GET", "POST"])
def home():
    try:
        recommendations = []

        if request.method == "POST":
            selected_movie = request.form.get("movie")
            recommendations = recommend(selected_movie)

        return render_template("index.html",
                               movies=movies['title'].values,
                               recommendations=recommendations)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
