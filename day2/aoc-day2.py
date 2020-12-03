with open('day2/aoc-day2-data.txt') as f:
    # Read & print the entire file
    data = f.read().splitlines()


class policy:
    def __init__(self, num_limit_min, num_limit_max, letter, password):
        self.num_limit_min = num_limit_min
        self.num_limit_max = num_limit_max
        self.letter = letter
        self.password = password


def get_char_list(password):
    return [char for char in password]


list = []
for x in data:
    z = x.split()
    y = z[0].split('-')
    list.append(policy(y[0], y[1], z[1].strip(":"), z[2]))

valid_passwords = 0
# Part 1
# for p in list:
#     password_char_list = get_char_list(p.password)
#     count = 0
#     for c in password_char_list:
#         if c == p.letter:
#             count += 1
#     if int(p.num_limit_min) <= count <= int(p.num_limit_max):
#         valid_passwords += 1
# print("NUMBER OF VALID PASSWORDS: ", valid_passwords)

# Part 2:
# Each policy actually describes two positions in the password
# Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant.

containsLetter1 = False
# containsLetter2 = False
for p in list:
    password_char_list = get_char_list(p.password)
    if password_char_list[int(p.num_limit_min)-1] == p.letter:
        # print("CONTAINS CHAR IN MIN for: ", p.password)
        containsLetter1 = True

    if password_char_list[int(p.num_limit_max)-1] == p.letter:
        # print("CONTAINS CHAR IN MAX for: ", p.password)
        # containsLetter2 = True
        if containsLetter1 == False:
            valid_passwords += 1
        containsLetter1 = False
    # if containsLetter1 & containsLetter2:
    #     valid_passwords += 1
    #     containsLetter1 = False
    #     containsLetter2 = False
    # elif containsLetter1 == True & containsLetter2 == False:
    #     valid_passwords += 1
    #     containsLetter1 = False
    #     containsLetter2 = False
    # elif containsLetter1 == False & containsLetter2 == True:
    #     valid_passwords += 1
    #     containsLetter1 = False
    #     containsLetter2 = False
print("NUMBER OF VALID PASSWORDS: ", valid_passwords)
# 196 and 427 are too low.
