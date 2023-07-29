from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html', name='Singh')
@app.route('/your-url', methods=['GET','POST'])
def your_url():
    if request.method=='POST':
        return render_template('your_url.html', name='Singh', code=request.form['code'])
    else:
        return 'This is not valid'
@app.route('/about')
def about():
    return 'My First Flask project!'