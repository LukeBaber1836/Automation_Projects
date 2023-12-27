import json

def word_definition(word):
    # Opening JSON file
    file = open('dictionary.json')
    data = json.load(file)
    try:
        definition = data[word.lower()]
        full_deff = ''
        count = 1
        for x in definition:
            full_deff = full_deff + f"Definition {count}:  " + x + "\n \n"
            count +=1
        return full_deff
    except:
        return("Word not found...")

if __name__ == "__main__":
    print(word_definition("Dog"))