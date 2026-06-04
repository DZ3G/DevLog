from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///devlog.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.route('/')
def index():
    posts = Post.query.order_by(Post.date.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        if User.query.filter_by(username=username).first():
            flash('Nom d\'utilisateur déjà pris.')
            return redirect(url_for('register'))
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Compte créé ! Tu peux te connecter.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('index'))
        flash('Identifiants incorrects.')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        post = Post(
            title = request.form['title'],
            content = request.form['content'],
            user_id = current_user.id
        )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('post_form.html', title = 'Nouvelle entrée', post = None)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = db.session.get(Post, post_id)
    return render_template('post_detail.html', post = post)

@app.route('/post/<int:post_id>/edit', methods = ['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = db.session.get(Post, post_id)
    if post.user_id != current_user.id:
        return redirect(url_for('index'))
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        return redirect(url_for('post_detail', post_id = post.id))
    return render_template('post_form.html', title = 'Modifier', post = post)

@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = db.session.get(Post, post_id)
    if post.user_id == current_user.id:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)