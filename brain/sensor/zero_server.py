# from flask import Flask, request
import flask
import json
import requests


app = flask.Flask(__name__)


@app.route('/update', methods=["PUT"])
def update_time():
    # ip_address = flask.request.remote_addr
    # req_string = "http://"+str(ip_address)+":8000"
    # x = requests.get(req_string)
    # o = x.content
    # print(o.decode('utf-8'))
    out = flask.request.data
    with open("config.json","r+") as f:
        x = json.load(f)
    # print(out)
    x['light_time']= out.decode('utf-8')
    try:
        int(x['light_time'])
        with open("config.json","w") as f:
            json.dump(x, f, ensure_ascii=False, indent=4)
            return 'Updated'
    except:
        pass
        return 'Failed'
    


@app.route('/', methods=["GET"])
def motion_handle():
    # ip_address = flask.request.remote_addr
    # req_string = "http://"+str(ip_address)+":8000"
    # x = requests.get(req_string)
    # o = x.content
    # print(o.decode('utf-8')
    # print(out)


    return 'motion'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8800)