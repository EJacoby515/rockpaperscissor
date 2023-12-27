import random

class RockPaperScissors():
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def gamerules(self):
        print("In case you didn't know, Rock , Paper, Scissors is  a game of chance.") 
        print("It has three possible outcomes: a draw, a win or a loss. A player who")
        print("decides to play rock will beat another player who has chosen scissors (Rock crushes Scissors)")
        print(" but will lose to one who has played paper (paper covers rock); a play of")
        print("paper will lose to a play of scissors (scissors cuts paper). If both players")
        print("choose the same shape, the game is tied and is usually replayed to break the tie.")

    def user_input(self):
        rps = input("What do you choose? 'R'ock, 'P'aper, or 'S'cissor? or 'Q'uit': \n")
        if rps.upper() == 'R':
            return 'rock'
        elif rps.upper() == 'P':
            return 'paper'
        elif rps.upper() == 'S':
            return 'scissors'
        elif rps.upper() == 'Q':
            return 'quit'
        else:
            print("Invalid choice. Please try again.")
            return self.user_input()

    def comp_turn(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, comp_choice):
        if user_choice == comp_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and comp_choice == 'scissors') or (user_choice == 'paper' and comp_choice == 'rock') or (user_choice == 'scissors' and comp_choice == 'paper'):
            return "You win!"
        else:
            return "Computer wins!"

    def play_game(self):
        self.gamerules()
        while True:
            user_choice = self.user_input()
            if user_choice == 'quit':
                break
            comp_choice = self.comp_turn()
            print("Computer chooses:", comp_choice)
            print(self.determine_winner(user_choice, comp_choice))

game = RockPaperScissors()
game.play_game()