"""
Spotify Data App using Streamlit

Started on Friday February 5, 2025

"""
import streamlit as st 

#Spotify Image:
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Spotify_logo_with_text.svg/960px-Spotify_logo_with_text.svg.png" 
             width="300">
    </div>
    """,
    unsafe_allow_html=True
)

#Title and Objective/Goal - Energy Level, Dancebility, Popularity, Explicit/Clean
st.markdown(
    "<h1 style='text-align: center;'>You Hear that?? 💃🎧🕺</h1>",
    unsafe_allow_html=True
)

st.write("Ever wonder what songs are the most popular on Spotify? " \
"Ever wonder what songs you would want to dance your heart to?" \
" Hopefully this app will help you!! :smile:")
st.write("This app will allow you to set up preferences based on energy level,\
dancebility, popularity, and explicit/clean content." \
" From there you will find a list of songs in the similar range of your preferences!")
st.write("Let's get started! :musical_note: :notes:")

#Loading spotify_data.csv file
import pandas as pd

df = pd.read_csv("spotify_data.csv")

#Energy Level Slider (SCALED 1)
#I need to first edit the data so it fits the slider.
df["energy"] = df["energy"] * 100
df["danceability"] = df["danceability"] * 100

energy_lvl = st.slider("❄️ Low Energy  →  High Energy 🔥", min_value=0, max_value=100, value=50, step = 1) #Note I need margin of error of at least 8
dancebility_lvl = st.slider('Danceability', min_value=0, max_value=100, value=50, step=1)
popularity_lvl = st.slider('Popularity', min_value=0, max_value=100, value=50, step=1)
choice = st.radio("What you feelin'?", ['Clean', 'Explicit'])
selected_genre = st.selectbox("🎼 Pick a genre", df["track_genre"].unique())

margin = 10

#changing the values
explicit_map = {
    "Clean": False,
    "Explicit": True
}

filtered_df = df[
    (df["energy"].between(energy_lvl - margin, energy_lvl + margin)) &
    (df["danceability"].between(dancebility_lvl - margin, dancebility_lvl + margin)) &
    (df["popularity"].between(popularity_lvl - margin, popularity_lvl + margin)) &
    (df["explicit"] == explicit_map[choice])
    & (df["track_genre"] == selected_genre)
]

st.subheader(f"Here are some {selected_genre} songs you might like! :musical_note: :notes:")
columns_to_show = ["track_name", "artists", "album_name", "energy", "danceability", "popularity"]
st.dataframe(filtered_df[columns_to_show])

if filtered_df.empty:
    st.write("Sorry, no songs match your preferences. " \
    "Try adjusting the sliders or selecting a different genre." \
    "If it'll help, here is a graph of the specific genre you selected! :smile:")   

selected_song = st.selectbox("Choose your song", filtered_df["track_name"].unique())

#Button for spotify link with error exception
if st.button("Get Spotify Link"):
    # Filter to the selected song
    song_df = df[df["track_name"] == selected_song]

    if not song_df.empty:
        track_id = song_df["track_id"].iloc[0]
        spotify_url = f"https://open.spotify.com/track/{track_id}"

        # Display a clickable button that opens Spotify
        st.markdown(
            f"<a href='{spotify_url}' target='_blank'>"
            "<button style='background-color:#1DB954;color:white;padding:10px 20px;"
            "border:none;border-radius:5px;'>Open in Spotify 🎧</button></a>",
            unsafe_allow_html=True
        )
    else:
        st.error("No track ID found for this song.")

import altair as alt

st.subheader( f"Distribution of Energy Levels in {selected_genre} Songs :bar_chart:")

# Filter by selected genre (optional)
genre_df = df[df["track_genre"] == selected_genre]

# Choose which attribute to plot
attribute_label = st.selectbox(
    "Pick an attribute to visualize",
    ["Energy", "Danceability", "Popularity"],
    index=0
)

# Map display names → actual df column names
attribute_map = {
    "Energy": "energy",
    "Danceability": "danceability",
    "Popularity": "popularity"
}

attribute = attribute_map[attribute_label]

import altair as alt
genre_df = df[df["track_genre"] == selected_genre]

# Altair selection
selection = alt.selection_interval(encodings=["x"])

#Histogram for frequency of energy, popularity, and dancebility levels in the selected genre
hist = (
    alt.Chart(genre_df)
    .mark_bar()
    .encode(
        alt.X(f"{attribute}:Q", bin=alt.Bin(maxbins=30)),
        alt.Y("count()"),
        color=alt.Color(f"{attribute}:Q", bin=alt.Bin(maxbins=30), scale=alt.Scale(scheme="viridis")),
        opacity=alt.condition(selection, alt.value(1), alt.value(0.3))
    )
    .add_params(selection)
)

st.subheader(f"Frequency of {attribute.capitalize()}")
chart = st.altair_chart(hist, use_container_width=True)

# If all else fails, finding songs based on popularity and artists

#Option to choose the artist within the genre and popularity
st.subheader("If vibees aren't for you, here's a way to find songs based on popularity and artists! :sunglasses:")
popularity_lvl_2 = st.slider('Popularity for Artists', min_value=0, max_value=100, value = 50, step=1)
selected_genre2 = st.selectbox("Pick a genre", df["track_genre"].unique())
genre1_df = df[ 
    (df["track_genre"] == selected_genre2) &
    (df["popularity"].between(popularity_lvl_2 - margin, popularity_lvl_2 + margin))
]
artists = sorted(genre1_df["artists"].unique().tolist())    
selected_artist = st.selectbox("🎤 Pick an artist", artists)

Final_df = genre1_df[genre1_df["artists"] == selected_artist]

songs = Final_df["track_name"].unique().tolist()
selected_song = st.selectbox("🎵 Pick a song", songs)

st.subheader(f"Here are some songs by {selected_artist} in the {selected_genre2} \
             genre with popularity around {popularity_lvl_2}! :musical_note: :notes:")

if st.button("Spotify Link for the Song"):
    # Filter to the selected s  ong
    song_df = Final_df[Final_df["track_name"] == selected_song]

    if not song_df.empty:
        track_id = song_df["track_id"].iloc[0]
        spotify_url = f"https://open.spotify.com/track/{track_id}"

        # Display a clickable button that opens Spotify
        st.markdown(
            f"<a href='{spotify_url}' target='_blank'>"
            "<button style='background-color:#1DB954;color:white;padding:10px 20px;"
            "border:none;border-radius:5px;'>Open in Spotify 🎧</button></a>",
            unsafe_allow_html=True
        )
    else:
        st.error("No track ID found for this song.")


# Works and Data:

st.subheader("Works Cited :books:")
st.write("The data that has been collected can be found [here](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset/data)." \
" Maharshi Pandya is the author of the data set with DOI: https://doi.org/10.34740/kaggle/dsv/4372070")

#Some of the fixing of errors and bugs in the code was done with the help of CoPilot.
#  I also used the Streamlit documentation to help me with some of the code: 
# https://docs.streamlit.io/library/api-reference/widgets