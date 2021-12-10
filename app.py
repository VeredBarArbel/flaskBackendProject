from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def redirect_about_func():
    print('Hey There')
    return redirect(url_for('about_func'))

@app.route('/aboutMe')
def about_func():
    return 'I am Awesome!'

@app.route('/contact')
def redirect_phone_func():
    return redirect('/phone')

@app.route('/phone')
def phone_func():
    return 'My phone number is 050-1234567'

if __name__ == '__main__':
    app.run(debug=True)
