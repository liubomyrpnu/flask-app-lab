# app/posts/views.py — 100% ПРАВИЛЬНЫЙ ВАРИАНТ ПО ТВОЕМУ PDF!
from flask import Blueprint, render_template, request, flash, redirect, url_for
from app import db
from app.posts.models import Post
from app.posts.forms import PostForm

# ← ВАЖНО: создаём blueprint БЕЗ url_prefix!
posts_bp = Blueprint('posts', __name__, template_folder='templates/posts')

@posts_bp.route('/')
def index():
    posts = Post.query.order_by(Post.posted.desc()).all()
    return render_template('all_posts.html', posts=posts)

@posts_bp.route('/<int:id>')
def detail(id):
    post = Post.query.get_or_404(id)
    return render_template('detail_post.html', post=post)

@posts_bp.route('/create', methods=['GET', 'POST'])
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, category=form.category.data)
        db.session.add(post)
        db.session.commit()
        flash('Пост створено!', 'success')
        return redirect(url_for('posts.index'))
    return render_template('add_post.html', form=form, title="Новий пост")

@posts_bp.route('/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    post = Post.query.get_or_404(id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.category = form.category.data
        db.session.commit()
        flash('Пост оновлено!', 'info')
        return redirect(url_for('posts.detail', id=post.id))
    return render_template('add_post.html', form=form, title="Редагування")

@posts_bp.route('/<int:id>/delete', methods=['GET', 'POST'])
def delete(id):
    post = Post.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(post)
        db.session.commit()
        flash('Пост видалено!', 'danger')
        return redirect(url_for('posts.index'))
    return render_template('delete_confirm.html', post=post)