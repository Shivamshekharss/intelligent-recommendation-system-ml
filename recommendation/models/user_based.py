import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def build_user_similarity(train_user_item):
    similarity = cosine_similarity(train_user_item)
    return pd.DataFrame(
        similarity,
        index=train_user_item.index,
        columns=train_user_item.index
    )

def recommend_user_based(user_id, train_user_item, user_similarity_df, top_n=5):

    if user_id not in train_user_item.index:
        return []

    user_sim = user_similarity_df[user_id].sort_values(ascending=False)
    user_sim = user_sim.drop(user_id)

    top_users = user_sim.head(10).index

    weighted_scores = pd.Series(dtype=float)

    for similar_user in top_users:
        similarity_score = user_sim[similar_user]
        ratings = train_user_item.loc[similar_user]
        weighted_scores = weighted_scores.add(ratings * similarity_score, fill_value=0)

    already_rated = train_user_item.loc[user_id]
    weighted_scores = weighted_scores[already_rated == 0]

    return weighted_scores.sort_values(ascending=False).head(top_n).index.tolist()