import fizzbuzz

def start():
    number = int(input("Please enter a number:"))
    print(fizzbuzz.apply_fizz_buzz_rules(number))

# Application entry point
if __name__ == "__main__":
    start()