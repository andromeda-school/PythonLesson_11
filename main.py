from tkinter import *

bg_purple = "#D48CEE"
bg_white = "#F5E5FB"
block_size = 50
WIDTH = block_size * 8
HEIGHT = block_size * 8

window = Tk()
window.title("Первое приложение")
window.geometry(str(WIDTH)+"x"+str(HEIGHT)) # 500x500
window.config(bg=bg_purple)

canvas = Canvas(
    window,
    width=WIDTH,
    height=HEIGHT,
    bg=bg_white
)
canvas.pack()

number = 1

# canvas.create_text(
#     WIDTH/2,
#     HEIGHT/2,
#     fill="black",
#     font="Calibri 18",
#     text=str(number)
# )
for i in range(20):
    if number>10:
        canvas.create_text(
            (block_size / 2) * 9 + 10.0,
            (HEIGHT / 2) + (25.0 * ((i%10)+1)),
            fill="black",
            font="Calibri 18",
            text=str(number)
        )
    else:
        canvas.create_text(
            (block_size / 2) * i + 10.0,
            HEIGHT / 2,
            fill="black",
            font="Calibri 18",
            text=str(number)
        )
    number = number + 1


# white_turn = True
# for i in range(8):
#     for j in range(8):
#         pos_x = block_size * j
#         pos_y = block_size * i
#         if white_turn:
#             canvas.create_rectangle(
#                 pos_x, pos_y,
#                 pos_x + block_size, pos_y + block_size,
#                 fill="white")
#         else:
#             canvas.create_rectangle(
#                 pos_x, pos_y,
#                 pos_x + block_size, pos_y + block_size,
#                 fill="black")
#         white_turn = not white_turn
#     white_turn = not white_turn

window.mainloop()
