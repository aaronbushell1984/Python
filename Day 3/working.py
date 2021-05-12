# ***LESSONS***
# key/value pairs, key must be unique, mutable
countries = {
    "Brazil"    :   "Coffee",
    "Canada"    :   "Timber",
    "UK"        :   "Services",
}

for key in countries:
    print("key", key)
    print("value", countries[key])

# NB.COMBINED ACCESS OF KEY AND VALUE
for key, value in countries.items():
    print("key:", key, "value:", value)

# Change a value
countries["Canada"] = "Maple Syrup"
print(countries)
# NB TYPO WOULD ADD A NEW KEY WITH NO ERROR
countries["Canadax"] = "Maple Syrup"
print(countries)
# add a new set
countries["France"] = "Wine"
print(countries)
# remove a set
countries.pop("Canadax")
print(countries)

# List inside a dictionary
# Bank account - build up rather than assign immediately
# Create empty
bank = {}
# Create account as lists
davids_account = ["David", 2000.00]
bills_account = ["BILL", 2403.45]
# assign keys to accounts
bank[10000001] = davids_account
bank[10000002] = bills_account
print("\n*** BANK ACCOUNTS ***")
print(bank)

bank[10000001][1] += 1000
bank[10000002][0] = "Bill"
print(bank)
