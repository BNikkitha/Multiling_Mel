import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius
import nltk
from nltk.corpus import words
from nltk.tokenize import word_tokenize
import subprocess
import datetime
# from translate import Translator
from googletrans import Translator, constants
from pprint import pprint

nltk.download('punkt')

# Set up Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='174e4525132a4906a776c1e8212ba082',client_secret='92d2e5fb852442f0b8e59a3f197706c2'))


def translate_to_english(text):
    # translator = Translator(to_lang="en")
    # english_lyrics = translator.translate(text)
    # print(english_lyrics)
    # return english_lyrics
    translator = Translator()
    translation = translator.translate(text)
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

# Example usage:
# lyrics = "Hola, cómo estás? Je suis bien. Ich liebe Musik."
# english_lyrics = translate_to_english(lyrics)

def get_track_id(song_name, artist_name):
    results = sp.search(q=f'track:{song_name} artist:{artist_name}', type='track')
    if results['tracks']['items']:
        return results['tracks']['items'][0]['id']
    return None

# Set up Genius API client
genius = lyricsgenius.Genius('fvUgPzo-nDE2V_WzoQ82xdcmGujqtspipdIeS8aKMD9PuYqncnQiEYQEXIQ1uAah')

def get_lyrics(track_id):
    track = sp.track(track_id)
    song_name = track['name']
    artist_name = track['artists'][0]['name']
    
    # Search for lyrics on Genius
    song = genius.search_song(song_name, artist_name)
    
    if song:
        lyrics = song.lyrics
        return lyrics
    else:
        return None
    
# Define a function to check if a token is an English word
nltk.download('words')
english_words = set(words.words())

def is_english_word(token):
    return token.lower() in english_words

#making a note
def note(text):
    d=datetime.datetime.now()
    fn=str(d).replace("."," ").replace(":"," ")+" note.txt"
    s = ""
    for i in text:
        if i.isalpha() or i=="\t" or i=="\n":
            s+=i
    print(s)
    # with open(fn,"w") as f:
    #     f.write(s)
    # subprocess.Popen(["notepad.exe",fn])

# Example usage
# artist = "BTS"
artist = str(input("Enter the name of the artist: "))
# title = "Blood Sweat and Tears"
title = str(input("Enter the name of the song: "))
track_id = get_track_id(title, artist)
lyrics = get_lyrics(track_id)
# print(lyrics)
# note(translate_to_english(lyrics))
translate_to_english(lyrics)