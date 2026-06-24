import streamlit as st
import pickle
import pandas as pd
import requests


# Fetch movie poster from TMDB
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8a9d3c8957241138878b8e163e577ffe&language=en-US"
    for _ in range(3):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('poster_path'):
                    return "https://image.tmdb.org/t/p/w500" + data['poster_path']
                break  # If successful but no poster_path, exit retry loop
        except Exception as e:
            print(f"Error fetching poster: {e}")
            continue  # Retry on connection errors
    
    return "https://placehold.co/500x750/png?text=No+Poster"


# Recommendation Function
def recommend(movie_name):
    movie_name = movie_name.lower().strip()

    matches = movies[movies['title'].str.lower() == movie_name]

    if matches.empty:
        return [], []

    movie_index = matches.index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(
            movies.iloc[i[0]].title
        )

        recommended_posters.append(
            fetch_poster(movie_id)
        )

    return recommended_movies, recommended_posters


# Load Data
movies_dict = pickle.load(
    open('movie_dict.pkl', 'rb')
)

movies = pd.DataFrame(movies_dict)

similarity = pickle.load(
    open('similarity.pkl', 'rb')
)


# Streamlit UI
st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Select a Movie",
    movies['title'].values
)

if st.button("Recommend"):

    names, posters = recommend(
        selected_movie_name
    )

    if len(names) == 0:
        st.error("Movie not found!")
    else:

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.text(names[0])
            st.image(posters[0])

        with col2:
            st.text(names[1])
            st.image(posters[1])

        with col3:
            st.text(names[2])
            st.image(posters[2])

        with col4:
            st.text(names[3])
            st.image(posters[3])

        with col5:
            st.text(names[4])
            st.image(posters[4])