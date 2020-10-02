from flask import Flask, render_template
from utils.main import a_star, brute_force
from utils.modules.mazeGenerator import generator
from os import system

app = Flask(__name__)

@app.route('/')
def home():
    return  render_template('index.html')

@app.route('/A')
def A_Search():
    system("del /static/a.gif")
    a_star(generator(30, 20))
    return render_template('a.html')

@app.route('/Brute')
def Brute():
    system("del /static/brute.gif")
    brute_force(generator(30, 20))
    return render_template('brute.html')

@app.route('/Video')
def Video():
    return render_template('video.html')

if __name__ == '__main__':
    app.run(debug=True)
    