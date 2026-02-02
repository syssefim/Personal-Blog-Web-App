from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import json #vcode
import os   #vcode

app = Flask(__name__)
app.secret_key = 'super_secret_key'








app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost/personal_blog_db'
db=SQLAlchemy(app)


class Article(db.Model):
    __tablename__ = 'articles'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Article {self.title}>'
    

with app.app_context():
    db.create_all()












@app.route("/")
@app.route("/home")
def home():
    articles = Article.query.all()
    return render_template("home.html", articles=articles)

@app.route("/article/<id>")
def view_article(id):
    article = Article.query.get_or_404(id)
    return render_template("article.html", article=article)










@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "password":
            session["logged_in"] = True
            return redirect(url_for("admin"))
        else:
            flash("Invalid credentials")

    return render_template("login.html")



@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("home"))










#admin pages
@app.route("/admin")
def admin():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    
    articles = Article.query.all()
    return render_template("admin.html", articles=articles)


if __name__ == "__main__":
    app.run()