location = 1.1

def north(location):
    print("You can travel: (N)orth.") 
    direction=(input("Direction: ")) 
    while direction.lower() != "n":
        print("Not a valid direction!") 
        direction=(input("Direction: "))
    if direction.lower() == "n":
        location = round(location+0.1 ,2) 
    return(location)

def north_east_south(location):
    print("You can travel: (N)orth or (E)ast or (S)outh.")    
    direction=(input("Direction: "))
    while direction.lower() != "n" and direction.lower() != "e" and direction.lower() != "s":
        print("Not a valid direction!") 
        direction=(input("Direction: ")) 
    if direction.lower() == "n":
        location = round(location + 0.1, 2) 
    if direction.lower() == "e":
        location = round(location + 1, 2) 
    if direction.lower() == "s":
        location = round(location - 0.1, 2)
    return(location)

def south_west(location):
    print("You can travel: (S)outh or (W)est.") 
    direction=(input("Direction: "))
    while direction.lower() != "w" and direction.lower() != "s":  
        print("Not a valid direction!")
        direction=(input("Direction: ")) 
    if direction.lower() == "w":
        location = round(location - 1, 2) 
    if direction.lower() == "s":
        location = round(location - 0.1, 2) 
    return(location)

def east_south(location):
    print("You can travel: (E)ast or (S)outh.") 
    direction=(input("Direction: ")) 
    while direction.lower() != "e" and direction.lower != "s":
        print("Not a valid direction!") 
        direction=(input("Direction: "))
    if direction.lower() == "e":
        location = round(location + 1 ,2) 
    if direction.lower() == "s":
        location = round(location - 0.1 ,2) 
    return(location)

def east_west(location):
    print("You can travel: (E)ast or (W)est.")
    direction=(input("Direction: ")) 
    while direction.lower() != "e" and direction.lower() != "w":
        print("Not a valid direction!") 
        direction=(input("Direction: "))
    if direction.lower() == "e":
        location = round(location + 1 ,2) 
    if direction.lower() == "w":
        location = round(location - 1 ,2) 
    return(location)

def north_south(location):
    print("You can travel: (N)orth or (S)outh.")
    direction=(input("Direction: ")) 
    while direction.lower() != "n" and direction.lower() != "s":
        print("Not a valid direction!")
        direction=(input("Direction: ")) 
    if direction.lower() == "n":
        location = round(location + 0.1, 2)
    if direction.lower() == "s":
        location = round(location - 0.1, 2) 
    return(location)




while location != 3.1:
    if location == 1.1:
        new_location=north(location)
    if location == 2.1:
        new_location=north(location)
    if location == 1.2:
        new_location=north_east_south(location)
    if location == 2.2:
        new_location=south_west(location)
    if location == 3.3:
        new_location=south_west(location)
    if location == 1.3:
        new_location=east_south(location)
    if location == 2.3:
        new_location=east_west(location)
    if location == 3.2: 
        new_location=north_south(location)

    


        

    
    
