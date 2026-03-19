import pandas as pd
from models.user_based import build_user_similarity, recommend_user_based
from models.item_based import build_item_similarity, recommend_item_based
from models.hybrid import compute_popularity, recommend_hybrid
from agents.decision_agent import decision_agent
from agents.cold_start_agent import cold_start_agent

# -------------------------
# Load datasets
# -------------------------

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
        "drama", "fantasy", "film_noir", "horror", "musical", "mystery",
        "romance", "sci_fi", "thriller", "war", "western"
    ]
)

# -------------------------
# Create user-item matrix
# -------------------------
train_user_item = ratings.pivot(
    index="user_id",
    columns="movie_id",
    values="rating"
).fillna(0)

# -------------------------
# Build similarity matrices
# -------------------------
user_similarity_df = build_user_similarity(train_user_item)
item_similarity_df = build_item_similarity(train_user_item)

# -------------------------
# Compute popularity scores
# -------------------------
popularity_scores = compute_popularity(ratings)

# -------------------------
# Agentic Recommendation with Genre Filter
# -------------------------
def recommendation_agent(user_id, top_n=5, genre=None):

    cold = cold_start_agent(user_id, train_user_item, popularity_scores, top_n)
    if cold is not None:
        recs = cold
    else:
        model = decision_agent(user_id, train_user_item)
        print(f"\nAgent selected model: {model}")

        if model == "item_based":
            recs = recommend_item_based(
                user_id, train_user_item, item_similarity_df, top_n=top_n*3
            )

        elif model == "user_based":
            recs = recommend_user_based(
                user_id, train_user_item, user_similarity_df, top_n=top_n*3
            )

        else:
            cf_scores = train_user_item.loc[user_id]
            recs = recommend_hybrid(
                user_id, train_user_item, cf_scores, popularity_scores, top_n=top_n*3
            )

    # -------------------------
    # Genre filtering
    # -------------------------
    if genre is not None:
        if genre not in movies.columns:
            print("Invalid genre name!")
            return []

        recs = [
            movie for movie in recs
            if movies.loc[movies["movie_id"] == movie, genre].values[0] == 1
        ]

    return recs[:top_n]


# -------------------------
# Print recommendations
# -------------------------
def print_movie_recommendations(movie_ids):

    recommended_movies = movies[movies["movie_id"].isin(movie_ids)]

    print("\nRecommended Movies:")
    for _, row in recommended_movies.iterrows():
        genres = [col for col in movies.columns[5:] if row[col] == 1]
        genre_str = ", ".join(genres) if genres else "Unknown"

        print(f"{row['movie_id']}: {row['title']} ({row['release_date']})")
        print(f"   Genres: {genre_str}")
        print("-" * 50)


# -------------------------
# User Interaction
# -------------------------
if __name__ == "__main__":

    print("Available Genres:")
    print(", ".join(movies.columns[5:]))

    user_id = int(input("\nEnter User ID: "))
    genre_choice = input("Enter genre you want (or press Enter to skip): ").strip().lower()

    if genre_choice == "":
        genre_choice = None

    recommendations = recommendation_agent(user_id, top_n=5, genre=genre_choice)
    print_movie_recommendations(recommendations)