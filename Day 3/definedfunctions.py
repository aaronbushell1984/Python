def print_simple_list(list, title):
    print(f"\n=== {title} ===")
    for item in list:
        print(item)
    return

languages = ["Python", "Java", "JavaScript", "SQL"]
print_simple_list(languages, "My Languages")

numbers = [9,8,7,6,5,4]
print_simple_list(numbers, "My Numbers")