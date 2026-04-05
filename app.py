from flask import Flask, render_template, request
import os
import pandas as pd

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "movies.csv")

try:
    movies = pd.read_csv(file_path, encoding='latin-1')
except Exception as e:
    movies = pd.DataFrame()
    print("Error loading CSV:", e)

def recommend(movie):
    if 'title' not in movies.columns:
        return ["Column 'title' not found in dataset"]

    if movie not in movies['title'].values:
        return ["Movie not found"]

    # just return first 5 movies (stable)
    return list(movies['title'].head(5))


@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []

    movie_list = []
    if 'title' in movies.columns:
        movie_list = movies['title'].values

    if request.method == "POST":
        selected_movie = request.form.get("movie")
        recommendations = recommend(selected_movie)

    return render_template("index.html",
                           movies=movie_list,
                           recommendations=recommendations)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
