from urllib import request

from flask import Flask, render_template, request
import urllib.parse, urllib.request, urllib.error, json
import pprint

import functions

app = Flask(__name__)


#### HCDE 310
#### HW5 - Exercises

# def get_word_def_safe(word = "test"):
#     try:
#         base_url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"
#
#         params = {"key": "f3ec4512-6658-4e54-8d83-a1c392c108fe"}
#
#         url = base_url + word + "?" + urllib.parse.urlencode(params)
#
#         response = urllib.request.urlopen(url)
#         data = response.read()
#         json_data = json.loads(data)
#
#         return json_data[0]["shortdef"]
#
#     except urllib.error.HTTPError as e:
#         print("Error from server:", e.code)
#         return
#     except urllib.error.URLError as e:
#         print("Error trying to retrieve data")
#         print("Reason:", e.reason)
#         return
#
# pprint.pprint(get_word_def_safe("cough"))
#
#
# def print_definition(word):
#     def_list = get_word_def_safe(word)
#     def_num = 0
#     print(word)
#     for definition in def_list:
#         def_num += 1
#         print(str(def_num) + ". " + definition)
#     print("\n")
#
# word_list = ["page", "pit", "novel"]
# for word in word_list:
#     print_definition(word)
#
# # input_word = input("Enter a word: ")
# # print_definition(input_word)
# #
# # keep_asking = True
# # while keep_asking:
# #     input_word = input("Enter a word: ")
# #     print_definition(input_word)
# #     input_asking = input("Do you want to continue? (y/n): ")
# #     if input_asking == "n":
# #         keep_asking = False


@app.route('/', methods=['GET', 'POST'])
# def show_definition():  # put application's code here
#     word = None
#     if not word:
#         current_word = "novel"
#         definition = get_word_def_safe(current_word)
#     if request.method == "POST":
#         text_value = request.form.get("word")
#         print(text_value)
#         current_word = text_value
#         definition = get_word_def_safe(current_word)
#     return render_template('index.html', word = current_word, first_def = definition[0])

def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    if request.method == 'POST':
        song_name = request.form['song_name']
        artist_name = request.form['artist_name']
        song_data = functions.artist_songs(song_name, artist_name)
        return render_template('results.html', song=song_data)


if __name__ == '__main__':
    app.run(debug=True)
