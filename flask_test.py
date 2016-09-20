from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/get/<index>', methods = ['GET'])
def get_call(index):

    return 'This is a get request for index file number: ' + str(index)

@app.route('/p1', methods = ['POST'])
def post_call():
	data = request.get_json()
	index = data['index']
	return 'This is a post request for index file number: ' + str(index)
app.run()