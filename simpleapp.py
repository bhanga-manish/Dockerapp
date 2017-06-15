import argparse
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"


if __name__=='__main__':
    parser = argparse.ArgumentParser(description = 'python simpleapp.py')
    parser.add_argument('-p',action = 'store' , dest='port')
    args = parser.parse_args()
    print(args.port)
    app.run(host='127.0.0.1',port=int(args.port),debug=False)
    
