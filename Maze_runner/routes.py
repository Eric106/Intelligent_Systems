from os import system
from flask import Flask, render_template, redirect, url_for
from utils.main import a_star, brute_force
from utils.modules.mazeGenerator import generator

app = Flask(__name__)
system("del /s/q/f .\static\mazeImg")
mazeX , mazeY = 30, 16
maze = generator(mazeX , mazeY)
gifPaths = {"astar":a_star(maze),
            "brute":brute_force(maze)}

@app.route('/')
def home():
    return  render_template('index.html')

@app.route('/A')   
def A_Search():
    fileName = gifPaths["astar"]
    return render_template('a.html',fileName=fileName)

@app.route('/Brute')
def Brute():
    fileName = gifPaths["brute"]
    return render_template('brute.html',fileName=fileName)

@app.route('/mazeGenerator/<toRedirect>')
def mazeGenerator(toRedirect):
    maze = generator(mazeX , mazeY)
    gifPaths["astar"]  = a_star(maze)
    gifPaths["brute"] = brute_force(maze)
    if toRedirect == "A":
        return redirect(url_for('A_Search'))
    elif toRedirect == "Brute":
        return redirect(url_for('Brute'))

@app.route('/Video')
def Video():
    return render_template('video.html')

if __name__ == '__main__':
    app.run(debug=False)
    