# Importing necessary libraries
import pickle
import pandas as pd
import streamlit as st
from sklearn.neighbors import NearestNeighbors
import lzma

# Loading movie data and similarity matrix
def load_data():
    movies = pd.read_pickle('movie_list.pkl.xz') 
    similarity = pd.read_pickle('similarity.pkl.xz') 
    
    return movies, similarity


# Function to recommend movies using NearestNeighbors for faster search
def recommend(movie, movies, similarity, model):
    index = movies[movies['title'] == movie].index[0]
    distances, indices = model.kneighbors([similarity[index]], n_neighbors=6)
    
    recommended_movies = []
    recommended_set = set()  # To keep track of unique recommendations
    
    # Iterating over indices and adding movies until we get 5 unique recommendations
    for i in indices[0][1:]:  
        movie_title = movies.iloc[i].title
        if movie_title not in recommended_set:
            recommended_movies.append(movie_title)
            recommended_set.add(movie_title)
        if len(recommended_movies) == 5:
            break
    
    return recommended_movies

# Streamlit header
st.header('Movie Recommender System Using Machine Learning')

# Loading the movie data and similarity matrix
movies, similarity = load_data()

# Fitting NearestNeighbors model for efficient recommendations
model = NearestNeighbors(n_neighbors=6, metric='cosine')
model.fit(similarity)

# Movie selection dropdown
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Recommendation logic
if st.button('Show Recommendation'):
    with st.spinner('Generating Recommendations...'):
        recommended_movie_names = recommend(selected_movie, movies, similarity, model)
        cols = st.columns(5)
        
        # Displaying recommended movies with Google search links
        for idx, col in enumerate(cols):
            if idx < len(recommended_movie_names): 
                movie_name = recommended_movie_names[idx]
                google_search_url = f"https://www.google.com/search?q={movie_name.replace(' ', '+')}"
                with col:
                    st.markdown(f"**{movie_name}**")
                    st.markdown(f"[Search]({google_search_url})")
