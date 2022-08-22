import random

def main():
    player1=0
    player2=0
    player1_wins=0
    player2_wins=0
    rounds=1

    while rounds!=10:
        print("Round"+str(rounds))
        player1=dice()
        player2=dice()
        print("player 1 roll ",player1)
        print("player 2 roll ",player2)

        if player1==player2:
            print("draw")

        elif player1>player2:
            print("player1 wins")
            player1_wins=player1_wins+1

        elif player1<player2:
            print("player2 wins")
            player2_wins=player2_wins+1
        print()

        rounds+=1
        
    if player1_wins==player2_wins:
        print("match draw")

    elif player1_wins>player2_wins:
        print("Player 1 won the game")
    else:
        print("player 2 won the game")
    
def dice():
    dice_roll=random.randint(1,6)
    return dice_roll

main()

    
        
