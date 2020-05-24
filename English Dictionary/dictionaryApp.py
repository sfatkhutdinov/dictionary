import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    
    word = word.lower()
        
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        response = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if response == "Y" or response == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif response == "N" or response == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understan your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)