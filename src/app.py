from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        "nome": "Flask API",
        "hostname": socket.gethostname(),
        "version": "1.0.0",
        "Descricao": "A simple Flask API",
        "tempo": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    })


@app.route('/api/v1/healthz')
def healthz():
    return jsonify({
        "status": "healthy"
    }), 200

if __name__ == '__main__':

    app.run(host='0.0.0.0')