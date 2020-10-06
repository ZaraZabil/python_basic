film = {"Shrek": {"age": 3, "seats": 6},
       "Mission Impossible 2": {"age": 5, "seats": 3},
       "Endgame": {"age": 7, "seats": 5},
       "Infinity War": {"age": 9, "seats": 5}}
choice = input(
   "Which film would you like to watch? "
   "\n Shrek \n Mission Impossible 2 \n "
   "Endgame \n Infinity War "
   "\n Press enter to exit : ").strip().title()
if choice in film:
    if film[choice]["seats"]==0:
        print("seats are not availble")
    else:
        your_age=int(input("enter your age "))
        if your_age<=film[choice]["age"]:
            print("you are too young to watch the movie")
        else:
            no_seats=film[choice]["seats"]
            enter_seats=int(input("enter num of seats "))
            if no_seats< enter_seats:
                print("enter as per availability")
            else:
                print("enjoy the movie!!")

else:
    print("movie is not in the list")
