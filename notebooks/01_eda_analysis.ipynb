# EDA: totals, top genres, artist popularity + visualizations
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set(style="whitegrid", context="talk")

# Parameters
CLEANED_CSV = "spotify_clean.csv"   # path to cleaned dataset
MIN_TRACKS_FOR_ARTIST = 5           # minimum number of tracks to consider an artist for ranking
TOP_N = 10                          # top-N to display in genre charts

# Load data
df = pd.read_csv(CLEANED_CSV)

# Normalize string columns
if "track_genre" in df.columns:
    df["track_genre"] = df["track_genre"].fillna("Unknown").astype(str).str.strip()
df["artists"] = df["artists"].astype(str).str.strip()

# 1. Total songs
total_songs = len(df)

# 2. Total artists: explode multi-artist entries
# Many rows use ';' or ',' as separators; normalise to ';' then explode
artists_norm = df["artists"].str.replace(",", ";", regex=False)
artists_exploded = artists_norm.dropna().str.split(";").explode().str.strip()
artists_exploded = artists_exploded[artists_exploded != ""]   # drop empty tokens
total_artists = artists_exploded.nunique()

# 3. Total genres
total_genres = df["track_genre"].nunique() if "track_genre" in df.columns else 0

# 4. Average popularity
avg_popularity = df["popularity"].mean()

# 5. Most common genres (by count)
most_common_genres = df["track_genre"].value_counts().head(TOP_N)

# 6. Most popular genres (by average popularity)
if "track_genre" in df.columns:
    genre_stats = (
        df.groupby("track_genre")
          .agg(track_count=("track_id", "size"),
               avg_popularity=("popularity", "mean"))
          .sort_values(["avg_popularity", "track_count"], ascending=[False, False])
    )
    most_popular_genres = genre_stats.reset_index().head(TOP_N)
else:
    most_popular_genres = pd.DataFrame(columns=["track_genre", "track_count", "avg_popularity"])

# 7. Top artists by average popularity (explode artists, join popularity)
artists_df = (
    df[["popularity"]]
      .join(artists_norm.str.split(";").explode().rename("artist"))
)
artists_df["artist"] = artists_df["artist"].str.strip()
artists_df = artists_df[artists_df["artist"] != ""]

artist_summary = (
    artists_df.groupby("artist")
              .agg(track_count=("popularity", "count"),
                   avg_popularity=("popularity", "mean"))
              .reset_index()
              .sort_values(["avg_popularity", "track_count"], ascending=[False, False])
)
top_artists_by_avg_pop = artist_summary[artist_summary["track_count"] >= MIN_TRACKS_FOR_ARTIST].head(20)

# Print numeric summaries
print("Total songs:", total_songs)
print("Total unique artists:", total_artists)
print("Total genres:", total_genres)
print("Average popularity:", round(avg_popularity, 2))
print("\nMost common genres (top {})".format(TOP_N))
print(most_common_genres)
print("\nMost popular genres (top {}) by average popularity".format(TOP_N))
print(most_popular_genres[["track_genre", "track_count", "avg_popularity"]])
print("\nTop artists by average popularity (min_tracks={}):".format(MIN_TRACKS_FOR_ARTIST))
print(top_artists_by_avg_pop)

# -------------------------
# VISUALIZATIONS
# -------------------------
plt.figure(figsize=(10, 6))
ax = sns.barplot(x=most_common_genres.values, y=most_common_genres.index, palette="viridis")
ax.set_title("Top {} Most Common Genres (by track count)".format(TOP_N))
ax.set_xlabel("Number of Tracks")
ax.set_ylabel("Genre")
for i, v in enumerate(most_common_genres.values):
    ax.text(v + max(most_common_genres.values)*0.01, i, str(v), va="center")
plt.tight_layout()
plt.show()

# Most popular genres by average popularity
if not most_popular_genres.empty:
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x="avg_popularity", y="track_genre", data=most_popular_genres, palette="magma")
    ax.set_title("Top {} Genres by Average Popularity".format(TOP_N))
    ax.set_xlabel("Average Popularity")
    ax.set_ylabel("Genre")
    for i, row in most_popular_genres.iterrows():
        ax.text(row["avg_popularity"] + 0.5, i - most_popular_genres.index.min(), str(int(row["track_count"])), va="center")
    plt.tight_layout()
    plt.show()

# Top artists by average popularity (bar)
plt.figure(figsize=(12, 8))
ax = sns.barplot(x="avg_popularity", y="artist", data=top_artists_by_avg_pop, palette="cubehelix")
ax.set_title("Top Artists by Average Popularity (min_tracks = {})".format(MIN_TRACKS_FOR_ARTIST))
ax.set_xlabel("Average Popularity")
ax.set_ylabel("Artist")
for p in ax.patches:
    width = p.get_width()
    ax.text(width + 0.5, p.get_y() + p.get_height() / 2, f"{width:.1f}", va="center")
plt.tight_layout()
plt.show()

# Popularity distribution
plt.figure(figsize=(10, 5))
sns.histplot(df["popularity"], bins=30, kde=True)
plt.title("Distribution of Track Popularity")
plt.xlabel("Popularity")
plt.tight_layout()
plt.show()

# Save summary CSVs for external use
most_common_genres.to_csv("most_common_genres.csv", header=["count"])
most_popular_genres.to_csv("most_popular_genres.csv", index=False)
top_artists_by_avg_pop.to_csv("top_artists_by_avg_pop.csv", index=False)

print("\nSaved summary CSVs: most_common_genres.csv, most_popular_genres.csv, top_artists_by_avg_pop.csv")