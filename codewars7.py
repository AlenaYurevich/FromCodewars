#  To be a senior, a member must be at least 55 years old and have a handicap greater than 7.
#  In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

def open_or_senior(data):
    print(["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data])


open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6]])
