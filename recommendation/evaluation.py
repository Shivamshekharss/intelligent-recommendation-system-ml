import numpy as np

def precision_recall_at_k(recommend_func, test_data, top_n=5):

    precisions = []
    recalls = []

    test_users = test_data["user_id"].unique()

    for user in test_users:

        relevant_items = test_data[
            test_data["user_id"] == user
        ]["movie_id"].tolist()

        if user not in train_user_item.index:
            continue

        recommended = recommend_func(user, top_n)

        if len(recommended) == 0:
            continue

        hits = len(set(recommended) & set(relevant_items))

        precision = hits / top_n
        recall = hits / len(relevant_items)

        precisions.append(precision)
        recalls.append(recall)

    return np.mean(precisions), np.mean(recalls)