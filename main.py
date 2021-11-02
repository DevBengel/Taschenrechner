"""
Mein Taschenrechner
"""
import socket
from flask import Flask
from flask import abort
from flask import request
from flask import jsonify, make_response

local_server_ip = socket.gethostbyname(socket.gethostname())
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hallo():
    """
    Return Hello-World
    """
    response = make_response(jsonify(hello='world'), 200,)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/add', methods=['POST'])
def add_op():
    """
    Addition
    """
    # Force erlaubt auch ein JSON-Decode, wenn kein MIME-Type gesetzt ist
    content = request.get_json(force=True)
    if "zahleins" in content:
        zahlx = int(content["zahleins"])
    else:
        abort(400)

    if "zahlzwei" in content:
        zahly = int(content["zahlzwei"])
    else:
        abort(400)

    ergebnis = zahlx + zahly
    response = make_response(jsonify(ergebnis=ergebnis), 200,)
    response.headers["Content-Type"] = "application/json"
    return response

@app.route('/status', methods=['GET'])
def serverstate():
    """
    Return State and IP-Address
    """
    response = make_response(jsonify(my_ip=local_server_ip, state="alive"), 200,)
    response.headers["Content-Type"] = "application/json"
    return response

if  __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
