from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
shopping_list = ['milk', 'eggs']

@app.route('/', methods=['GET', 'POST'])
def index():
    global shopping_list
    if request.method == 'POST':
        shopping_list.append(request.form['item'])
    return render_template('index.html',items=shopping_list)
    # return '<h1>Shopping List</h1>'

@app.route('/remove/<itemName>')
def RemoveItem(itemName):
    global shopping_list
    if itemName in shopping_list:
        shopping_list.remove(itemName)
    return redirect(url_for('index'))

@app.route('/api/items')
def get_items():
    global shopping_list
    return jsonify({'items': shopping_list})


if (__name__ == '__main__'):
    app.run(debug=True)
