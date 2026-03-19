import pandas as pd

# Compute popularity scores (average rating per movie)
def compute_popularity(train_ratings):
    return train_ratings.groupby("movie_id")["rating"].mean()

# Hybrid recommendation function
def recommend_hybrid(user_id,
                     train_user_item,
                     cf_scores,
                     popularity_scores,
                     alpha=0.7,
                     top_n=5):

    if user_id not in train_user_item.index:
        # Cold-start fallback
        return popularity_scores.sort_values(ascending=False).head(top_n).index.tolist()

    # Compute hybrid scores: weighted combination of CF and popularity
    hybrid_scores = alpha * cf_scores + (1 - alpha) * popularity_scores

    # Remove already rated items
    already_rated = train_user_item.loc[user_id]
    hybrid_scores = hybrid_scores[already_rated == 0]

    return hybrid_scores.sort_values(ascending=False).head(top_n).index.tolist()