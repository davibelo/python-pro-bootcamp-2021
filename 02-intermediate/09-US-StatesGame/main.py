import turtle
import pandas as pd

# creating screen with US map
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "02-intermediate/09-US-StatesGame/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("02-intermediate/09-US-StatesGame/50_states.csv")
all_states = df.state.to_list()
guessed_states = []
score = 0

while len(guessed_states) < 50:
    # prompt for a state and .title method to correct case
    answer_state = screen.textinput(
        title=f"Score {score}/50",
        prompt="What's another state?").title()

    # exit command generates a list of missed states
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        df_missing_states = pd.DataFrame(missing_states)
        df_missing_states.to_csv(
            "02-intermediate/09-US-StatesGame/missing_states.csv")
        break

    # checks if the state exists
    if answer_state in all_states:
        # checks if state was already guessed
        if answer_state not in guessed_states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = df[df.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(state_data.state.item())
            guessed_states.append(answer_state)
            score += 1

turtle.mainloop()
