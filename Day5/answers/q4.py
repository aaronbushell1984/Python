def rock_paper_scissors(choice1, choice2):
    choices = ('rock','paper','scissors')
    choice1 = choice1.lower()
    choice2 = choice2.lower()
    
    if choice1 not in choices or choice2 not in choices:
        return "Invalid choice"
    
    if choice1 == choice2:
        return "Tie"
    elif choice1 == 'rock':
        if choice2 == 'scissors':
            return "Player 1 wins"
        else:
            return "Player 2 wins"
    elif choice1 == 'paper':
        if choice2 == 'rock':
            return "Player 1 wins"
        else:
            return "Player 2 wins"
    else:
        if choice2 == 'paper':
            return "Player 1 wins"
        else:
            return "Player 2 wins"
        