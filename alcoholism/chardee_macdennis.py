from random import randint
import pandas as pd

class Deck:

    def __init__(self):
        self.file_name = "ChardeeCards.xlsx"
        self.lvl1sheet = "lvl1cards"
        self.lvl2sheet = "lvl2cards"
        self.lvl3sheet = "lvl3cards"
        self.chancesheet = "chancecards"
        self.cards=[]
        self.loadData()


    def loadData(self):
        self.lvl_one = pd.read_excel(io=self.file_name, sheet_name=self.lvl1sheet).values.tolist()
        self.lvl_two = pd.read_excel(io=self.file_name, sheet_name=self.lvl2sheet).values.tolist()
        self.lvl_three = pd.read_excel(io=self.file_name, sheet_name=self.lvl3sheet).values.tolist()
        self.chance = pd.read_excel(io=self.file_name, sheet_name=self.chancesheet).values.tolist()
        self.cards = [self.lvl_one,self.lvl_two,self.lvl_three,self.chance]

    def drawHelper(self,lvl):
        deck = self.cards[lvl]
        if(len(deck)==0):
            return "No Cards Left, please reset"
        index = randint(0,len(deck)-1)
        card = deck[index]
        del(deck[index])
        return card[0]


    def draw(self,lvl):
        print("\n")
        if lvl<1 or lvl>3:
            return "level must be 1-3"

        #one fourth chance of drawing chance card
        useChance = randint(0,4)

        #if at least one deck is empty
        if(len(self.cards[lvl-1]) == 0 and len(self.cards[3]) == 0):
            return "no valid cards left, please reset deck"

        if(lvl!=3 and len(self.cards[lvl-1]) == 0):
            return self.drawHelper(3)
        
        if(len(self.cards[3]) == 0):
            return self.drawHelper(lvl-1)

        #if both decks unempty
        
        if useChance==0 and lvl!=3:  #no chance cards lvl 3
            return self.drawHelper(3)
        else:
            return self.drawHelper(lvl-1)


if __name__ == "__main__":
    deck = Deck()
    #print(deck.cards)
    for i in range(0,19+13+3):
        print(deck.draw(1))

    for i in range(0,len(deck.cards[1])+2):
        print(deck.draw(2))
    




