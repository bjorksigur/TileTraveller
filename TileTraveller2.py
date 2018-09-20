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

while location != 3.1:
    if location == 1.1:
        new_location=north(location)
    if location == 2.1:
        new_location=north(location)
    if location == 3.1:
        new_location=norht(location)
    
