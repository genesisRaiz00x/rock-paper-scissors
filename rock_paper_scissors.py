import random as rd



def moves():
    player_move=input('enter your choice [rock,paper,scissors]')
    options=['rock','paper','scissors']
    computer_move=rd.choice(options)
    choice_dictionary={'player':player_move,'computer':computer_move}

    return choice_dictionary



def winning_checker(player,computer):
    
  

    if player==computer:
        return 'ohhh!!! its a tie!'
    
    elif player=='rock':
        if computer=='scissors':
            return 'rock busted the scissors , you won!!!'
        
        else:
            return 'paper caught the rock , you loose!!!'
        
    elif player=='paper':
        if computer=='rock':
            return 'paper caught the rock , you won!!!'
        
        else:
            return 'scissors cut the paper , you loose!!!'
        
    elif player=='scissors':
        if computer=='paper':
            return 'scissors cut the paper , you won!!!'
        else:
            
            return 'rock busted the scissors ,you loose!!!'
        


def main_body():
    # comp_points=0
    game_start=moves()
    result=winning_checker(game_start['player'],game_start['computer'])
    print(result)



main_body()



