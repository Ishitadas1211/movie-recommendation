# Movie Recommendation System

## Project Overview

This project is a **Movie Recommendation System** built using Machine Learning.
It suggests movies based on similarity using content-based filtering.


## Features

* Select a movie from a dropdown list
* Get top 5 similar movie recommendations
* Simple and user-friendly web interface
* Built using Flask and Python


## Technologies Used

* Python
* Pandas
* Scikit-learn
* Flask
* HTML


## How It Works

1. Movie dataset is loaded
2. Features like overview and genres are combined
3. Text is converted into vectors using CountVectorizer
4. Cosine similarity is calculated
5. Similar movies are recommended


## Project Structure

movie_project/
│
├── app.py
├── movies.csv
├── requirements.txt
└── templates/
└── index.html


## How to Run the Project

1. Install dependencies:

```
pip install flask pandas scikit-learn
```

2. Run the app:

```
python app.py
```

3. Open browser:

```
http://127.0.0.1:5000
```


## Deployment

The project can be deployed using platforms like:

* Render
* GitHub
* Hugging Face Spaces


## Future Improvements

* Add movie posters
* Improve UI design
* Use advanced recommendation algorithms
* Add search functionality


## Author

Ishita Das


## Conclusion

This project demonstrates how machine learning can be used to build a simple and effective recommendation system.

---
