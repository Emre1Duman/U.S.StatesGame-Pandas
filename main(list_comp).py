import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(740, 510)
image = "blank_states_img.gif" #Importing external image

screen.addshape(image) #using that image as our screen background
turtle.shape(image)

#get the  x & y values via mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

guessed_states = []

while  len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    data = pandas.read_csv("50_states.csv")
    states_list = data["state"].to_list()

    if answer_state == "Exit":
        #Check the users guessed states and append the states not guessed into missing states using list comprehension
        missing_states = [state for state in states_list if state not in guessed_states] 
        missing_states_file = pandas.DataFrame(missing_states)
        missing_states_file.to_csv("states_to_learn.csv") #Export the list into a csv file
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state] #Find the data for the state guessed
        t.goto(int(state_data.x), int(state_data.y)) #plot using the coordinates in state data
        t.write(answer_state)




