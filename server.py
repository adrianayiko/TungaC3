from main import Flask 
app = Flask(__name__)

# route for "/"
@app.route('/')
def hello_world():
    return 'Hello, World!'

#route for "/about"
@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
    app.run()