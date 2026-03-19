import pandas as pd

# Load the original MovieLens file (adjust path if needed)
ratings = pd.read_csv(
    "../data/ml-100k/u.data",  # Change this if your data folder is somewhere else
    sep="\t",
    names=["user_id", "movie_id", "rating", "timestamp"]
)

# Save as CSV in the recommendation folder
ratings.to_csv("ratings.csv", index=False)
print("ratings.csv created successfully!")