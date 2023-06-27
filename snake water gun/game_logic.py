
import random
class Game:

    def __init__(self):
        self.choice ={'snake':1,'Water':2,'Gun':3}
        self.player_score =0
        self.computer_score =0

    def play(self):
        print("Welcome to the game of Snake,Water and Gun")
        print("-------------------------------------------------")

        while True:
            player_choice = int(input("Enter 1.snake ,2.water or 3.Gun"))
            if player_choice not in self.choice.values():
                print("Invalid input please select from the choices given.. Thank-you")
                continue

            computer_choice = random.randint(1,3)

            print("Player Choice: ",player_choice)
            print("Computer Choice: ",computer_choice)

            if computer_choice == player_choice:
                print("Its a Tie")
            elif computer_choice == 1 and player_choice == 2:
                print("Computer Win's !!")
                self.computer_score +=1
            elif computer_choice == 1 and player_choice == 3:
                print("Player Win's !!")
                self.player_score +=1
            elif computer_choice == 2 and player_choice == 1:
                print("Player  Win's !!")
                self.player_score +=1

            elif computer_choice == 2 and player_choice == 3:
                print("Computer Win's !!")
                self.computer_score +=1

            elif computer_choice == 3 and player_choice == 1:
                print("computer Win's !!")
                self.computer_score +=1
            elif computer_choice == 3 and player_choice == 2:
                print("Player has Won !!")
                self.player_score +=1
            else:
                pass



            print("Player Score :",self.player_score)
            print("Computer Score :",self.computer_score)
            play_again = input("Do you want to continue game: y/n")

            if play_again.lower() != 'y':
                break

        print("Thanks for playing the game of snake water and Gun")






game = Game()
game.play()
