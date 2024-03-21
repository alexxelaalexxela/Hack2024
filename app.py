from flask import Flask, render_template, request, jsonify
from jessie_app import final_result
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    result = final_result(user_input)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)