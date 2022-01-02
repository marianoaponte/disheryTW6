from flask import Flask, render_template

app = Flask(__name__, static_url_path='', template_folder='templates', static_folder='static')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addrecipe")
def test():
    return render_template("test.html")

if __name__ == '__main__':
    app.run()

