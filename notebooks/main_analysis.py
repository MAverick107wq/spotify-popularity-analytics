import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# 1. SETUP & THEME
sns.set_theme(style="darkgrid", context="talk", rc={
    "axes.facecolor": "#0f1112", "figure.facecolor": "#0b0c0d",
    "grid.color": "#212527", "text.color": "#e6eef3",
    "axes.labelcolor": "#e6eef3", "xtick.color": "#cbd5e1", "ytick.color": "#cbd5e1"
})

# 2. LOAD & CLEAN
# Automatically check where we are running
if os.path.exists("spotify_clean.csv"):
    df = pd.read_csv("spotify_clean.csv")
else:
    df = pd.read_csv("../data/spotify_clean.csv")

df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")
df["track_genre"] = df["track_genre"].fillna("Unknown")

# Set save path (Colab gets current folder, Local gets ../visuals/)
save_dir = "./" if os.path.exists("/content/") else "../visuals/"

# 3. ANALYSIS 1: POPULARITY DISTRIBUTION
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="popularity", bins=30, kde=True, color="#4c9f70")
plt.title("Distribution of Track Popularity")
plt.savefig(f"{save_dir}popularity_distribution.png", dpi=300, bbox_inches="tight")
plt.show() # Added show() so you can see it in Colab

# 4. ANALYSIS 2: TOP GENRES
genre_counts = df["track_genre"].value_counts().head(15)
plt.figure(figsize=(12, 8))
sns.barplot(x=genre_counts.values, y=genre_counts.index, palette="viridis")
plt.title("Top 15 Genres by Number of Tracks")
plt.savefig(f"{save_dir}top_genres.png", dpi=300, bbox_inches="tight")
plt.show()

# 5. ANALYSIS 3: TOP ARTISTS
artists_df = df[["popularity", "artists"]].copy()

# Fix: Explode correctly without creating duplicate index issues
artists_df = artists_df.assign(artist=artists_df["artists"].str.split(";")).explode("artist")
artists_df["artist"] = artists_df["artist"].str.strip()

# Now aggregate:
artist_stats = artists_df.groupby("artist").agg(
    track_count=("popularity", "count"), 
    avg_popularity=("popularity", "mean")
)

# Filter and Sort
top_artists = artist_stats[artist_stats["track_count"] >= 5].sort_values("avg_popularity", ascending=False).head(15)

# Plotting
plt.figure(figsize=(12, 9))
sns.barplot(x=top_artists["avg_popularity"], y=top_artists.index, palette="coolwarm_r")
plt.title("Top 15 Artists by Average Popularity (min 5 tracks)")
plt.savefig(f"{save_dir}top_artists.png", dpi=300, bbox_inches="tight")
plt.show()