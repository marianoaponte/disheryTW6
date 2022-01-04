from flask import Flask, render_template

app = Flask(__name__, static_url_path='', template_folder='templates', static_folder='static')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addrecipe")
def addrecipe():
    return render_template("addrecipe.html")

@app.route("/feed")
def feed():
    return render_template("feed.html")

@app.route("/test")
def test():
    return render_template("test.html")

if __name__ == '__main__':
    app.run()
