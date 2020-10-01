known_users = ["Shrek", "Donkey", "Fiona", "Patrick", "Bob", "Joe"]
print("hi my name is travis")
name=input("what is your name?")
name=name.strip().capitalize()
if name in known_users:
    print("hello {}".format(name))
    stay=input("Would you like to stay in the list- Yes/No: ")
    stay=stay.strip().capitalize()
    if stay=="No":
        known_users.remove(name)
        print(known_users)
else:
    print("hello {}".format(name))
    enter=input("Would you like to get added in the list- Yes/No: ")
    enter=enter.strip().capitalize()
    if enter=="Yes":
        known_users.append(name)
        print(known_users)