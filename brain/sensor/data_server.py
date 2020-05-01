# from flask import Flask, request
import flask
import json
import requests


app = flask.Flask(__name__)


@app.route('/', methods=["GET"])
def get_data():
    # req_data = request.get_json()
    # print(req_data['id'])
    # return 'recieved'
    # req_data = request.get_json()

    # language = req_data['language']
    # framework = req_data['framework']
    # python_version = req_data['version_info']['python'] #two keys are needed because of the nested object
    # example = req_data['examples'][0] #an index is needed because of the array
    # boolean_test = req_data['boolean_test']

    # return '''
    #        The language value is: {}
    #        The framework value is: {}
    #        The Python version is: {}
    #        The item at index 0 in the example list is: {}
    #        The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)
    try:
        with open("config.json","r+") as f:
            x = json.load(f)
        ip_address = flask.request.remote_addr
        req_string = "http://"+str(ip_address)+":"+str(x["sensor_port"])
        print(req_string)
        x = requests.get(str(req_string))
        o = x.content
        sensor_type = o.decode('utf-8')
        print(sensor_type)
        update_ip(sensor_type, str(ip_address))
        print(ip_address)
        return 'True'
    except:
        return 'False'

@app.route('/motion', methods=["PUT"])
def motion():
    # ip_address = flask.request.remote_addr
    # req_string = "http://"+str(ip_address)+":8000"
    # x = requests.get(req_string)
    # o = x.content
    # print(o.decode('utf-8'))
    out = flask.request.data
    update_value('motion', out.decode('utf-8'))

    return 'motion'


@app.route('/temprature')
def temprature():
    # ip_address = flask.request.remote_addr
    # req_string = "http://"+str(ip_address)+":8000"
    # x = requests.get(req_string)
    # o = x.content
    # print(o.decode('utf-8'))
    return 'temprature'


@app.route('/rfid')
def rfid():
    # ip_address = flask.request.remote_addr
    # req_string = "http://"+str(ip_address)+":8000"
    # x = requests.get(req_string)
    # o = x.content
    # print(o.decode('utf-8'))
    return 'rfid'


def update_value(sensor, value):      
    with open("data.json","r+") as f:
        x = json.load(f)
    for i in x:
        if(i["sensor"]==str(sensor)):
            i["value"] = str(value)
    with open("data.json","w") as f:
        json.dump(x, f, ensure_ascii=False, indent=4)


def update_ip(sensor, ip):      
    with open("data.json","r+") as f:
        x = json.load(f)
    for i in x:
        if(i["sensor"]==str(sensor)):
            i["ip_address"] = str(ip)
    with open("data.json","w") as f:
        json.dump(x, f, ensure_ascii=False, indent=4)



if __name__ == "__main__":
    with open("config.json","r+") as f:
        x = json.load(f)
    app.run(host='0.0.0.0', port=int(x['brain_port']))