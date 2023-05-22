
import json

JFR = open("books.json", "r")
jsonFile = json.load(JFR)           # convert json data into python objects

for book in jsonFile['books']:
    for k, v in book.items():
        print(k, "=>", v)
    print("-" * 40)
