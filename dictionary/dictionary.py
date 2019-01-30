import json
from difflib import get_close_matches as gsm

data = json.load(open("dictionary.json"))

def retrive_definition(word):

    word = word.lower()

    matches_words = gsm(word, data.keys(), n=3, cutoff=0.75)

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(matches_words) > 0:
        action = input("Did you mean %s instead? [1 or 2 or 3]: "
                       % matches_words)
        return data[matches_words[int(action) - 1]]
    else:
        return ("The word doesn't exist, please double check it.")

while True:
    word_user = input("Enter a word: ")
    if word_user == "e":
        break

    output = retrive_definition(word_user)

    if type(output) == list:
        for item in output:
            print("-", item)
    else:
        print("-",output)
