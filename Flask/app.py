import json, os.path
from flask import Flask, render_template, request, redirect,url_for,flash
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.secret_key = 'qwerty1234'
@app.route('/')
def home():
    return render_template('home.html', name='Singh')
@app.route('/your-url', methods=['GET','POST'])
def your_url():
    if request.method=='POST':
        urls={}
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
        if request.form['code'] in urls.keys():
            flash('That shortname has already been taken, please select another name')
            return redirect(url_for('home'))

        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url': request.form['url']}
        else:
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename)
            f.save('/Users/abhisheksingh/DataspellProjects/mcb2/flask/'+full_name)
            urls[request.form['code']] = {'file': full_name}

        with open('urls.json','w') as url_file:
            json.dump(urls, url_file)
        return render_template('your_url.html', name='Singh', code=request.form['code'])
    else:
        return redirect(url_for('home'))


@app.route('/<string:code>')
def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls=json.load(urls_file)
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
@app.route('/about')
def about():
    return 'My First Flask project!'

