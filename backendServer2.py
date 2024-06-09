from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello From Backend Server'

@app.route('/health')
def health():
    return 'Healthy', 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=500)  # Change port number for different servers
