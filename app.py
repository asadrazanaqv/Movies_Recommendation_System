import streamlit as st
import pickle
import requests
import streamlit.components.v1 as components

# Load movies and similarity data
movies_list = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))

# TMDB API settings
api_key = "c7ec19ffdd3279641fb606d19ceb9bb1"

def get_movie_id(movie_title):
    url = f"http://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}"
    response = requests.get(url)
    data = response.json()
    if data['results']:
        return data['results'][0]['id']
    else:
        return None

def fetch_poster(movie_title):
    movie_id = get_movie_id(movie_title)
    if movie_id is None:
        return "No poster available"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path

st.header("Movie Recommender System")

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

imageUrls = [fetch_poster(movie) for movie in movies_list[:16]]

imageCarouselComponent(imageUrls=imageUrls, height=200)

selectvalue = st.selectbox("Select movie from dropdown", movies_list)

def recommend(movie):
    index = movies_list.index(movie)
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = [movie]  # Add the selected movie first
    for i in distance[1:16]:
        recommend_movie.append(movies_list[i[0]])
    return recommend_movie

if st.button("Show Recommend"):
    movie_name_list = recommend(selectvalue)
    for i in range(0, len(movie_name_list), 4):
        cols = st.columns(4)
        for j in range(4):
            if i + j < len(movie_name_list):
                movie = movie_name_list[i + j]
                cols[j].text(f"{i+j+1}. {movie}")
                try:
                    poster_url = fetch_poster(movie)
                    cols[j].image(poster_url, width=100)
                except Exception as e:
                    cols[j].write("Poster not available")