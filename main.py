from flask import Flask , render_template

app = Flask(__name__)

# route decorator

@app.route('/index')
def index():
    return "<h1>Index Page</h1>"

