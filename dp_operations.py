from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

def add_post(title, content):
    new_post = Post(title=title, content=content)
    db.session.add(new_post)
    db.session.commit()
    print(f'Post "{title}" added successfully!')

def delete_post(post_id):
    post = Post.query.get(post_id)
    if post:
        db.session.delete(post)
        db.session.commit()
        print(f'Post with ID {post_id} deleted successfully!')
    else:
        print(f'Post with ID {post_id} not found.')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
        # Example usage:
        # add_post('My First Post', 'This is the content of my first post.')
        # delete_post(1)  # Replace 1 with the ID of the post you want to delete
