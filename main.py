import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_names = data["state"].to_list()
guesses_states = []
#print(state_names)


while len(guesses_states) < 50:
    answer_state = screen.textinput(title=f"{len(guesses_states)}/50 States Correct",
                                    prompt="What's another state name?").title()
    #print(answer_state)
    if answer_state == "Exit":
        states_to_learn = [state for state in state_names if state not in guesses_states]
        df = pandas.DataFrame(states_to_learn)
        df.to_csv('states_to_learn.csv')
        break
    if answer_state in state_names:
        guesses_states.append(answer_state)
        t = turtle.Turtle()
        state_row = data[data["state"] == answer_state]
        x_cor = state_row["x"].iloc[0]
        y_cor = state_row["y"].iloc[0]
        t.hideturtle()
        t.penup()
        t.goto(x=x_cor, y=y_cor)
        t.write(arg=answer_state)


print(states_to_learn)