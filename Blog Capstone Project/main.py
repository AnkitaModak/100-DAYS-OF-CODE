from flask import Flask, render_template
import requests

blog_data = requests.get(url="https://api.npoint.io/813c044d51e8707883ea").json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blogs=blog_data)


@app.route('/post/<int:id_num>')
def each_post(id_num):
    return render_template("post.html", posts=blog_data, ID=id_num)


if __name__ == "__main__":
    app.run(debug=True)
