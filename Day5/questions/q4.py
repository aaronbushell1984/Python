def rock_paper_scissors(player1, player2):
    player1 = player1.lower()
    player2 = player2.lower()
    r = "rock"
    s = "scissors"
    p = "paper"
    while player1 != "rock" and player1 != "paper" and player1 != "scissors":
        return "Invalid choice"
    while player2 != "rock" and player2 != "paper" and player2 != "scissors":
        return "Invalid choice"
    while player1 == r and player2 == s:
        return "Player 1 wins"
    while player1 == p and player2 == r:
        return "Player 1 wins"
    while player1 == s and player2 == p:
        return "Player 1 wins"
    while player2 == r and player1 == s:
        return "Player 2 wins"
    while player2 == p and player1 == r:
        return "Player 2 wins"
    while player2 == s and player1 == p:
        return "Player 2 wins"
    else:
        return "Tie"