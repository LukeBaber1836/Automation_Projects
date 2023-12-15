import json
 
def word_definition(word= 'hello'):
    # Opening JSON file
    file = open('dictionary.json')
    data = json.load(file)
    return(data[word])