from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': {
            'username': 'test-user'
        },
        'title': 'first post',
        'content': 'first post content',
        'date_posted': datetime.strptime('2018-08-01', '%Y-%m-%d')
    },
    {
        'author': {
            'username': 'test-user'
        },
        'title': 'second post',
        'content': 'second post content',
        'date_posted': datetime.strptime('2018-08-03', '%Y-%m-%d')
    },
]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
  return render_template('about.html', title='About')

if __name__=="__main__":
   app.run()