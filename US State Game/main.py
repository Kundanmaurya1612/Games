from turtle import Turtle, Screen
import pandas
screen = Screen()
screen.addshape("country.gif")

tim = Turtle("country.gif")

# ------------------------------------------------------
# note: if it say 'no directory found ' 
# then change the terminal directory to:
# ' cd "US State Game" ' .
# ------------------------------------------------------


data = pandas.read_csv("50_states.csv")

states = data["state"].to_list()
guessed_states = []
states_to_learn = []
score = 0

while len(guessed_states) != len(states):
    user = screen.textinput(title=f"Your Score {score} / 50", prompt="Guess the Country").title() # type: ignore
    if user == "Exit":
        break
    print(user)
    if user in states:
        score += 1
        tom = Turtle()
        tom.color("black")
        tom.penup()
        tom.hideturtle()
        cordinate_of_state = data[data["state"] == user]
       
        tom.goto(cordinate_of_state["x"].item(),cordinate_of_state["y"].item())
        tom.write(user, font=("Arial", 8, "bold"))
        guessed_states.append(user)

for gs in states:
    if gs not in guessed_states:
        states_to_learn.append(gs)
df = pandas.DataFrame(states_to_learn)
df.to_csv("states_to_learn.csv")
    

screen.mainloop()