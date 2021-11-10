import turtle
import pandas as pd

# creates a data frame from a csv file
data = pd.read_csv("50_states.csv")

# instantiated turtle object
t = turtle.Turtle()

# Creating a screen
screen = turtle.Screen()
screen.title("U.S States Game")

# initializing img to blank_states file path
img = 'blank_states_img.gif'

screen.addshape(img)
turtle.shape(img)

guessed_state = []
missing_states = []
all_states = data.state.to_list()

while len(guessed_state) < 50:

    total_correct_guesses = len(guessed_state)

    answer_state = screen.textinput(f'{total_correct_guesses}/50 States Correct',
                                    prompt="What's another state's name?").title()

    state_is_correct = answer_state in data['state'].values

    # checks to see if user input is one of the 50 states & has not been previously guessed.
    if state_is_correct and not guessed_state.__contains__(answer_state):
        state_data = data[data.state == answer_state]
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_state.append(answer_state)
    elif answer_state == "Exit":
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        missing_states_data_frame = pd.DataFrame(missing_states)
        missing_states_data_frame.to_csv("states_to_learn.csv")
        break



