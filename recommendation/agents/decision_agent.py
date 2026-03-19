def decision_agent(user_id, train_user_item, threshold=50):

    if user_id not in train_user_item.index:
        return "cold_start"

    rating_count = train_user_item.loc[user_id].count()

    if rating_count > threshold:
        return "item_based"
    elif rating_count > 10:
        return "user_based"
    else:
        return "hybrid"