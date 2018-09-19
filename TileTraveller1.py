#Svo lengi sem location er ekki í 3.1 þá keyrir while lykkja af stað.
#Breytan location byrjar í 1.1
#Undir while lykkjunni skilgreinir forritið hvaða input eru valid.
#Geymir núverandi staðsetninug í location
#Tekur við input og reiknar út næstu staðsetingu og geymir í location. 
#Prentar út hvaða input eru í boði.
#Tekur við input og reiknar svo næstu staðsetningu og geymir í location. 
#Ef user slær inn input sem er ekki í boði þá pretnar kóðinn "Not valid input" og biður um nýtt. 
#Heldur áfram þangað til að location er orðið 3.1
#Ef location í 3.1 þá prentast út "Victory!" og hættir. 


location = 1.1

while location  != 3.1:
    if location == 1.1:
        print("You can travel: (N)orth.") 
        direction=(input("Direction: ")) 
        while direction.lower() != "n":
            print("Not a valid direction!") 
            direction=(input("Direction: ")) 
        if direction.lower() == "n":
            location = round(location+0.1 ,2)   
    if location == 1.2:
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
    if location == 1.3:
        print("You can travel: (E)ast or (S)outh.") 
        direction=(input("Direction: ")) 
        while direction.lower() != "e" and direction.lower != "s":
            print("Not a valid direction!") 
            direction=(input("Direction: "))
        if direction.lower() == "e":
            location = round(location + 1 ,2) 
        if direction.lower() == "s":
            location = round(location - 0.1 ,2) 
    if location == 2.2:
        print("You can travel: (S)outh or (W)est.") 
        direction=(input("Direction: "))
        while direction.lower() != "w" and direction.lower() != "s":  
            print("Not a valid direction!")
            direction=(input("Direction: ")) 
        if direction.lower() == "w":
            location = round(location - 1, 2) 
        if direction.lower() == "s":
            location = round(location - 0.1, 2) 
    if location == 2.1:
        print("You can travel: (N)orth.") 
        direction=(input("Direction: ")) 
        while direction.lower() != "n":
            print("Not a valid direction!") 
            direction=(input("Direction: "))
        if direction.lower() == "n":
            location = round(location + 0.1, 2)  
    if location == 2.3: 
        print("You can travel: (E)ast or (W)est.")
        direction=(input("Direction: ")) 
        while direction.lower() != "e" and direction.lower() != "w":
            print("Not a valid direction!") 
            direction=(input("Direction: "))
        if direction.lower() == "e":
            location = round(location + 1 ,2) 
        if direction.lower() == "w":
            location = round(location - 1 ,2) 
    if location == 3.3:
        print("You can travel: (S)outh or (W)est.")
        direction=(input("Direction: ")) 
        while direction.lower() != "w" and direction.lower() != "s":
            print("Not a valid direction!")
            direction=(input("Direction: ")) 
        if direction.lower() == "w":
            location = round(location - 1, 2) 
        if direction.lower() == "s":
            location = round(location - 0.1, 2) 
    if location == 3.2:
        print("You can travel: (N)orth or (S)outh.")
        direction=(input("Direction: ")) 
        while direction.lower() != "n" and direction.lower() != "s":
            print("Not a valid direction!")
            direction=(input("Direction: ")) 
        if direction.lower() == "n":
            location = round(location + 0.1, 2)
        if direction.lower() == "s":
            location = round(location - 0.1, 2) 
else:
    print("Victory!") 
            