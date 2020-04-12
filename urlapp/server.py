
import os
from flask import Flask, request
import redis
import hashlib


# connect to redis
#client = redis.Redis(host='redis-server', port=6379)
client = redis.Redis(host="10.5.5.91", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

bad_url_file = open('/data/bad_urls.txt', 'r')
lines = bad_url_file.readlines()
for line in lines:
    key = hashlib.md5(line.strip().encode('utf-8')).hexdigest()
    client.set(key, line.strip())

@app.route("/")
def home_test():
    return "Hello Ram"

def check_if_url_is_bad(url : str):
    key = hashlib.md5(url.encode('utf-8')).hexdigest()
    if client.exists(key):
        return True
    return False

@app.route('/add_url_api')
def insert_mongo_db():
    url = request.args.get('url', default='', type=str)
    key = hashlib.md5(url.strip().encode('utf-8')).hexdigest()
    client.set(key, url.strip())
    return 'Insert ' + str(item) + ' into redis!'

@app.route('/list_url_api')
def get_db():
    result = []
    for key in client.scan_iter():
        value = client.get(key)
        result.append(str(value))
    return '\n'.join(result) + '\n'

@app.route('/check_url_api')
def check_url():
    url = request.args.get('url', default='', type=str)
    if check_if_url_is_bad(url):
        return 'Url ' + str(url) + ' is bad\n'
    else:
        return 'Url ' + str(url) + ' is safe\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
