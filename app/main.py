"""
AWS SDK TESTS.  I WRITE THESE TESTST IN ORDER TO BETTER UNDERSTAND
THE AWS  ARCHITECTURE . THIS IS  ONLY FOR TESTING PURPOSE
"""
import boto3
import os
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello , tol World"


@app.route('/test')
def test_aws():
    sqs = boto3.resource('sqs')
    for q in sqs.queues.all():
        print(q.url)
    print("__________________")
    sqs1 = boto3.client("sqs")
    response = sqs1.list_queues()
    print(response['QueueUrls'])
    return response['QueueUrls']


@app.route('/lambda')
def test_lambda():
    client = boto3.client('lambda')
    response = client.list_functions()
    print(response)
    return response


@app.route('/apigateway')
def test_apigateway():
    client = boto3.client('apigateway')
    response = client.get_integration()
    print(response)
    return response


@app.route('/sns')
def sns():
    client = boot.client('sns')
    response = client.list_topics()
    print(response)
    return response


print("get some aws data")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
