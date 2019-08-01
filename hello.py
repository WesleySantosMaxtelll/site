from cloudant import Cloudant
from flask import Flask, render_template, request, jsonify
from Interface import interface
import atexit
import os
import json

app = Flask(__name__, static_url_path='')

db_name = 'mydb'
client = None
db = None
inter = interface()

if 'VCAP_SERVICES' in os.environ:
    vcap = json.loads(os.getenv('VCAP_SERVICES'))
    print('Found VCAP_SERVICES')
    if 'cloudantNoSQLDB' in vcap:
        creds = vcap['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)
elif "CLOUDANT_URL" in os.environ:
    client = Cloudant(os.environ['CLOUDANT_USERNAME'], os.environ['CLOUDANT_PASSWORD'], url=os.environ['CLOUDANT_URL'], connect=True)
    db = client.create_database(db_name, throw_on_exists=False)
elif os.path.isfile('vcap-local.json'):
    with open('vcap-local.json') as f:
        vcap = json.load(f)
        print('Found local VCAP_SERVICES')
        creds = vcap['services']['cloudantNoSQLDB'][0]['credentials']
        user = creds['username']
        password = creds['password']
        url = 'https://' + creds['host']
        client = Cloudant(user, password, url=url, connect=True)
        db = client.create_database(db_name, throw_on_exists=False)

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))

@app.route('/')
def root():
    return app.send_static_file('index.html')

# /* Endpoint to greet and add a new visitor to database.
# * Send a POST request to localhost:8000/api/visitors with body
# * {
# *     "name": "Bob"
# * }
# */
# @app.route('/api/visitors', methods=['GET'])
# def get_visitor():
#     if client:
#         return jsonify(list(map(lambda doc: doc['name'], db)))
#     else:
#         print('No database')
#         return jsonify([])

# /**
#  * Endpoint to get a JSON array of all the visitors in the database
#  * REST API example:
#  * <code>
#  * GET http://localhost:8000/api/visitors
#  * </code>
#  *
#  * Response:
#  * [ "Bob", "Jane" ]
#  * @return An array of all the visitor names
#  */

@app.route('/post', methods=['POST', 'GET'])
def put_visitor():

    if request.method == 'POST':
        print(request.json)
        topic = request.json['radios']
        text = request.json['text']
        resp = inter.request(text, topic)
        return resp
        # return jsonify({'prediction':resp})

    else:
        resp = 'Resposta'
        return jsonify({'prediction':resp})


@app.route('/save', methods=['POST', 'GET'])
def save_text():

    if request.method == 'POST':
        print(request.json)
        # topic = request.json['radios']
        # text = request.json['text']
        inter.save_text(request.json['text'], request.json['radios'], request.json['resp_radios'],
            request.json['model_ans'])
        return 'done'
        # return jsonify({'prediction':resp})
    return ''



@app.route('/statistics', methods=['GET'])
def get_statistics():
    t, p, mp = inter.statiscts()
    if t > 5:
        return jsonify({"prec":'{}%'.format(int(100*p[0][0])), "cont":t})
    else:
        return jsonify({"prec":'{}%'.format('-'), "cont":t, "mp":mp})
    #     resp = 'Resposta'
    #     return jsonify({'prediction':resp})



@app.route('/textos', methods=['GET'])
def get_textos():
    resp = inter.get_textos()
    # resp = {1:'a', 2:'b', 3:'c'}
    f = open('textos.txt', 'w+')
    f.write(str(resp))
    return jsonify(resp)
   
@atexit.register
def shutdown():
    if client:
        client.disconnect()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)
