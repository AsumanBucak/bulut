from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Merhaba, Ben Asuman Bucak'

if __name__ == '__main__':
    app.run()