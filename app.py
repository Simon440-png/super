from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/query-example')
def query_example():
    language = request.args.get('language')

    return '''<h1>The language value is: {}</h1>'''.format(language)


@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)
    return '''
              <form method="POST">
                  <div><label>Language: <input type="text" name="language"></label></div>
                  <div><label>Framework: <input type="text" name="framework"></label></div>
                  <input type="submit" value="Submit">
              </form>'''


@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()
    return '''<h1>The language value is: {}</h1>'''.format(request_data)


if __name__ == '__main__':
    app.run()
