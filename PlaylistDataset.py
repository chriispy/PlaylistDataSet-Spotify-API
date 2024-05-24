import tekore as tk
import csv

client_id = 'client_id'
client_secret = 'client_secret'

app_token = tk.request_client_token(client_id, client_secret)

# Spotify object
spotify = tk.Spotify(app_token)

playlistID = 'playlist_id' # Playlist ID 

first_items = spotify.playlist_items(playlistID)

with open('dataset.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write header row
    writer.writerow(['artist_name', 'track_name', 'track_id', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'])

    # Process each track and retrieve audio features
    for item in spotify.all_items(first_items):
        if item.track:
            track_name = item.track.name
            track_id = item.track.id
            artists = item.track.artists
            artist_name = artists[0].name if artists else 'Unknown' # First artist
            audio_features = spotify.track_audio_features(track_id)

            # Write the track details and audio features to the CSV file
            writer.writerow([
                artist_name,
                track_name, 
                track_id,
                audio_features.danceability,
                audio_features.energy,
                audio_features.key,
                audio_features.loudness,
                audio_features.mode,
                audio_features.speechiness,
                audio_features.acousticness,
                audio_features.instrumentalness,
                audio_features.liveness,
                audio_features.valence,
                audio_features.tempo
            ])