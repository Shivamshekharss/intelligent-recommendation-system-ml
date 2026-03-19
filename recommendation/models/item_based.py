import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def build_item_similarity(train_user_item):
    item_matrix = train_user_item.T
    similarity = cosine_similarity(item_matrix)
    return pd.DataFrame(
        similarity,
        index=item_matrix.index,
        columns=item_matrix.index
    )

def recommend_item_based(user_id, train_user_item, item_similarity_df, top_n=5):

    if user_id not in train_user_item.index:
        return []

    user_ratings = train_user_item.loc[user_id]
    rated_items = user_ratings[user_ratings > 0].index

    scores = pd.Series(dtype=float)

    for item in rated_items:
        similarity_scores = item_similarity_df[item]
        scores = scores.add(similarity_scores * user_ratings[item], fill_value=0)

    scores = scores.drop(rated_items)

    return scores.sort_values(ascending=False).head(top_n).index.tolist()