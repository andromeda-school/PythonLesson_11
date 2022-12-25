import random

import emoji

#   Елочка из емодзи в терминале
#   https://carpedm20.github.io/emoji/
#   python -m pip install emoji --upgrade

size = int(input("Введите размер елочки: "))
k = 1.0 - float(input("Введите шанс игрушек: "))

# simple_toys = [
#     ":red_circle:", ":orange_circle:", ":white_circle:",
#     ":yellow_circle:", ":blue_circle:"
# ]

toys = [
    ":tangerine:", ":rocket:",
    ":collision:", ":Santa_Claus:",
    ":large_blue_diamond:", ":orange_heart:",
    ":fireworks:", ":cookie:"
]

for i in range(size):
    if i == 0:
        print(" "*(size-1) + emoji.emojize(":star:"))
    else:
        line = " " * (size-i)
        for j in range(i):
            if random.random() > k:
                line = line + random.choice(toys)
            else:
                line = line + ":green_square:"
        print(emoji.emojize(line))
print(" " * (size-1)+emoji.emojize(":brown_square:"))


# key = 1
# for i in range(size):
#     if i == 0:
#         print(" "*(size-1) + emoji.emojize(":star:"))
#     else:
#         if size // 3 == i or (size - size // 3) == i:
#             key = 1
#         line = " " * (size-key)
#         for j in range(key):
#             if random.random() > k:
#                 line = line + random.choice(toys)
#             else:
#                 line = line + ":green_square:"
#         print(emoji.emojize(line))
#     key = key + 1
# print(" "* (size-1)+emoji.emojize(":brown_square:"))



