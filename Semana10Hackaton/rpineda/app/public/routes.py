import logging

from flask import abort, render_template, redirect, url_for
from flask_login import current_user
from app.models import Producto
from .forms import CommentForm
from . import public_bp


logger = logging.getLogger(__name__)


@public_bp.route("/")
def index():
    logger.info('Mostrando los posts del blog')
    productos = Producto.get_all()
    return render_template("public/index.html", productos=productos)


# @public_bp.route("/p/<string:slug>/", methods=['GET', 'POST'])
# def show_post(slug):
#     logger.info('Mostrando un post')
#     logger.debug(f'Slug: {slug}')
#     post = Post.get_by_slug(slug)
#     if not post:
#         logger.info(f'El post {slug} no existe')
#         abort(404)
#     form = CommentForm()
#     if current_user.is_authenticated and form.validate_on_submit():
#         content = form.content.data
#         comment = Comment(content=content, user_id=current_user.id,
#                           user_name=current_user.name, post_id=post.id)
#         comment.save()
#         return redirect(url_for('public.show_post', slug=post.title_slug))
#     return render_template("public/post_view.html", post=post, form=form)


@public_bp.route("/error")
def show_error():
    res = 1 / 0
    posts = Producto.get_all()
    return render_template("public/index.html", posts=posts)