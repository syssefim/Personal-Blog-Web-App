from flask import Blueprint, render_template

articles = Blueprint('articles', __name__)

@articles.route("/article/1")
def article1():
    return render_template("article1.html")

@articles.route("/article/2")
def article2():
    return "artcicle 2 page whatever"