import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = ("2021-08-07_05-30-47-49d4697646f3d0d9612226538bcfc120.gif")
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("states_India.csv")
all_states = data.state.to_list()
guessed_states =[]
while len(guessed_states) < 36:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct" , prompt = "What's another state's name?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states =[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        x = float(data[data.state == answer_state].x.iloc[0])
        y = float(data[data.state == answer_state].y.iloc[0])
        t.goto(x,y)
        t.write(answer_state)
        guessed_states.append(answer_state)
screen.exitonclick()
