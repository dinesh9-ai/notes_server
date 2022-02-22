from flask import render_template,request,redirect,url_for,flash,Flask
app=Flask(__name__,static_url_path='/static')
@app.route("/")
def index():
    return render_template("index.html")
#h&s code
@app.route("/h1_1")
def h1_1():
    return render_template("h1_1.html")
@app.route("/h1_2")
def h1_2():
    return render_template("h1_2.html")
#ece code
@app.route("/es2_1")
def es2_1():
    return render_template("es2_1.html")
@app.route("/es2_2")
def es2_2():
    return render_template("es2_2.html")
@app.route("/es3_1")
def es3_1():
    return render_template("es3_1.html")
#cse code
@app.route("/cs2_1")
def cs2_1():
    return render_template("cs2_1.html")
@app.route("/cs2_2")
def cs2_2():
    return render_template("cs2_2.html")
@app.route("/cs3_1")
def cs3_1():
    return render_template("cs3_1.html")