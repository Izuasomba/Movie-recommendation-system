import pickle
import streamlit as st
import requests

# CSS styling
st.markdown(
    """
    <style>
    .header {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }

    .movie-name {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .movie-poster {
        width: 200px;
        height: auto;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.markdown("<h1 class='header'>Movie Recommendation System</h1>", unsafe_allow_html=True)

movies = pickle.load(open('C:/Users/hp/OneDrive/Desktop/Movie recommendation system/movie_list.pkl','rb'))
similarity = pickle.load(open('C:/Users/hp/OneDrive/Desktop/Movie recommendation system/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("<p class='movie-name'>{}</p>".format(recommended_movie_names[0]), unsafe_allow_html=True)
        st.image(recommended_movie_posters[0], caption=recommended_movie_names[0], use_column_width=True)
    with col2:
        st.markdown("<p class='movie-name'>{}</p>".format(recommended_movie_names[1]), unsafe_allow_html=True)
        st.image(recommended_movie_posters[1], caption=recommended_movie_names[1], use_column_width=True)

    with col3:
        st.markdown("<p class='movie-name'>{}</p>".format(recommended_movie_names[2]), unsafe_allow_html=True)
        st.image(recommended_movie_posters[2], caption=recommended_movie_names[2], use_column_width=True)
    with col4:
        st.markdown("<p class='movie-name'>{}</p>".format(recommended_movie_names[3]), unsafe_allow_html=True)
        st.image(recommended_movie_posters[3], caption=recommended_movie_names[3], use_column_width=True)
    with col5:
        st.markdown("<p class='movie-name'>{}</p>".format(recommended_movie_names[4]), unsafe_allow_html=True)
        st.image(recommended_movie_posters[4], caption=recommended_movie_names[4], use_column_width=True)
