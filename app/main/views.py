from flask import render_template,request,redirect,url_for
# from app import app
from ..requests import get_sources,get_article
from . import main


#views
@main.route("/")
def index():
    """View root page function that returns the index page and its data"""
    news = get_sources()
    title = 'News - Get yourself newsed up'
    return render_template("index.html",title = title ,news=news)


@main.route("/news/<id>")
def article(id):
    """View article page that returns articles and their data"""
    article = get_article(id)
    #title = f"{article.title}"

    return render_template("article.html",article=article)