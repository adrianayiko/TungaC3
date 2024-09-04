from flask import Flask, render_template, request
from books import articles

app = Flask(__name__)

#code to render templates of Html 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', articles = articles)

@app.route('/hello', methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template('form.html', name=name)
    

if __name__ == '__main__':
    app.run(debug=True)