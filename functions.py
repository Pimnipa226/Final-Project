import urllib
import urllib.parse, urllib.request, urllib.error, json
import pprint
from lyricsgenius import Genius

def get_word_def_safe(word = "test"):
    try:
        base_url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"

        params = {"key": "f3ec4512-6658-4e54-8d83-a1c392c108fe"}

        url = base_url + word + "?" + urllib.parse.urlencode(params)

        response = urllib.request.urlopen(url)
        data = response.read()
        json_data = json.loads(data)

        return json_data[0]["shortdef"]

    except urllib.error.HTTPError as e:
        print("Error from server:", e.code)
        return
    except urllib.error.URLError as e:
        print("Error trying to retrieve data")
        print("Reason:", e.reason)
        return

pprint.pprint(get_word_def_safe("cough"))


def print_definition(word):
    def_list = get_word_def_safe(word)
    def_num = 0
    print(word)
    for definition in def_list:
        def_num += 1
        print(str(def_num) + ". " + definition)
    print("\n")

word_list = ["page", "pit", "novel"]
for word in word_list:
    print_definition(word)

# input_word = input("Enter a word: ")
# print_definition(input_word)
#
# keep_asking = True
# while keep_asking:
#     input_word = input("Enter a word: ")
#     print_definition(input_word)
#     input_asking = input("Do you want to continue? (y/n): ")
#     if input_asking == "n":
#         keep_asking = False


# def get_lyrics_safe(lyrics = "test"):
#     try:
#         base_url = "https://api.genius.com"
#
#         params = {"key": "l4fy_ho_DxnT2JaQTCYVWN3Q9AaQa2CqUWusCSnuwNcuqJd7WvOWiZEUZBecY2UKkZZMj8Xs10kHxcsJqKr8EA"}
#
#         url = base_url + word + "?" + urllib.parse.urlencode(params)
#
#         response = urllib.request.urlopen(url)
#         data = response.read()
#         json_data = json.loads(data)
#
#         return json_data[0]["songlyrics"]
#
#     except urllib.error.HTTPError as e:
#         print("Error from server:", e.code)
#         return
#     except urllib.error.URLError as e:
#         print("Error trying to retrieve data")
#         print("Reason:", e.reason)
#         return
#
# pprint.pprint(get_lyrics_safe(""))

def artist_songs(song_name, artist_name=None):

    genius = Genius("h108TqRwV5pR1ANBoVIKK9Nl21m8xCHq0K037IQ80i_vGsR3vsLrCQgZ7kPXHell")
    if artist_name is not None:
        song = genius.search_song(song_name, artist_name)
    else:
        song = genius.search_song(song_name)
    # artist = genius.search_artist("Taylor Swift", max_songs = 3)
    # print (artist.songs)
    # artist.save_lyrics()
    # songs_title = "Out of Time"
    # song = genius.search_song(songs_title)
    # print(song.lyrics)
    # artist = "Andy Shauf"
    # song = genius.search_song("To You", artist)
    # print (song.lyrics)

    lyrics_text = song.lyrics
    lines = lyrics_text.split("\n")
    lyrics_only = "\n".join(lines[1:])
    html_text = lyrics_only.replace("\n", "<br>")
    song_results = {
        "title" : song.title,
        "artist" : song.artist,
        "lyrics" : html_text
    }

    return song_results



# artist_songs("Stay", "Zedd")
# artist_songs("Stay")




