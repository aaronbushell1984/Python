# ***LESSON***

languages = ["Python", "Java", "Javascript", "SQL"]

# slicing
print("First element:", languages[0])
print("First element:", languages[-1])
print("Step:", languages[0:3:2])
part_languages = languages[0:3:2]
print("Part:", part_languages)

# membership
if "Java" in languages:
    print("Java is present")
if "c++" in languages:
    print("C++ not present")

# list manioulation
languages.append("c++")
languages.insert(2, "c#")
print("After additions", languages)