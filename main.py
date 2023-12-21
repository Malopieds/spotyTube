from ytmusicapi import YTMusic
import requests
import json

spotify_playlist = #####
ytmusic_playlist = #####

yt = YTMusic('oauth.json')

headers = {
        "Authorization": "Basic NzIxZDZmNjcwZjA3NGIxNDk3ZTc0ZmM1OTEyNWE2ZjM6ZWZkZGMwODNmYTk3NGQzOWJjNjM2OWE4OTJjMDdjZWQ=",
        "Content-Type": "application/x-www-form-urlencoded"
}
params = {
        "grant_type": "client_credentials"
}

authorization_token = requests.post("https://accounts.spotify.com/api/token", headers = headers, params = params).json()['access_token']
print("authorization_token found: " + authorization_token)
headers = {
        "Authorization": "Bearer " + authorization_token
        }
r = requests.get('https://api.spotify.com/v1/playlists/'+spotify_playlist, headers=headers)
data = r.json()

for i in data['tracks']['items']:
    search = i['track']['name']
    for j in i['track']['artists']:
        search = search + " " + j['name']
    print(search)
    res = yt.search(search, 'songs', limit = 1)
    print("id found: " + res[0]['videoId'])
    yt.add_playlist_items(ytmusic_playlist, [res[0]['videoId']])
