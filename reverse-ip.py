from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    ip = request.remote_addr
    octets = ip.split('.')
    
    reversed_ip = '.'.join(octets[::-1])
    return reversed_ip


if __name__ == '__main__':
    app.run(host='127.0.0.1')
