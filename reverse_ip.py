from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    octets = ip.split('.')
    reversed_ip = '.'.join(octets[::-1])
    return reversed_ip

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

