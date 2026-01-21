from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

#import the articles blueprint
from articles import articles
app.register_blueprint(articles)



if __name__ == "__main__":
    app.run()