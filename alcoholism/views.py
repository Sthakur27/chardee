from flask import render_template
from alcoholism import app
from alcoholism.chardee_macdennis import *

deck = Deck()


@app.route('/')
def start():
    return render_template("drinkingproblems.html", card="Rules: Each team gets 3 timeouts that can be used in between card draws or right before a challenge starts You must begin each game with the ritual of sportsmanship with the pregame wine and cheese reception, to give the illusion of respect for the other team. If the team who draws a card is unable to complete a task or answer a question the other team has the chance to steal the card. Each time a team completes a task or answers a question successfully the other team members have to take a sip of their drinks.   Questions are not allowed once the level begins; if one is asked, all players on that team must chug their drinks for 5 seconds. If a team is caught cheating the other team jumps to the next level. If the cheating team is ahead, the other team may advance to the same level. If you spill your drink, your team has to chug the drinks of the other team. No swearing after round 1 - if you do, the team of the swearer must chug the rest of their drink If a player answers their phone or replies to a text their team must drink for 5 seconds. If a card says to do one thing and the rules say to do another, the card wins. 4 cards per level to move on to 2nd level. 4 cards to move to the 3rd level. 1 final card to win the game. Please begin with customary wine and cheese reception to fake respect for your opponent")

@app.route('/draw/<int:level>')
def draw_lvl(level):
    new_card=deck.draw(level)
    return render_template("drinkingproblems.html", card=new_card)

@app.route('/reset')
def reset():
    deck.loadData()
    return render_template("drinkingproblems.html", card="Deck reloaded!")

    
