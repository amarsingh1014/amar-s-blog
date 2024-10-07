from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz  # Import pytz for timezone handling
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')  # Update with your credentials
db = SQLAlchemy(app)

# Existing Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)  # Date field
    tags = db.relationship('Tag', secondary='post_tags', backref=db.backref('posts', lazy='dynamic'))

    @property
    def date_posted_ist(self):
        """Convert UTC datetime to IST."""
        utc_zone = pytz.utc
        ist_zone = pytz.timezone('Asia/Kolkata')
        utc_dt = utc_zone.localize(self.date_posted)  # Localize the UTC datetime
        return utc_dt.astimezone(ist_zone)  # Convert to IST

# New Tag model
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

# Association table for the many-to-many relationship between Post and Tag
post_tags = db.Table('post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        tag_names = request.form['tags'].split(',')  # Assume tags are comma-separated
        
        new_post = Post(title=title, content=content)
        
        for tag_name in tag_names:
            tag_name = tag_name.strip()
            if tag_name:
                tag = Tag.query.filter_by(name=tag_name).first()
                if not tag:
                    tag = Tag(name=tag_name)
                new_post.tags.append(tag)
        
        db.session.add(new_post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html')

@app.route('/')
def home():
    posts = Post.query.order_by(Post.date_posted.desc()).all()  # Get posts from the database
    return render_template('index.html', posts=posts)  # Only serve database posts

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)

@app.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if query:
        posts = Post.query.filter(
            (Post.title.ilike(f'%{query}%')) | 
            (Post.content.ilike(f'%{query}%'))
        ).all()
    else:
        posts = Post.query.all()  # Return all posts if no query

    return render_template('partials/posts.html', posts=posts)  # Create a new partial template for posts

@app.route('/tag/<tag_name>')
def tag(tag_name):
    tag = Tag.query.filter_by(name=tag_name).first_or_404()
    posts = tag.posts.order_by(Post.date_posted.desc()).all()
    return render_template('tag.html', tag=tag, posts=posts)

if __name__ == '__main__':
    with app.app_context():  
        db.create_all() 
    app.run(debug=True)
