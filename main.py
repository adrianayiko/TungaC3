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
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    #logic to create a new article 
    if request.method == "GET":
        return render_template('form.html')
    if request.method == "POST":
        #retrieve data from form
        author = request.form['author']
        title = request.form['title']
        details = request.form['details']
        
        #add article to list 
        articles.append({"title": title, "author": author, "details":details})
        
    return render_template('form.html')
    

if __name__ == '__main__':
    app.run(debug=True)