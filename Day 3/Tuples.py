# immutable, ordered, duplicates
months = (
    "Jan",
    "Feb",
    "Mar", 
    "Apr"
)
print(months)
print(months[0])

# NB. tuple' object does not support item assignment
# months[2] = "May" breaks...

# These still work
print(months.index("Mar"))
print(months.count("Feb"))

# Tuples can be used to define the keys for dictionaries