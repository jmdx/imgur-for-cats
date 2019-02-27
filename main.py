import flask
from flask import render_template, request
from flask import Flask

from db import init_db, query_db

app = Flask(__name__)

try:
    init_db(app)
except:
    pass


@app.route('/')
def index():
    return render_template('index.html', pics=query_db('select * from cat_pictures'))


@app.route('/<slug>')
def cat(slug):
    # Sketchy, but safe query
    slug, url, votes = query_db("select * from cat_pictures where slug = ?", args=(slug,))[0]
    return render_template('cat.html', slug=slug, url=url, votes=votes)


@app.route('/vote/<slug>', methods=['POST'])
def vote(slug):
    """
    Warning: this is dangerous code, don't do this in production
    """
    query_db("update cat_pictures set votes = votes + 1 where slug = '" + slug + "'")
    return 'success'


@app.route('/cat/add', methods=['GET'])
def add_cat():
    return render_template('add.html')


@app.route('/cat/add', methods=['POST'])
def submit_cat():
    # This is a really bad auth system, don't use this in prod
    if len(query_db('select * from api_tokens where secret = ?', args=(request.form['api-token'],))) == 1:
        query_db('insert into cat_pictures (slug, url) values (?, ?)',
                 args=(request.form['cat-slug'], request.form['cat-url']))
        return flask.redirect('/')
    else:
        flask.abort(401)
