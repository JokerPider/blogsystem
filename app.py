#coding: utf-8
from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
Bootstrap(app)


class Post(db.Model):
	__tablename__ = "post"

	id = db.Column(db.Integer(), primary_key=True)
	author = db.Column(db.String(255))
	title = db.Column(db.String(255))
	date = db.Column(db.DateTime(), default=datetime.now)
	text = db.Column(db.Text())
	tag = db.Column(db.String(255))

	def __repr__(self):
		return "<Post %s>" % self.title


@app.route('/')
def big():
	"""欢迎页面"""
	return render_template('big.html', all=all)

@app.route('/index/')
def index():
	'''目录页面'''
	return render_template('index.html')

@app.route('/text/<id>')
def text(id):
	post = Post.query.filter_by(id=id).first_or_404()
	return render_template('text.html',
		author=post.author,
		title=post.title,
		date=post.date,
		text=post.text)

if __name__ == "__main__":
	app.run()