from flask import Flask
app = Flask(__name__)

#define a dynamic route for veiwing blog posts by post ID

@app.route('/post/<int:post_id>')
def view_post(post_id):
    #logic t retrieve  and display blog post
    return f"Viewing Blog Post #{post_id}"