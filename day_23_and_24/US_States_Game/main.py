import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

score = 0
total_guesses = 0


def get_user_input():
    return screen.textinput(f"{score}/50 States Correct", "What's another state name?")


def print_state(state_name, color="black"):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == state_name]
    t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
    t.color(color)
    t.write(state_name)


def print_and_save_missing_states():
    missing_states = [state for state in all_states if state not in guessed_states]
    for state in missing_states:
        print_state(state, "red")
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv", header=["states"], index=False)


def print_final_score():
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(-100, 280)
    t.write(f"{score}/50 States Correct. Total Guesses: {total_guesses}")


# main loop
while len(guessed_states) < len(all_states):
    user_input = get_user_input()
    if user_input in all_states:
        if user_input in guessed_states:
            total_guesses += 1
            continue
        guessed_states.append(user_input)
        print_state(user_input)
        score += 1
        total_guesses += 1
    elif user_input.lower() == "exit":
        print_final_score()
        print_and_save_missing_states()
        break
    else:
        total_guesses += 1

if len(guessed_states) == len(all_states):
    print_final_score()

screen.exitonclick()
