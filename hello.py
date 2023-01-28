import flask

def say_hello():
    print('Hello!')




app = flask.Flask(__name__)

@app.route('/api/say_hello', methods=['GET'])
def say_hello_api():
    return say_hello()