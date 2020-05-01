import flask
import config as cfg


app = flask.Flask(__name__)

@app.route('/')
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
    return str(cfg.SENSOR_TYPE)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
