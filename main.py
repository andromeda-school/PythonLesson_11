import random
import emoji


size = int(input("Введите размер ёлочки: "))
k = 1.0 - float(input("Введите шанс игрушек: "))

toys = [":tangerine:", ":rocket:",
        ":collision:", ":Santa_Claus:",
        ":large_blue_diamond:", ":orange_heart:",
        ":fireworks:", ":cookie:"]

for i in range(size):
    if i == 0:
        print(" "*(size-1), emoji.emojize(":star:"))
    else:
        tree_str = " "*(size-i)+" "
        for j in range(i):
            if random.random() > k:
                tree_str = tree_str + random.choice(toys)
            else:
                tree_str = tree_str + ":green_circle:"

        print(emoji.emojize(tree_str))
print(" "*(size-1), emoji.emojize(":brown_square:"))
