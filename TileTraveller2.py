# Það var mun auðveldara að vinna þennan kóða en fyrri. Vegna þess að það þurfti bara að setja það sem gert var í fyrri kóðanum inní föll. 
# Þessi kóði er mun læsilegri. Hann er bæði skipulagaðri og styttri. Hinn virðist alltof flókinn þegar horft er á hann. 
# Var ekki að lenda í því að gera klaufavillur í þessum kóða eins og í hinum. 




def north(location):                      #Reitur sem ferðast aðeins norður. 
    print("You can travel: (N)orth.")     
    direction=(input("Direction: ")) 
    while direction.lower() != "n":
        print("Not a valid direction!") 
        direction=(input("Direction: "))
    if direction.lower() == "n":
        location = round(location+0.1 ,2) 
    return(location)

def north_east_south(location):            #Reitur þar sem aðeins er hægt að ferðast norður, austur og suður. 
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


location = 1.1           #first location 

while location != 3.1:
    if location == 1.1:
        location=north(location)
    if location == 2.1:
        location=north(location)
    if location == 1.2:
        location=north_east_south(location)
    if location == 2.2:
        location=south_west(location)
    if location == 3.3:
        location=south_west(location)
    if location == 1.3:
        location=east_south(location)
    if location == 2.3:
        location=east_west(location)
    if location == 3.2: 
        location=north_south(location)
else:
    print("Victory!") 



    


        

    
    
