import ast
# If you are using Python 3+, import urllib instead of urllib2
import ssl
import urllib.request
#import urllib2
# from urllib2 import HTTPError
import json
import os.path

from flask import Flask, Response, request,render_template,send_from_directory


app = Flask(__name__)
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
port = int(os.getenv('PORT', 8080))

@app.route("/")
def welcome():
    print(tmpl_dir)
    return render_template('index.html')

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).rbiead()
    except IOError as exc:
        return str(exc)

@app.route('/getPredicted', methods=['POST'])

def getPredictedDetails():
    data = {

        "Inputs": {

            "input1":
                {
                    "ColumnNames": ["age", "Medu", "Fedu","traveltime", "studytime", "freetime"],
                    "Values": [ [(request.form.get("age")),
                                (request.form.get("Medu")),
                                (request.form.get("Fedu")),
                                (request.form.get("traveltime")),
                                (request.form.get("studytime")),
                                (request.form.get("freetime")),
                                ], ]
                }, },
        "GlobalParameters": {
        }
    }

    body = str.encode(json.dumps(data))


    url = 'https://ussouthcentral.services.azureml.net/workspaces/49a0370322ee4162aa36ef32433f614d/services/bbab5a5f0f604324988e472b9bc730d6/execute?api-version=2.0&details=true'
    api_key = 'IRHHtZeElVlxifPADI3W5NivftKwz+CgX9AANLZXuXdy2dlnAmjNZdZgJ9+nWjSyIcD3FenCPOQ1LNnZ8pmSjg=='  # Replace this with the API key for the web service
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}
    #context = ssl._create_unverified_context()
    req = urllib.request.Request(url, body, headers)
    #req = urllib2.Request(url, body, headers)
    # try:
    response = urllib.request.urlopen(req)


    #response = urllib2.urlopen(req)
        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers)
        # response = urllib.request.urlopen(req)

    result = response.read().decode('utf-8')
    # result= json.loads(response.read())
        # for key, value in dict.items(result["ColumnNames"]):
        #     print(key, value)
    jsonList=json.loads(result)
    values=jsonList['Results']['output1']['value']['Values']
    print(result)
    print(values)
    prediction=float(values[0][7])
    #prediction = 0.68
    if (prediction > 0.5):
        resultStatus="Grades are Affected"
        print(values[0][7])
    else:
        resultStatus = "Grades are not Affected"
    print (resultStatus)
    # except urllib.error as error:
    #     print("The request failed with status code: " + str(error.code))
    #
    #     # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    #     print(error.info())
    #
    #     print(json.loads(error.read()))

    #return send_from_directory('js', path)
    #return render_template('UserDashboard.html',resultStatus=resultStatus)
    prediction=round(prediction,2)*100
    print(prediction)
    return render_template('gradesFactors.html',prediction=prediction,resultStatus=resultStatus)


@app.route('/getClassified', methods=['POST'])

def getClassified():
    data = {

        "Inputs": {

            "input1":
                {
                    "ColumnNames": ["age", "Medu", "Fedu","traveltime", "studytime", "freetime"],
                    "Values": [ [(request.form.get("age")),
                                (request.form.get("Medu")),
                                (request.form.get("Fedu")),
                                (request.form.get("traveltime")),
                                (request.form.get("studytime")),
                                (request.form.get("freetime")),
                                ], ]
                }, },
        "GlobalParameters": {
        }
    }

    body = str.encode(json.dumps(data))


    url = 'https://ussouthcentral.services.azureml.net/workspaces/49a0370322ee4162aa36ef32433f614d/services/e62465b4fb714cf689837acda34c9fee/execute?api-version=2.0&details=true'
    api_key = 'EisSOIJ0rmbiX7fVTUnYMpg1GFLVuHaVvGj1gtO/rCw/UBrj+O7Sv24tsX8CfEWltFVBJWGXb5DWpBROoETRmQ=='  # Replace this with the API key for the web service
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}
    #context = ssl._create_unverified_context()
    req = urllib.request.Request(url, body, headers)
    #req = urllib2.Request(url, body, headers)
    # try:
    response = urllib.request.urlopen(req)


    #response = urllib2.urlopen(req)
        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers)
        # response = urllib.request.urlopen(req)

    result = response.read().decode('utf-8')
    # result= json.loads(response.read())
        # for key, value in dict.items(result["ColumnNames"]):
        #     print(key, value)
    jsonList=json.loads(result)
    values=jsonList['Results']['output1']['value']['Values']
    print(result)
    print(values)
    prediction=int(values[0][23])
    #resultStatus = prediction
    #prediction = 0.68
    #if (prediction > 0.5):
        #resultStatus="Grades are Affected"
        #print(values[0][7])
    #else:
        #resultStatus = "Grades are not Affected"
    #print (resultStatus)
    # except urllib.error as error:
    #     print("The request failed with status code: " + str(error.code))
    #
    #     # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    #     print(error.info())
    #
    #     print(json.loads(error.read()))

    #return send_from_directory('js', path)
    #return render_template('UserDashboard.html',resultStatus=resultStatus)
    #prediction=round(prediction,2)*100
    print(prediction)
    return render_template('grades.html',prediction=prediction)


if __name__ == "__main__":
    app.run()
    #app.run(host='0.0.0.0', port=port, debug=True)