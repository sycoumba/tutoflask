from flask import Flask, app, render_template



app= Flask(__name__)

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/about')
def about():
    return render_template('pages/about.html')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')
    
@app.route('/blog')
def post_index():
    posts =[
        {'id':1, 'title':'First Post', 'content':'This is my First Post'},
        {'id':2, 'title':'Second Post', 'content':'This is my Second Post'},
        {'id':3, 'title':'Third Post', 'content':'This is my Third Post'}
    ]
    return render_template('posts/index.html', posts = posts)

@app.route('/blog/posts/<int:id>')
def post_show(id):
     posts =[
        {'id':1, 'title':'First Post', 'content':'This is my First Post'},
        {'id':2, 'title':'Second Post', 'content':'This is my Second Post'},
        {'id':3, 'title':'Third Post', 'content':'This is my Third Post'}
    ]
     post = posts[id -1]
     return render_template('posts/show.html', post = post)   

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


if __name__=='__main__':
    app.run(debug=True)