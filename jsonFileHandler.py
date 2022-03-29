import json

def readJsonFile(jsonFileHandler):
    data = ""
    try:
        with open(jsonFileHandler) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data
