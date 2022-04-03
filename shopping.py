from pydoc import render_doc
from flask import Flask
from flask import render_template

app = Flask(__name__)
shopping_list = ['milk', 'eggs']


@app.route('/')
def index():
    return render_template('index.html',items=shopping_list)
    # return '<h1>Shopping List</h1>'


if (__name__ == '__main__'):
    app.run(debug=True)
