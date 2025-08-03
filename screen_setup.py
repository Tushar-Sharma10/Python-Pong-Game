from turtle import Turtle,Screen

def show_start_screen():
    start_screen = Turtle()
    start_screen.hideturtle()
    start_screen.color("white")
    start_screen.penup()

    start_screen.goto(0, 50)
    start_screen.write('''Welcome to Pong Game\n
Player (Right Paddle): Use Up and Down Arrow Keys\n
Left Paddle: AI Controlled\n
First to 5 points wins!\n
''', align="center", font=("Courier", 25, "normal"))

    start_screen.goto(0, -100)
    start_screen.write('''
 ██▓███   ▒█████   ███▄    █   ▄████      ▄████  ▄▄▄       ███▄ ▄███▓▓█████ 
▓██░  ██▒▒██▒  ██▒ ██ ▀█   █  ██▒ ▀█▒    ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ 
▓██░ ██▓▒▒██░  ██▒▓██  ▀█ ██▒▒██░▄▄▄░   ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   
▒██▄█▓▒ ▒▒██   ██░▓██▒  ▐▌██▒░▓█  ██▓   ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ 
▒██▒ ░  ░░ ████▓▒░▒██░   ▓██░░▒▓███▀▒   ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒
▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ░▒   ▒     ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░
░▒ ░       ░ ▒ ▒░ ░ ░░   ░ ▒░  ░   ░      ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░
░░       ░ ░ ░ ▒     ░   ░ ░ ░ ░   ░    ░ ░   ░   ░   ▒   ░      ░      ░   
             ░ ░           ░       ░          ░       ░  ░       ░      ░  ░
''', align="center", font=("Courier", 12, "normal"))

    start_screen.goto(0, -200)
    start_screen.write("Press SPACE to Start", align="center", font=("Courier", 25, "normal"))

    return start_screen

def show_end_screen(scoreboard):
    screen = Screen()
    end_screen = Turtle()
    end_screen.hideturtle()
    end_screen.color("white")
    end_screen.penup()

    screen.clear()
    screen.bgcolor("black")

    # Decide the winner
    if scoreboard.r_score >= 5:
        winner = "You Win! 🎉"
    elif scoreboard.l_score >= 5:
        winner = "AI Wins! 🤖"
    else:
        winner = "Game Over"

    # Show winner text
    end_screen.goto(0, 0)
    end_screen.write(winner, align="center", font=("Courier", 40, "bold"))

    end_screen.goto(0, -100)
    end_screen.write("Thanks for playing!\nClick anywhere to exit.", align="center", font=("Courier", 20, "normal"))


