# from playsound import playsound
# # playsound("eat.wav")
# playsound("C:/Users/RBcomputers/Desktop/eat.wav")  # full path example

from playsound import playsound

# sound_path = os.path.join(os.environ["USERPROFILE"], "Desktop", "eat.wav")
# playsound(sound_path)

from tkinter import *

import random


GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 10
BODY_PARTS = 8
SNAKE_COLOR = "Blue"
FOOD_COLOR = "White"
FOOD_SIZE = 20    
BACKGROUND_COLOR = "Black"

# class Snake:
#     def __init__(self):
#         self.body_size = BODY_PARTS
#         self.coordinates = []
#         self.squares = []

#         for i in range(0, BODY_PARTS):
#             self.coordinates.append([0, 0])

#         for x, y in self.coordinates:
#             square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="Snake")
#             self.squares.append(square)
# 
class Snake:
    def __init__(self):
        self.coordinates = []
        self.squares = []

        for _ in range(BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="Snake")
            self.squares.append(square)

    def grow(self):
        self.coordinates.append(self.coordinates[-1])
        x, y = self.coordinates[-1]
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="Snake")
        self.squares.append(square)
    


class Food:

    def __init__(self):

        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) -1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) -1) * SPACE_SIZE

        self.coordinates = [x, y]

        # canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="FOOD")
        canvas.create_oval(x, y, x + FOOD_SIZE, y + FOOD_SIZE, fill=FOOD_COLOR, tag="FOOD")



# # When snake eats food, call this
# def play_eat_sound():
#     try:
#         # Best practice
#         # playsound(r"C:\Users\RBcomputers\Desktop\eat.wav")

#         playsound("eat.wav")
#     except Exception as e:
#         print("Sound error:", e)


import threading
from playsound import playsound

def play_eat_sound():
    def _play():
        try:
            playsound("C:/Users/RBcomputers/Desktop/eat.wav")
        except Exception as e:
            print("Sound error:", e)
    threading.Thread(target=_play, daemon=True).start()


   



def next_turn(snake, food):
    global score

    x, y = snake.coordinates[0]
    ...


    if direction == "up": 
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, [x, y])

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR) 
    snake.squares.insert(0, square) 

    # if x == food.coordinates[0] and y == food.coordinates[1]:
    #     playsound("eat.wav")  # 🔊 play sound when food eaten
    #     score += 1
    #     score_label.config(text="Score:{}".format(score))
    #     canvas.delete("FOOD")
    #     food = Food()

    #     snake.grow()    


    #     # Label.config(text="score:{}".format(score))
    #     score_label.config(text="Score:{}".format(score))

    #     canvas.delete("FOOD")

    #     food = Food()

    # def grow(self):
    #     self.coordinates.append(self.coordinates[-1])
    #     x, y = self.coordinates[-1]
    #     square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="Snake")
    #     self.squares.append(square)


    if x == food.coordinates[0] and y == food.coordinates[1]:
        play_eat_sound()
        score += 1
        score_label.config(text="Score:{}".format(score))
        snake.grow()
        canvas.delete("FOOD")
        food = Food()


    else:
    
        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]  

        

    if check_collisions(snake):
        game_over()

    else:   
        Window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction
    


def check_collisions(snake):

    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        
        return True
    if y < 0 or y >= GAME_HEIGHT:
        print("GAME OVER")
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME OVER")
            return True
    return False  
 
def restart_game():
    global snake, food, score, direction

    canvas.delete(ALL)
    score = 0
    direction = 'down'
    score_label.config(text="Score:0")
    
    snake = Snake()
    food = Food()
    next_turn(snake, food)
 

    
def game_over():
    canvas.delete(ALL)
    canvas.create_text(GAME_WIDTH/2, GAME_HEIGHT/2,
                       font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")
    
    restart_btn = Button(Window, text="Restart", font=('consolas', 20), command=restart_game)
    restart_btn.pack(pady=10)


    # canvas.create_text(canvas.wait_winfo_width()/2, canvas.winfi_height()/2,
    #                     font=('consolas',70),  text="GAME OVER", fill="red", tag="gameover")

Window = Tk()
Window.title("Snake game")
Window.resizable(False, False)

score = 0
direction = 'down'

score_label = Label(Window, text="Score:{}".format(score), font=('consolas', 40))
score_label.pack()


# Label = Label(Window, text="Score:{}".format(score), font=('consolas', 40))
# Label.pack()

canvas = Canvas(Window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()  

Window.update()

Window_width = Window.winfo_width()
Window_height = Window.winfo_height()
screen_width = Window.winfo_screenwidth()
screen_height = Window.winfo_screenheight()

x = int((screen_width/2) - (Window_width/2))
y = int((screen_height/2) - (Window_height/2))

Window.geometry(f"{Window_width}x{Window_height}+{x}+{y}")

Window.bind('<Left>',lambda event: change_direction('left'))
Window.bind('<Right>',lambda event: change_direction('right'))
Window.bind('<Up>',lambda event: change_direction('up'))
Window.bind('<Down>',lambda event: change_direction('down'))

# self.coordinates = [x, y]
 
# Window.geometry(f"{Window_width}x{Window_height}+{x}+{y}")

snake = Snake()
food = Food()

# Window.bind("<KeyPress>", )



next_turn(snake, food)
# play_eat_sound()


Window.mainloop()

