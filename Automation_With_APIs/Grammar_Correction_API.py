import requests
import json

# Uses langauge tool API for spell check correction
def spell_check(sentence):
    url = "https://api.languagetool.org/v2/check"
    data = {
        'text' : sentence,
        'language' : 'auto'
    }
    response = requests.post(url, data=data).json()
    #print(json.dumps(response, indent= 2))

    for x in range(len(response['matches'])):
        correct_word = response['matches'][x]['replacements'][0]['value']
        # Use these values for inserting ne word at correct location
        start = int(response['matches'][x]['offset'])
        end = int(response['matches'][x]['length']) + start
        old_word = data['text'][start:end]
        sentence = sentence.replace(old_word, correct_word)
    
    return sentence

def get_input():
    value = input("Type a sentence: ")
    return value

def __main__():
    user_input = get_input()
    correction = spell_check(user_input)
    print("Corrected sentence: " + correction)

if __name__ == "__main__":
    while True:
        __main__()