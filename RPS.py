import random

class RockPaperScissors():
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def user_input(self):
        rps = input("What do you choose? 'R'ock, 'P'aper, or 'S'cissor?: \n")
        if rps.upper() == 'R':
            return 'rock'
        elif rps.upper() == 'P':
            return 'paper'
        elif rps.upper() == 'S':
            return 'scissors'
        elif rps.lower() == 'quit':
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
        while True:
            user_choice = self.user_input()
            if user_choice == 'quit':
                break
            comp_choice = self.comp_turn()
            print("Computer chooses:", comp_choice)
            print(self.determine_winner(user_choice, comp_choice))

game = RockPaperScissors()
game.play_game()