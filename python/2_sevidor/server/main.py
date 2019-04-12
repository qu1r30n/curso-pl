from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_wer():
    return 'hola mundo total2'

if __name__ == '__main__':
    app.run()