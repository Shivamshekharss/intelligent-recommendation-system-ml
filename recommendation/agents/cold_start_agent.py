def cold_start_agent(user_id, train_user_item, popularity_scores, top_n=5):

    if user_id not in train_user_item.index:
        print("Cold-start detected → Using Popularity-Based")
        return popularity_scores.sort_values(ascending=False).head(top_n).index.tolist()

    return None