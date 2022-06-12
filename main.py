import turtle as t
import pandas as data

screen = t.Screen()
test_guessed_state = []
guessed_state = []

#Setting the background of Turtle to the Specific Image
bg_image = "blank_states_img.gif"
t.addshape(bg_image)
t.shape(bg_image)

#Looping Until User Guesses all State.
while(len(guessed_state)<50):
    answer = screen.textinput(title=f"{len(guessed_state)}/50 Guess the State?",prompt="Type Exit to Exit.Guess the State :")
    answer_text = answer.capitalize()

#fetching data from csv using Pandas:
    data_file = data.read_csv("50_states.csv")
    all_states = data_file.state.tolist()
    state_details = data_file[data_file["state"] == answer_text]

#If user wants to end the Game use: Exit
# Reading all Missing States and Creating a CSV file on States to learn. 
    if (answer_text == "Exit"):
        missing_states = []
        for states in all_states:
            if states not in guessed_state:
                missing_states.append(states)
        missing_states_data = data.DataFrame(missing_states)
        missing_states_data.to_csv("states_to_learn.csv")
        break

#Checking if User Input is Correct and adding them to a list
    if answer_text in all_states:
        test_guessed_state.append(answer_text)
        for i in test_guessed_state:
            if i not in guessed_state:
                guessed_state.append(answer_text)

#Turtle function which helps in displaying the Correctly Typed Names at the Correct Co ordinates.
        tim = t.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.goto(int(state_details.x), int(state_details.y))
        tim.write(answer_text)
