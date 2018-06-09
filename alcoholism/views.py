from flask import render_template
from alcoholism import app
from alcoholism.chardee_macdennis import *



@app.route('/')
def start():
    return render_template("drinkingproblems.html", card="Please begin with customary wine and cheese reception to fake respect for your opponent")

@app.route('/draw/<int:level>')
def draw_lvl(level):
    new_card=draw(level)
    return render_template("drinkingproblems.html", card=new_card)
