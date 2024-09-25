from flask import Flask,request,render_template

app = Flask(__name__,template_folder="./Templates")

@app.route('/')
def home():
    return render_template("home.html")
    # return render_template('index.html')

@app.route('/upload')
def uploadFile():
    # print(request.files())
    return "yet to complete"

app.run(debug=True)
