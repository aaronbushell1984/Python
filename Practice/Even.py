def is_even_in_list(list):
    even_list = []
    for number in list:
        if number % 2 == 0:
            even_list.append(number)
    return even_list