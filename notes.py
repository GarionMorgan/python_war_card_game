from random import shuffle
#two variables for creating cards
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


class Deck:
    """
    Deck class. Used for creating the deck
    """
    def __init__(self):
        print("Creating new ordered deck")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("Shuffling deck...")
        shuffle(self.allcards)

    def split_in_half(self):
        return(self.allcards[:26],self.allcards[26:])

class Hand:
    """
    Hand class. Each player has a hand in the game
    """
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:
    """
    Player class, which takes a name and an instance of the Hand class object
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed {}\n".format(self.name,drawn_card))
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                #remove_card() from Hand class
                war_cards.append(self.hand.remove_card())
            return war_cards

    def still_has_cards(self):
        """
        Returns True is player still has cards left
        """
        return len(self.hand.cards) != 0


###################
#### GAME PLAY ####
###################

def main():
    print("Welcome to War, let's begin...")

    #create a new deck and split in half
    d = Deck()
    d.shuffle()
    half1,half2 = d.split_in_half()

    #create both players
    cpu = Player("Computer",Hand(half1))

    name = input("What is your name? ")
    user = Player(name, Hand(half2))

    total_rounds = 0
    war_count = 0

    while user.still_has_cards() and cpu.still_has_cards():
        total_rounds += 1
        print("Time for a new round!")
        print("here are the current standings")
        print(user.name + "has the count: " + str(len(user.hand.cards)))
        print(cpu.name + "has the count: " + str(len(cpu.hand.cards)))
        print("play a card!\n")

        table_cards = []

        c_card = cpu.play_card()
        p_card = user.play_card()

        table_cards.append(c_card)
        table_cards.append(p_card)

        if c_card[1] == p_card[1]:
            war_count += 1

            print("War!")

            table_cards.extend(user.remove_war_cards())
            table_cards.extend(cpu.remove_war_cards())

            if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
                user.hand.add(table_cards)
            else:
                cpu.hand.add(table_cards)

        else:
            if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
                user.hand.add(table_cards)
            else:
                cpu.hand.add(table_cards)

    print("Game Over. Number of rounds:" + str(total_rounds))
    print("War happened " + str(war_count) + " times")
    print("Does the computer still have cards? ")
    print(str(cpu.still_has_cards()))
    print("Does the player still have cards? ")
    print(str(user.still_has_cards()))


if __name__ == "__main__":
    main()
