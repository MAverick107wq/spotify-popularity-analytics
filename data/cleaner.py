import pandas as pd

# Load dataset
df = pd.read_excel("dataset.xlsx", sheet_name="dataset")

# Basic overview
print("Shape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nHead")
print(df.head())

# Row count
print("\nRow count")
print(len(df))

# Column descriptions
column_descriptions = {
    "Unnamed: 0": "Exported row index, not a meaningful feature",
    "track_id": "Spotify track identifier",
    "artists": "Artist or artists associated with the track",
    "album_name": "Album name",
    "track_name": "Track name",
    "popularity": "Spotify popularity score from 0 to 100",
    "duration_ms": "Track duration in milliseconds",
    "explicit": "Whether the track is explicit",
    "danceability": "Danceability score from 0 to 1",
    "energy": "Energy score from 0 to 1",
    "key": "Musical key encoded numerically",
    "loudness": "Track loudness in decibels",
    "mode": "Track mode encoded numerically",
    "speechiness": "Speechiness score from 0 to 1",
    "acousticness": "Acousticness score from 0 to 1",
    "instrumentalness": "Instrumentalness score from 0 to 1",
    "liveness": "Liveness score from 0 to 1",
    "valence": "Valence score from 0 to 1",
    "tempo": "Tempo in beats per minute",
    "time_signature": "Time signature",
    "track_genre": "Genre label"
}

print("\nColumn descriptions")
for col, desc in column_descriptions.items():
    print(col, "-", desc)

# Missing values
print("\nMissing values by column")
print(df.isnull().sum().sort_values(ascending=False))

# Duplicate rows
print("\nDuplicate rows")
print(df.duplicated().sum())

# Duplicate track IDs
print("\nDuplicate track_id values")
print(df["track_id"].duplicated().sum())

# Duplicate combinations of key identifiers
print("\nDuplicate rows based on track_id, artists, track_name")
print(df[["track_id", "artists", "track_name"]].duplicated().sum())

# Check whether Unnamed: 0 is just a sequential index
print("\nUnnamed: 0 is sequential index")
print(df["Unnamed: 0"].equals(pd.Series(range(len(df)))))

# Range and validity checks
quality_checks = {
    "popularity_outside_0_100": ((df["popularity"] < 0) | (df["popularity"] > 100)).sum(),
    "danceability_outside_0_1": ((df["danceability"] < 0) | (df["danceability"] > 1)).sum(),
    "energy_outside_0_1": ((df["energy"] < 0) | (df["energy"] > 1)).sum(),
    "speechiness_outside_0_1": ((df["speechiness"] < 0) | (df["speechiness"] > 1)).sum(),
    "acousticness_outside_0_1": ((df["acousticness"] < 0) | (df["acousticness"] > 1)).sum(),
    "instrumentalness_outside_0_1": ((df["instrumentalness"] < 0) | (df["instrumentalness"] > 1)).sum(),
    "liveness_outside_0_1": ((df["liveness"] < 0) | (df["liveness"] > 1)).sum(),
    "valence_outside_0_1": ((df["valence"] < 0) | (df["valence"] > 1)).sum(),
    "duration_ms_non_positive": (df["duration_ms"] <= 0).sum()
}

print("\nData quality checks")
for check_name, result in quality_checks.items():
    print(check_name, "-", result)