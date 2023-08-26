from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')  
def index():
    return render_template('html/signin.html')

@app.route('/signup.html')  
def sighnup():
    return render_template('html/signup.html')

if __name__ == '__main__':
    app.run(debug=True)


