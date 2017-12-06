import time



def get_inventory(inventory):
    print("Items in inventory are:\n")
    for items in inventory:
        print(items)

def barn():
    print("You walk into the barn and you enter with the noise of all the animals")
    choice = int(input("Which animals would you like to go to first?\n1. Horses\n2. Cows\n3. Pigs\n4. Chickens"))
    if choice == 1:
        print("You walk to the horses and feed them. They are very excited to see you. You start petting them and they really seem to like it.")
        print("You then proceed to feed the chickens and making sure you collect the eggs. ")
        print("Then after feeding the chickens you go to the cows and feed them and make sure that you milk them")
        print("After milking the cows you head to the pigs and feed them while they squeal around waiting for their food.")
        inventory.append("Milk")
        inventory.append("Chicken Eggs")
    if choice == 2:
        print("You head to the cows and give them their food. While they are eating you start to milk some of them so you can store it in your fridge.")
        print("You head then head to the horses and feed them. While they are eating you start petting them and they really seem to like it. One of them nudges for a ride but you are sadly very busy")
        print("After the horses you then head to the chickens and give them their food and while they are eating you quietly sneak over and collect their eggs")
        print("After feeding the chicken you then head over to the pigs where you give them their food. They make loud squeamish noises as you start giving them their food.")
        inventory.append("Milk")
        inventory.append("Chicken Eggs")
    if choice == 3:
        print("You head over to the pigs where you give them their food. While approaching the pen they start squealing very loudly, hungry to receive their food. ")
        print("After feeding the pigs you head over to the cows and give them their food. While they are eating you start to milk some of them so you can store it in your fridge.")
        print("After the cows you head over to the horses and feed them. While they are eating you start petting them and they really seem to enjoy it. One of them nudges you for a ride but you are sadly very busy.")
        print("After the horses you then head to the chicken coop and give them their food and while they are eating you quietly sneak over and collect their eggs.")
        inventory.append("Milk")
        inventory.append("Chicken Eggs")
    if choice == 4:
        print("You head over to the chicken coop and give them their food and while they are eating you quietly sneak over and collect their eggs.")
        print("After the chicken coop you head over to the horses and feed them. While they are eating you start petting them and they really seem to enjoy it. One of them nudges you for a ride but you are sadly very busy.")
        print("After the horses you head over to the cows and give them their good. While they are eating you start to milk some of them so you can store it in your fridge.")
        print("After the cows you head over to the pigs where you give them their food. They make loud squeamish noises as you start giving them their food.")
        inventory.append("Milk")
        inventory.append("Chicken Eggs")
    print("You head back outside and think about where to go next.")

def lake():
    print("You walk over to the lake and look at the fish trap that you set.")
    print("You peer into it and it happens to be a big tuna")
    choice = int(input("Do you let it go (1) or do you kill it and take it home with you took cook (2)."))
    if choice == 1:
        print("You let the fish go and it swims back into the lake. ")
    if choice == 2:
        print("You take the slimy tuna out of the trap and it starts squirming around. You reach into your bag and take our your cutting knife.")
        print("You pierce the fish, killing it and put it in your bad")
        inventory.append("Big Tuna")
    print("You decide to reset the trap again so you can catch another fish when you realize something strange in the water. It looks like something that you have not seen before.")


#Local Variables

gameLoop = True
inventory = ["Small cutting knife"]
allFed = False
fed = 0


#beginning of Program

print("You wake up to the birds chirping. Opening your eyes you see the sun peer through the tiny hole cut out into the wall.\n")
time.sleep(2)
print("You feel thirsty and walk down to the kitchen")
print("...")
time.sleep(3)
print("You look in the fridge thinking what you want to drink.")

drink = int(input("1. Water\n2. Juice\n3. Milk\n4. Bottle without a label\n"))
gameLoop = True
while(gameLoop == True):
    if drink != 4:
        if drink == 1:
            print("You get the nice cold water and chug it down. You then put the bottle back into the fridge.")
            print("After drinking the water you then grab your backpack and go outside")
        if drink == 2:
            print( "You drink the juice and you end up liking it so much that you finish the entire bottle and throw it away.")
            print("After drinking the juice you then grab your backpack and go outside")
        if drink == 3:
            print("You drink the milk and start to feel very tired so you rub your eyes and go upstairs to your bed. ")
            time.sleep(5)
            print("You wake up to the birds chirping. Opening your eyes you see the sun peer through the tiny hole cut out into the wall.\n")
            print("Feeling thirsty again you head into your fridge and grab a water bottle and put it in your backpack and go outside ")
            inventory.append("Water Bottle")
        choice_area = int(input("Where do you want to go?\n1. Barn\n2. Lake\n3. Go for a run\n4. Visit the village"))
        if choice_area == 1:
            barn()
        if choice_area == 2:
            lake()
            choice_check = int(input("Do you check it out (1) or just leave it be (2)?"))
            if choice_check == 1:
                print("You leave your backpack on the ground and start swimming to the strange thing.")
                time.sleep(7)
                print("You then realize that the weird thing is a megalodon and it bites you and you die a very painful death. -_- *Guess they still do exist ")
                time.sleep(1)
                print("GAME OVER!")
                gameLoop = False
            if choice_check == 2:
                print("You decide that its not worth time to check it out and you walk away and head back to your house.")


    if drink == 4:
        print("You drink the mystery substance")
        time.sleep(5)
        print("and you collapse on the ground and you realize it was bleach and you die(thank god it's over) ")
        time.sleep(3)
        print("GAME OVER!")
        gameLoop = False


