from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/")
def index():
    age=23
    return render_template('home.html', age=age)
 
if __name__ == "__main__":
    app.run()