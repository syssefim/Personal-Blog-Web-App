from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import json #vcode
import os   #vcode

app = Flask(__name__)
app.secret_key = 'super_secret_key'
DATA_FILE = 'articles.json' #vcode








app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost/students'
db=SQLAlchemy(app)







#--------------- vcode ---------------
# --- Helper Functions ---

def load_articles():
    """Reads all articles from the JSON file."""
    # If the file doesn't exist yet (first run), return an empty list
    if not os.path.exists(DATA_FILE):
        return []
    
    # Open the file in 'read' mode ('r')
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)  # Convert JSON text back into a Python list
        except json.JSONDecodeError:
            return [] # Return empty list if file is corrupted

def save_articles(articles):
    """Writes the list of articles back to the JSON file."""
    # Open file in 'write' mode ('w')
    with open(DATA_FILE, 'w') as f:
        # indent=4 makes the file human-readable
        json.dump(articles, f, indent=4)

def get_article(id):
    """Finds a specific article by its ID."""
    articles = load_articles()
    for article in articles:
        # We convert both to strings to ensure they match safely
        if str(article['id']) == str(id):
            return article
    return None


#-------------------------------------








@app.route("/")
@app.route("/home")
def home():
    articles = load_articles()

    return render_template("home.html", articles=articles)

@app.route("/article/<id>")
def view_article(id):
    article = get_article(id)
    
    if article:
        return render_template("article.html", article=article)
    else:
        return "Article not found", 404










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
@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    articles = load_articles()
    return render_template('admin.html', articles=articles)

if __name__ == "__main__":
    app.run()