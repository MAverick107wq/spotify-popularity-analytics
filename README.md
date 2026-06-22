# Spotify Popularity Analytics

This project is an end-to-end data analysis pipeline designed to uncover patterns in music popularity. By processing track data, I identified key trends in genre distribution and artist performance, providing actionable insights into what drives a "successful" song.

## Project Highlights
* **Data Cleaning Pipeline:** Automated the handling of missing values and data type coercion to prepare 100k+ records for analysis.
* **Genre Analysis:** Mapped the top 15 genres by track volume to highlight distribution imbalances in the dataset.
* **Artist Performance:** Implemented a "Reliability Filter" (minimum of 5 tracks) to identify top-performing artists, successfully filtering out statistical noise from one-hit wonders.
* **Visualization:** Built a modular Python-based pipeline using `Seaborn` and `Matplotlib` to generate professional, dark-mode analytics.

## Tech Stack
* **Language:** Python
* **Libraries:** Pandas, Seaborn, Matplotlib, OS
* **Workflow:** Data Cleaning $\rightarrow$ Exploratory Data Analysis (EDA) $\rightarrow$ Visualization

## Dataset
The dataset used in this analysis is the **"Spotify Tracks Dataset"** sourced from Kaggle.
* **Source:** [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)
* **Instructions:** 1. Download the dataset from the Kaggle link above.
  2. Locate the file named `dataset.csv`.
  3. Rename it to `spotify_clean.csv` (or update the filename in `main_analysis.py`).
  4. Place this file into the `data/` folder in this repository.

## How to Run
1. Ensure your dataset `spotify_clean.csv` is in the `data/` directory.
2. Run the main analysis script:
   ```bash
   python notebooks/main_analysis.py









