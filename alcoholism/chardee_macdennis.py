import random
lvl_one=["Draw the word to the best of your abilities on a team mate’s back (if you draw an artistry card there will be a word written on it).First team to identify the drawing strictly by feel, wins the card.",
"Puzzle: Choose a conspicuous object bigger than a tennis balld and hide object for the other team to find in 3 min.",
"Artistry: opposing team comes up with a movie name, you have 1 minute to charade it to make your team guess correctly",
"Puzzle: play the google map game, if you guess within the same country as the answer you win",
"Artistry: all play, choose blind judges from each team and each team has to make the best sexy haiku about a professor",
"Artistry: draw an animal but can only put pencil in mouth. Team has to guess animal correctly in half a minute.",
"Artistry: do an interpretive dance of an opposing team member, your team has to guess directly",
"All play: One teammate is given the clue of a thing. That teammate must charade out the clue while the other teammate attempts to draw it. finally, another teammate who hasn't seen either charades or drawing has 10 seconds to see the drawing and guess the word",
"All play: See who can stack any objects in the room the highest in thirty seconds. The team with the tallest tower standing without any human support wins",
"Puzzler: Have the opposing team write down a 10-digit number on a piece of paper and hand it to a player on your team. The player can then speak the number only once. The remaining players on the team then have to keep the number in their heads (no speaking) for 30 seconds starting after the last digit was spoken. During the 30 seconds the opposing team cant distract/talk.",
"Trivia: all play: write down as many dinosaurs as you can in 10 seconds. If there’s a tie then both teams drink and no one gets card.",
"Trivia: look up 4 random countries (random generator) and name 1 correct capitol.",
"Trivia: Name all players who won the last game of chardee macdennis",
"Trivia: Name 4 international capitals in ten seconds.",
"Trivia: Have the other team write down a 1-digit number and a 2-digit number. Your team has 30 seconds to multiply those numbers in your heads (no paper, no calculator).",
"Trivia: name the youngest player on opposite team",
"All Play: choose the most sober member on each team. They each pour exactly a shot into an unmarked glass. Whoever pours the closest amount to a shots wins. Losers have to finish whatever was poured",
"Trivia; name a popular news story from today",
"Puzzle: draw a picture, let one person on the enemy team rip up the paper for 10 seconds, then the rest of the team of the person who drew this card must figure out what the drawing was in 30 seconds."]
lvl_two=["Successfully flip a water bottle in five attempts or fewer.",
"all Play: blindfolded race of one member of each team from one side of the room to the other.",
"Choose one member of the opposing team to strike your bare ass with a ruler. No flinching.",
"for the rest of the game, if you say someone's name, they slap you",
"Dragon’s Breath:  Take a shot of hot sauce.",
"Choose 1 member of the enemy team to have a staring contest with",
"Get tickled for 30 seconds without laughing. Choose opposing team member who tickles",
"Close eyes and balance on one foot while putting your hands together in namaste form for 30 seconds without falling/stumbling",
"All play: team with member who comes to doing the splits wins",
"Push-ups  until 1 member of your team finishes 2 beer.",
"Plank until 1 member of ur team finishes 2 beer.",
"take a new beer to use for the game. Pour a shot of milk into it. If you have to drink during the game, you have to drink from the milk'd beer",
"Sing 'Twinkle Twinkle Little Star' while chugging a beer.",
"Flip-a-delphia: All play, a team relay race using standard flip cup rules.",
"Two on One: You must challenge two people from an opposite team to a drink off using a beer, the people you challenge use half a beer each.",
"place a full ice cube in your armpit and hold it there until it melts",
"finish your drink, then come up with a verbal rule and punishment for the rest of the game (ie. if they say something then they get punished)"
"choose 1 member on your team. stand 5 feet apart and your teammate has one chane to throw a pong ball into your mouth to win. You can move to catch ball in mouth as soon as ball is in air",
"A member of the opposing team gets to five star a member of the other. In order for the team to keep the card they must not flinch or show signs of pain.",
"all play: place an object in the middle of the room and each team starts on different sides of the room. Whoever is in possession of the item at the end of 1 minute wins, or overtime if necissary",
"Do a plank while a member of your team sits on your back and finishes a beer.",
"High noon. each team chooses a champion. Give them a fresh beer. they start back to back, someone signals, they walk out for 5 seconds, turn around, face each other, and chugg. First to finish wins"]
lvl_three=["Show your underwear to the group. If you’re not wearing underwear, prove it.",
"Identify the member of the group for whom you would “go gay/straight” and provide a compelling argument for why.",
"Shave a noticeable amount of hair from anywhere on your body.",
"Identify the parent or loved one, of a member of the group, with whom you would sleep and provide a compelling argument for why",
"Identify the member of the group whom you would eat first should you have to resort to cannibalism. Provide a compelling argument for why.",
"Identity Theft: You must hand your cell phone over to the opposing team. You must watch and listen as the opposing team is given 2 min to send embarrassing text messages to anyone on your contact list. Each text can only be sent to one person at a time (no mass forwarding). If you complain, ask them to stop, or obstruct the other team in any way you lose. If you don’t have a cell phone a member of your team may take your place.",
"Give a mock demonstration of 5 sex positions with a teammate of the same sex. You have 60 seconds.",
"Give yourself a Mohawk using shaving cream.",
"Whoever pulled the card has 30 seconds to do one job: keep a straight face. The other team can do everything it takes to break them, except for physical contact. Make them laugh or make them flinch. Making them flinch is usually the easiest route, so if you make the player flinch, each member of that team takes a shot and you move on. However, if you make them laugh, after they take their shot, you get a fake out round. You can either slap them across their face, after which there are no further consequences, or you can try to make them flinch. If you make them flinch, they take another shot, but if you fail, your team takes a shot.",
"Play the rest of the game in your underwear. Get the point in 3 more card draws",
"Enemy team writes a speech and you have to deliver",
"Don't read out loud: look at a member of the opposing team and make orgasmic noises for 30 seconds without breaking eye construct",
"Pick and lick: Pick Someone lick armpit",
"Choose 1 opposing team member, call them daddy and then they slap you",
"Let a member of the opposing team give you a tattoo with a marker anywhere. Size restriction of 5 inches",
"opposing team chooses one member, you have to kiss them"]
chance=["Finish the drink of someone on the opposing team",
"Handcuffs- You must hold hands with a teammate for the remainder of the game. (Makes bathroom trips awkward). Get the point in 3 more card draws",
"Challenge a member of the opposing team to a duel in customary fashion",
"Draw a level 1 card instead",
"Eat a whole piece of paper",
"Gamble one of your team’s cards for one of your opponent’s! Rock Paper Scissors",
"Everytime you say the word “that” you must drink",
"Wear a piece of clothing of  another member of your team unconventionally",
"The opposing team chooses an accent and you have to do it. Drink every time you mess up",
"opposing team chooses an item. you have one minute to tag whoever is holding it or catch it in middair. Opposing team can throw item/etc",
"Come up with a catch phrase and you have to say it everytime someone says your name",
"Flip a coin, if heads you gain this card, tails you lose a card",
"all play: whoever can shed a tear first wins",
"One free get out of cheating card. This doesn't count as a point",
"Eat the closest edible object",
"All play, best twerker wins",
"Bite whatevers is in your hand. If empty bite your hand",
"choose an opposing team member. Come up with a dare. Call heads or tails. Flip a coin. Winner gets card, loser must do dare"]

for i in range(0,len(chance)):
    chance[i]="Chance! \n"+chance[i]



def draw(lvl):
    print("\n")
    if lvl<1 or lvl>3:
        return "level must be 1-3"
    a=[]
    if lvl==1:
        a=lvl_one
    if lvl==2:
        a=lvl_two
    if lvl==3:
        a=lvl_three
    a+=random.choices(chance,k=4)
    return(random.choice(a))


'''while True:
    inp=input("Add a team name or hit enter to stop adding teams")
    if inp="":
        break
    teams.append([inp,0])

def add_point(team_num):
    teams[team_num][
'''




