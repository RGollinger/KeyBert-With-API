#%%
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

    if 'range' not in form:
        range = 1
    else:
        range = form['range']
    results = keybertify(form['data'], range)

    return jsonify(results)

def keybertify(data, range = 1):
    data = data
    range = int(range)
    model = KeyBERT('distilbert-base-nli-mean-tokens')
    keywords = model.extract_keywords(data, keyphrase_ngram_range=(1,range))
    return keywords

if __name__ == '__main__':
    app.run()
# %%
