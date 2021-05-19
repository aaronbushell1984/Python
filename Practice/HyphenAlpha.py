def hyphen_alpha(hyphens: str):
    new_sequence = ""
    withouthyphens = hyphens.split("-")
    withouthyphens.sort()
    new_sequence = "-".join(withouthyphens)
    return new_sequence


hyphens = "green-red-yellow-black-white"
print(hyphen_alpha(hyphens))