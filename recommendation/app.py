import streamlit as st
import pandas as pd
import sys

st.set_page_config(page_title="Movie Recommender", layout="wide")

# -------------------------
# Load Dataset
# -------------------------
@st.cache_data
def load_data():
    ratings = pd.read_csv(
        "../data/ml-100k/u.data",
        sep="\t",
        names=["user_id", "movie_id", "rating", "timestamp"]
    )

    movies = pd.read_csv(
        "../data/ml-100k/u.item",
        sep="|",
        encoding="latin-1",
        header=None,
        names=[
            "movie_id", "title", "release_date", "video_release_date", "imdb_url", "unknown",
            "action", "adventure", "animation", "children", "comedy", "crime", "documentary",
            "drama", "fantasy", "film_noir", "horror", "musical", "mystery", "romance",
            "sci_fi", "thriller", "war", "western"
        ]
    )

    return ratings, movies

ratings, movies = load_data()

# -------------------------
# UI
# -------------------------
st.title("🎬 Intelligent Movie Recommendation System")

st.sidebar.header("Choose Recommendation Mode")

mode = st.sidebar.radio(
    "Recommendation Type",
    ["By User ID", "By Genre"]
)

top_n = st.sidebar.slider("Number of Recommendations", 1, 10, 5)

# -------------------------
# GENRE BASED
# -------------------------
if mode == "By Genre":

    genre_list = [
        "action", "adventure", "animation", "children", "comedy", "crime",
        "documentary", "drama", "fantasy", "film_noir", "horror",
        "musical", "mystery", "romance", "sci_fi", "thriller", "war", "western"
    ]

    selected_genre = st.sidebar.selectbox("Select Genre", genre_list)

    if st.sidebar.button("Recommend Movies"):

        genre_movies = movies[movies[selected_genre] == 1]

        # Sort by popularity (average rating)
        avg_ratings = ratings.groupby("movie_id")["rating"].mean()
        genre_movies = genre_movies.merge(avg_ratings, on="movie_id")
        genre_movies = genre_movies.sort_values(by="rating", ascending=False)

        st.subheader(f"Top {top_n} {selected_genre.capitalize()} Movies")

        for _, row in genre_movies.head(top_n).iterrows():
            st.markdown(f"### 🎥 {row['title']}")
            st.write(f"Release Date: {row['release_date']}")
            st.write(f"Average Rating: {round(row['rating'],2)}")
            st.markdown("---")

# -------------------------
# USER BASED (Simple Version)
# -------------------------
else:

    user_id = st.sidebar.number_input("Enter User ID", min_value=1, max_value=943, value=1)

    if st.sidebar.button("Recommend Movies"):

        # Simple popularity fallback
        avg_ratings = ratings.groupby("movie_id")["rating"].mean()
        top_movies = avg_ratings.sort_values(ascending=False).head(top_n)

        recommended = movies[movies["movie_id"].isin(top_movies.index)]

        st.subheader(f"Top Movies for User {user_id}")

        for _, row in recommended.iterrows():
            genres = [col for col in movies.columns[5:] if row[col] == 1]
            st.markdown(f"### 🎥 {row['title']}")
            st.write(f"Genres: {', '.join(genres)}")
            st.markdown("---")