
import os
from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://urldb:27017/', connect=False)
db = client.testdb

bad_url_file = open('/data/bad_urls.txt', 'r')
lines = bad_url_file.readlines()
for line in lines:
    item = {"url": line}
    db.test_collection.insert_one(item)

@app.route("/")
def home_test():
    return "Hello Ram"

def check_if_url_is_bad(url : str):
    if db.test_collection.find({"url": url}).count() > 0:
        return True
    return False

@app.route('/add_url_api')
def insert_mongo_db():
    url = request.args.get('url', default='', type=str)
    item = {"url" : url.strip()}
    db.test_collection.insert_one(item)
    return 'Insert ' + str(item) + ' into MongoDB!'

@app.route('/list_url_api')
def get_mongo_db():
    result = []
    for document in db.test_collection.find():
        result.append(document)
    return 'Received \n' + str(result) + '\n from MongoDB\n'

@app.route('/check_url_api')
def check_url():
    url = request.args.get('url', default='', type=str)
    if check_if_url_is_bad(url):
        return 'Url ' + str(url) + ' is bad\n'
    else:
        return 'Url ' + str(url) + ' is safe\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
