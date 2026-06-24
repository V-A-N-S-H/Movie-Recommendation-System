# Movie Recommendation System

A Content-Based Movie Recommendation System built with Python, Machine Learning, and Streamlit. This application recommends movies similar to the one selected by the user using cosine similarity and displays their posters using the TMDB API.

## Live Demo

Deployment:
https://movie-recommendation-system-mrs03.streamlit.app/

---

## Features

* Recommend top 5 similar movies
* Display movie posters using the TMDB API
* Fast content-based recommendation engine
* Interactive Streamlit web application
* Clean and user-friendly interface

---

## Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Requests
* Pickle
* TMDB API

---

## Project Structure

```text
Movie-Recommendation-System/
│
├── app.py                  # Streamlit application
├── main.ipynb              # Data preprocessing and model building
├── movie_dict.pkl          # Processed movie dataset
├── similarity.pkl          # Cosine similarity matrix
├── movies.csv              # Movie dataset
├── credits.csv             # Movie credits dataset
├── merged_data.csv         # Merged dataset
├── requirements.txt        # Required Python packages
├── Procfile                # Deployment configuration
├── setup.sh                # Streamlit configuration
├── .gitignore
├── .gitattributes
└── README.md
```

---

## How It Works

1. Load and preprocess the movie dataset.
2. Extract important movie features such as:

   * Genres
   * Keywords
   * Cast
   * Crew
   * Overview
3. Combine these features into a single text representation.
4. Convert text into vectors using CountVectorizer.
5. Compute Cosine Similarity between all movies.
6. When a movie is selected, retrieve the five most similar movies.
7. Fetch movie posters dynamically using the TMDB API.

---

## Dataset

The project uses the TMDB Movie Dataset containing movie information and credits.

Datasets:

* movies.csv
* credits.csv

These datasets are merged and processed before training the recommendation model.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/V-A-N-S-H/Movie-Recommendation-System.git
```

### 2. Navigate to the project directory

```bash
cd Movie-Recommendation-System
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

---

## Recommendation Algorithm

This project uses a Content-Based Filtering approach.

The recommendation model is built using:

* Feature Engineering
* CountVectorizer
* Cosine Similarity

Movies with similar content are recommended based on their feature vectors.

---

## Future Improvements

* User authentication
* Collaborative filtering
* Hybrid recommendation system
* Search autocomplete
* Movie trailers
* Genre-based filtering
* User ratings and reviews
* Deploy with Docker

---

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## Author

**Vansh**

GitHub: https://github.com/V-A-N-S-H

---

## Support

If you found this project helpful, consider giving it a star on GitHub.
