<h1>
  <img src="https://m.media-amazon.com/images/I/51rttY7a+9L.png" width="40" style="vertical-align: middle;">
  Spotify Data App
</h1>

## Data Science Assignment 🎒
As part of an assignment, we are asked to make a basic streamlit app using data of our interests. Since I am very interested in music and have been using spotify for a while, I chose to take data from Maharshi Pandya from their Kaggle [Spoitfy Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset). As part of the assignment, we are asked to write at least 100 lines of code interacts with at least four columns of data (mix of numerical and categorical variables). Moreover, this app that we make is suppose to help us explore as well and filter out data, reaching unique insights. 

### Objectives and Goals 📋:
- I hoped to make an app that *focuses* on **energy level**, **danceability**, **popularity**, and **explicit/clean** content to determine a list of songs.
- I acknowledge that its a bit difficult through just vibes by scaling, so I provided a *histogram* that focuses on the genre chosen to provide where a general range of the *frequency* of the songs based on **energy level**, **danceability**, and **popularity**.
- If that wasn't enough, I provided a way to *foccus* entirely on genre, popularity, and artists to narrow down the scope in another way.
- At the end, there is a way to choose the particular song from the given data frame and a button to acquire the **spotify link** to the song. 

## Terminology Data Table
Description taken from the Kaggle dataset

| Features / Variable | Description                                 |
|---------------------|---------------------------------------------|
| **track_id** | The Spotify ID for the track |
| **artists** | The artists' names who performed the track |
| **album_name** | The album name in which the track appears |
| **track_name** | Name of the track |
| **popularity** | The popularity of a track is a value between 0 and 100, with 100 being the most popular. The popularity is calculated by algorithm and is based, in the most part, on the total number of plays the track has had and how recent those plays are. |
| **duration_ms** | The track length in milliseconds | 
| **explicit** | Whether or not the track has explicit lyrics | 
| **danceability** | Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable |
| **energy** | Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy |
| **key** | The key the track is in | 
| **loudness** | The overall loudness of a track in decibels (dB) | 
| **mode** | Indicates the modality (major or minor) of a track. Major = 1, Minor = 0. |
| **speechiness** | Measures the presence of spoken words. Values > 0.66 are mostly speech; 0.33–0.66 contain mixed speech/music (e.g., rap); < 0.33 are mostly music. |
| **acousticness** | Confidence (0.0–1.0) that the track is acoustic. A value of 1.0 means high confidence the track is acoustic. |
| **instrumentalness** | Predicts whether a track contains no vocals. Higher values indicate a greater likelihood of being purely instrumental. |
| **liveness** | Detects audience presence. Higher values suggest the track was performed live; values > 0.8 strongly indicate a live performance. |
| **valence** | Measures musical positiveness (0.0–1.0). High valence = happy/cheerful; low valence = sad/angry. |
| **tempo** | Estimated tempo in beats per minute (BPM), representing the speed or pace of the track. |
| **time_signature** | Estimated time signature (3–7), representing meters like 3/4 through 7/4. |
| **track_genre** | The genre category to which the track belongs. |

## My App 🖥️
[Here](https://github.com/cbustil2/Bustillo-Data-Science-Portfolio/tree/main/basic_streamlit_app/Spotify%20Data%20App) is all of the information for my code and dataset. 
