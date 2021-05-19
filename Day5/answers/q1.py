def binary_odds(input_list):
    odds = []
    
    for number in input_list.split():
        if number[-1] == "1":
            odds.append(number)
    
    return odds
