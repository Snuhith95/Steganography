from flask import Flask,request,render_template,make_response,Response

app = Flask(__name__,template_folder="./Templates")

@app.errorhandler(Exception)
def errFunc(e):
    return f'<h1>Error Occured</h1><h4>{e}</h4>'

@app.route('/')
def home():
    return render_template("form.html")

f=[]

@app.route('/upload', methods=['POST'])
def uploadFile():
    print("check")
    print(request.form)
    f.append(request.files['image'])
    return render_template("success.html")

@app.route('/download')
def success():
    res = Response("heyy", content_type='image/jpeg')
    res.headers['Content-Disposition'] = 'attachment; filename=your_image.jpg'
    return res


app.run(debug=True)
