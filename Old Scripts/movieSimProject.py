# Movie simulator
# Choose from a range of movies
# Each movie contains a range of allowed ages to view the film based off a user prompt determine if the user can view the film

films = {
    "Terminator" : [17,10],
    "Ice Age": [5,4],
    "Black Panther": [13, 2]
}

while True:
 
    for i in films:
        print (i)

    prompt = input("Select the name for the movie: ").strip().title()
    if prompt in films:
        age = int(input("How old are you? ").strip())
        if age >= films[prompt][0]:
            if  films[prompt][1] > 0:
                print("Enjoy the show!")
                films[prompt][1] -= 1
                print("The {0} showing has {1} tickets remaining".format(prompt, films[prompt][1]))
            else:
                print("Show is sold out")
        else:
            print("You are under age, no film for you!")
    else:
        print ("This film doesn't exist, try another please!")
