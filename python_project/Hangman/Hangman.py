from getpass import getpass
import numpy as np
import os

class Hangman:
    
    def __init__(self, player_1_word:str) -> None:
        self.player_1 = player_1_word
        self.temp = player_1_word
        self.flag = 1
        self.finded_letters = ["_"]*len(self.player_1) 
        self.wrong_list = []
        
    """_summary_
    
    find given guessing letter is correct 
    parameters :-
        letter_guess:str => player 2 guessed letter
    retrun :-
        str => all finded correct letters
    """
    def correct_ans(self, letter_guess:str) -> str:
        if letter_guess in self.player_1:
            print('your ans in correct')
            for i, l in enumerate(self.player_1):
                if letter_guess == l:
                    self.finded_letters[i] = l
                    self.temp = self.temp[:i]+ self.temp[i+1:]
        return "".join(self.finded_letters)
    
    """_summary_
    
    find given guessing letter is wrong
    parameters :-
        letter_guess:str => player 2 guessed letter
    retrun :-
        str => all finded wrong letters
        flag:int => indicate errors (game allowed only 5 errors) and input to create_hangman method
    """
    def worng_ans(self, letter_guess:str) -> list[str, int]:
        if letter_guess not in self.player_1:
            print("you're answer is wrong")
            self.wrong_list.append(letter_guess)
            self.flag += 1
        return [" ".join(self.wrong_list), self.flag]
            
    """_summary_
    
        create hagman based on flag(errors)
        parameter :-
            flag => indicates error
        return :-
            str => Hangman drawing based on flags
    """
    # def __str__(self) -> str:
    def create_hangman(self, flag:int) -> str:
        hangman_matrix = [[' 'for j in range(5)]for i in range(4)]
        if flag > 0:
            (hangman_matrix[0][1], 
            hangman_matrix[0][4],
            hangman_matrix[1][4],
            hangman_matrix[2][4],
            hangman_matrix[3][4]) = ['|']*5
            
        if flag > 1:
            (hangman_matrix[0][2],
            hangman_matrix[0][3]) = ['-']*2
        
        if flag > 2:
            ## hangman-head
            hangman_matrix[1][0] = '('
            hangman_matrix[1][2] = ')'
            hangman_matrix[1][1] = '.'
        
        if flag > 3:
            ## Hangman - body
            hangman_matrix[2][1] = '|'
            hangman_matrix[3][1] = '.'
        
        if flag > 4:
            ## hangman - hand
            hangman_matrix[2][0] = '-'
            hangman_matrix[2][2] = '-'
            
        if flag > 5:
            ## hangman - leg
            hangman_matrix[3][0] = '/'
            hangman_matrix[3][2] = "\ ".strip()
        hangman_string = "\n".join(["".join(lis).center(40) for lis in hangman_matrix])
        return hangman_string
    
    
### player 1 starting and enter the word
# print("Player 1 start your game")
# player_1 = getpass("please enter your word : ")
# print()
file_path = "/home/devaraj/Documents/Python/python_project/Hangman/words.txt"
with open(file_path) as file:
    player_1 = np.random.choice(file.read().split("\n"))

print("".join(['*']*40))
### player start and enter the guessing letters
print("player start your game")
print(f"Word contains totally : {len(player_1)} letters")
print(" ".join(['_']*len(player_1)))
game: Hangman = Hangman(player_1)

correct = ''
flag = 0

### while loop for finding player 1 and player 2 letters are matching
while(correct != player_1):
    
    if (flag != 6):
        player_2 = input("Enter your guess (Enter only one letter) : ")
        correct = game.correct_ans(player_2)
        wrong, flag = game.worng_ans(player_2)
        
        print(game.create_hangman(flag))
        print(f'correct guess : {" ".join(list(correct))}')
        print(f'wrong guess : {wrong}')
        print(f"! You have only {6-flag} guesses")
        print()
        print(f'{"".join(['=']*50)}')
        print()
    else:
        print("----- You Lose -----")
        break

if (correct == player_1):
    print("----- You Won ------")

print(f"Correct answer is : {player_1}")
print("----- Game Over -----")








        