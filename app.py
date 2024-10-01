from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/level1')
def level1():
    return render_template('level1.html')

if __name__ == '__main__':
    app.run(debug=True)
