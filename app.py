from flask import *
from DataBaseConnection import *

app = Flask(__name__)

@app.route('/')
def mainFunction():
    dat = find_User("srikar")
    return "hello world"

@app.route('/createUser/<username>/<password>/')
def createUserFunction(username, password):
    ackl = create_User(name=username, password=password, head_user=False)
    if ackl : return "done" 
    else : return"not done"

@app.route('/findUser/<username>')
def giveUserInfo(username) :
    data = find_User(username)
    return data

@app.route('/massRemove')
def massRemove():
    return "hello world"

if __name__ == "__main__" :
    app.run(debug=True, host = "0.0.0.0", port = 5000)
