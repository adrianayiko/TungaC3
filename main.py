from flask import Flask, render_template, request

app = Flask(__name__)

#code to render temlates of Html 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    names = 'mark'
    return render_template('about.html', autor = names)

@app.route('/hello', methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template('form.html', name=name)
    

if __name__ == '__main__':
    app.run(debug=True)