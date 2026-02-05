from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import json
import os
import datetime
from dotenv import load_dotenv







app = Flask(__name__)
app.secret_key = 'super_secret_key'







# Load variables from the .env file
load_dotenv()
db_password = os.getenv("DB_PASSWORD")
app.config['SQLALCHEMY_DATABASE_URI']=f'postgresql://postgres:{db_password}@localhost/personal_blog_db'
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
    return render_template("home.html", articles=articles, is_logged_in=session.get("logged_in"))

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
#home page for admin
@app.route("/admin")
def admin():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    
    articles = Article.query.all()
    return render_template("admin.html", articles=articles)

#edit article
@app.route("/admin/edit/<id>", methods=["GET", "POST"])
def edit_article(id):
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    article = Article.query.get_or_404(id)

    if request.method == "POST":
        article.title = request.form["title"]
        article.date = request.form["date"]
        article.content = request.form["content"]

        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template("edit.html", article=article)

#new article
@app.route("/admin/new", methods=["GET", "POST"])
def new_article():
    if not session.get("logged_in"):
        return redirect(url_for("login"))

    if request.method == "POST":
        #the form gets the title and content from the user
        title = request.form["title"]
        content = request.form["content"]

        #then use datetime to get the current date
        current_datetime = datetime.datetime.now()
        date = current_datetime.strftime("%B %d, %Y")

        article = Article(title=title, date=date, content=content)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template("new.html")

#delete article
@app.route("/admin/delete/<id>")
def delete_article(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    return redirect(url_for("admin"))

if __name__ == "__main__":
    app.run()