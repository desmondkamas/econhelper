import random

names = ["Bob", "Gertrude", "Priscilla", "Amy", "Roswell", "Frida", "Caspian", "Oprah", "Jefferson", "Kiki"]
goods = ["marble", "taco", "fire", "igloo", "elf", "water", "book", "jail", "llama", "ring", "bee", "viking", \
         "noodle", "kiss", "apple", "zebra", "gorgon", "oracle", "doggo", "cake", "queen", "hand", "paint"]

class Game(object):
    def __init__(self, p1, p2, p1_choices, p2_choices, matrix, seq=False):
        self.seq = seq
        self.p1 = p1
        self.p2 = p2
        self.p1_choices = p1_choices
        self.p2_choices = p2_choices
        self.matrix = matrix

def create_simultaneous_game(dim1, dim2=None):
    random.shuffle(names)
    random.shuffle(goods)

    player1 = names[0]
    player2 = names[1]

    if dim2 == None:
        dim2 = dim1

    p1_choices = goods[:dim1]
    p2_choices = goods[dim1: dim2 + dim1]

    mat = []
    
    for y in range(dim1):
        row = []
        for x in range(dim2):
            row.append((random.randint(0, 10), random.randint(0, 10)))
        mat.append(row)
    
    return Game(player1, player2, p1_choices, p2_choices, mat)

sample_game = create_simultaneous_game(3)

print("I generated a game for you!")
print(f"{sample_game.p1} and {sample_game.p2} are playing a game where they pick objects and get different points")
p1_line = f"{sample_game.p1} can pick between"
for choice in range(len(sample_game.p1_choices)):
    if choice == len(sample_game.p1_choices) - 1:
        p1_line = p1_line[:-1] + f" and {sample_game.p1_choices[choice]}"
    else:
        p1_line += f" {sample_game.p1_choices[choice]},"
p1_line += f", and {sample_game.p2} can pick between"
for choice in range(len(sample_game.p2_choices)):
    if choice == len(sample_game.p2_choices) - 1:
        p1_line = p1_line[:-1] + f" and {sample_game.p2_choices[choice]}"
    else:
        p1_line += f" {sample_game.p2_choices[choice]},"
print(p1_line)

line = "\t"
for choice2 in range(len(sample_game.p2_choices)):
    line += f"{sample_game.p2_choices[choice2]}\t"
print(line)

for choice1 in range(len(sample_game.p1_choices)):
    line = f"{sample_game.p1_choices[choice1]}:\t"
    for choice2 in range(len(sample_game.p2_choices)):
        line = line + f"{sample_game.matrix[choice1][choice2]}{' ' if sample_game.matrix[choice1][choice2][0] != 10 else ''}{' ' if sample_game.matrix[choice1][choice2][1] != 10 else ''}"
    print(line)
