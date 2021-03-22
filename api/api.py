import flask
from flask import request, jsonify
from keybert import KeyBERT

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/v1/keybert/', methods=['POST'])


def api_id():
    if request.form:
        form = request.form
    else:
        return "Error: something wong"

    results = keybertify(form['data'])

    return jsonify(results)

def keybertify(data):
    data = data
    model = KeyBERT('distilbert-base-nli-mean-tokens')
    keywords = model.extract_keywords(data)
    return keywords

if __name__ == '__main__':
    app.run()