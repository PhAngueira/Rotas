from flask import Flask
app = Flask(__name__)

@app.route("/")
def index(): 
    return 'Hello!'

@app.route("/status")
def homepage():
    #{"status" : "OK"}
    return {"status" : "OK"}

@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}!'

@app.route('/soma/<int:n1>/<int:n2>')
def soma(n1, n2):
    return f'A soma de {n1} com {n2} é {n1+n2}'

if __name__ == "__main__":
    app.run()


'''
cmd -> pip install requests
python
>>>import requests
>>>response = requests.get('http://127.0.0.1.5000')
>>>response.text
>>>'Hello'

'''