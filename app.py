from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=["GET"])  # @app.get("/")
def index_get():
    return render_template('index.html')
    

@app.route('/', methods=["POST"])  # @app.post("/")
def index_post():
    message = request.form['message']


    
    return render_template("index.html", message=message)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 