
# Movie Recommendation System

This is a Movie Recommendation System built using machine learning techniques. The system leverages content-based filtering using cosine similarity to recommend movies based on the input movie title. The system is deployed using **Streamlit** for a user-friendly interface.

## Features

- **Content-based Recommendations**: Recommends movies similar to the one entered by the user based on genres, cast, keywords, and other metadata.
- **Streamlit Web App**: The app is deployed online, providing an interactive UI for users to input a movie title and get recommendations.

## Project Overview

This project uses the following steps:

1. **Data Preprocessing**:
    - Data is extracted from two datasets: `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`.
    - The movie data is cleaned and transformed by extracting relevant features such as genres, keywords, cast, and crew.

2. **Cosine Similarity**:
    - A `CountVectorizer` is used to convert movie metadata (tags) into vectors.
    - **Cosine Similarity** is calculated between these vectors to determine how similar two movies are to each other.

3. **Model**:
    - A **NearestNeighbors** model is used to efficiently find the most similar movies based on the cosine similarity matrix.
    
4. **Streamlit Interface**:
    - The app provides a dropdown where users can select a movie.
    - Upon clicking the "Show Recommendation" button, the system returns the top 5 movie recommendations.

## How It Works

1. **Input**: The user selects or types the title of a movie.
2. **Processing**: The system uses the content-based recommendation algorithm to find the most similar movies.
3. **Output**: The recommended movies are displayed, along with a link to search for more information on Google.

## Technologies Used

- **Python**: The core language for this project.
- **Pandas**: Used for data manipulation and cleaning.
- **Scikit-learn**: Used for vectorization and similarity computation.
- **Streamlit**: Used for the web app interface.
- **Numpy**: Used for handling numerical operations.
- **Pickle**: For saving and loading the processed data.

## Installation

To run this project locally:

1. Clone the repository:

    ```bash
    git clone https://github.com/Saurabh1221SK/MovieRecommendation
    cd MovieRecommendation
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Streamlit Deployment

The app is deployed on Streamlit, and you can access it using the following link:

[Movie Recommender System](https://saurabh-1.streamlit.app/)

## Example Use Case

- **Input**: "Avatar"
- **Output**: Recommended movies like "The Host", "Aliens", "Avengers: Endgame", etc.


