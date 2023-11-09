from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
  return render_template('homepage.html')


@app.route("/login")
def login():
  return render_template('login.html')


@app.route("/register")
def register():
  return render_template('register.html')


@app.route("/contactus")
def contactus():
  return render_template('contactus.html')

@app.route("/partners")
def partners():
  return render_template('partners.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
