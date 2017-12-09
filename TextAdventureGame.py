import time, random, sys

def printNicely(x):
    for word in x.split():
        sys.stdout.write(word + ' ')
        sys.stdout.flush()
        if word.__contains__('.'):
            time.sleep(0.75)
        elif word.__contains__(','):
            time.sleep(0.25)
        time.sleep(0.25)
    sys.stdout.write('\n')

def get_inventory():
    print("Items in inventory are:\n")
    for items in inventory:
        print(items)


def barn():
    printNicely("You walk into the barn and you enter with the noise of all the animals")
    choice = int(input("Which animals would you like to go to first?\n1. Horses\n2. Cows\n3. Pigs\n4. Chickens"))
    if choice == 1:
        printNicely("You walk to the horses and feed them. They are very excited to see you. You start petting them and they really seem to like it.")
        printNicely("You then proceed to feed the chickens and making sure you collect the eggs. ")
        printNicely("Then after feeding the chickens you go to the cows and feed them and make sure that you milk them")
        printNicely("After milking the cows you head to the pigs and feed them while they squeal around waiting for their food.")
        inventory.append("Milk")
        inventory.append("Chicken Eggs")
    if choice == 2:
        printNicely("You head to the cows and give them their food. While they are eating you start to milk some of them so you can store it in your fridge.")
        printNicely("You head then head to the horses and feed them. While they are eating you start petting them and they really seem to like it. One of them nudges for a ride but you are sadly very busy")
        printNicely("After the horses you then head to the chickens and give them their food and while they are eating you quietly sneak over and collect their eggs")
        printNicely("After feeding the chicken you then head over to the pigs where you give them their food. They make loud squeamish noises as you start giving them their food.")
        inventory.append("Milk")
        inventory.append("Chicken Eggs")
    if choice == 3:
        printNicely("You head over to the pigs where you give them their food. While approaching the pen they start squealing very loudly, hungry to receive their food. ")
        printNicely("After feeding the pigs you head over to the cows and give them their food. While they are eating you start to milk some of them so you can store it in your fridge.")
        printNicely("After the cows you head over to the horses and feed them. While they are eating you start petting them and they really seem to enjoy it. One of them nudges you for a ride but you are sadly very busy.")
        printNicely("After the horses you then head to the chicken coop and give them their food and while they are eating you quietly sneak over and collect their eggs.")
        inventory.append("Milk")
        inventory.append("Chicken Eggs")
    if choice == 4:
        printNicely("You head over to the chicken coop and give them their food and while they are eating you quietly sneak over and collect their eggs.")
        printNicely("After the chicken coop you head over to the horses and feed them. While they are eating you start petting them and they really seem to enjoy it. One of them nudges you for a ride but you are sadly very busy.")
        printNicely("After the horses you head over to the cows and give them their good. While they are eating you start to milk some of them so you can store it in your fridge.")
        printNicely("After the cows you head over to the pigs where you give them their food. They make loud squeamish noises as you start giving them their food.")
        inventory.append("Milk")
        inventory.append("Chicken Eggs")
    printNicely("You head back outside and think about where to go next.")
    return int(input("Where do you want to go?\n1. Barn\n2. Lake\n3. Go for a run\n"))

def lake():
    printNicely("You walk over to the lake and look at the fish trap that you set.")
    printNicely("You peer into it and it happens to be a big tuna")
    choice = int(input("Do you (1) let it go or (2) kill it and take it home with you took cook."))
    if choice == 1:
        printNicely("You let the fish go and it swims back into the lake. ")
    if choice == 2:
        printNicely("You take the slimy tuna out of the trap and it starts squirming around. You reach into your bag and take our your cutting knife.")
        printNicely("You pierce the fish, killing it and put it in your bad")
        inventory.append("Big Tuna")
    printNicely("You decide to reset the trap again so you can catch another fish when you realize something strange in the water. It looks like something that you have not seen before.")
    choice_check = int(input("Do you check it out (1) or just leave it be (2)?"))
    if choice_check == 1:
        printNicely("You leave your backpack on the ground and start swimming to the strange thing.")
        printNicely("You then realize that the weird thing is a megalodon and it bites you and you die a very painful death. -_- *Guess they still do exist ")
        printNicely("GAME OVER!")
        gameLoop = False
        return -1
    if choice_check == 2:
        printNicely("You decide that its not worth time to check it out and you walk away and head back to your house.")
    return int(input("Where do you want to go?\n1. Barn\n2. Lake\n3. Go for a run\n"))


def run():
    printNicely("You start to go running down the trail near your farm.")
    crossroads_choice = int(input("After some time you appear at a crossroads. You can either go\n1. Left\n2. Right "))
    if crossroads_choice == 1 or crossroads_choice == 2:
        if crossroads_choice == 1:
            printNicely("You take the left path and start running again")
        elif crossroads_choice == 2:
            printNicely("You take the right path and start running again")
    printNicely("While running you stumble on a cave. What do you do?")
    cave_choice = int(input("1. Go inside the cave and investigate\n2. Decide to ignore the cave and continue on your run\n"))
    if cave_choice == 1:
        printNicely("You decide to enter the cave")
        cave()
    if cave_choice == 2:
        printNicely("You decide to ignore the cave and continue on your run but as you walk away from the cave you get attacked by a bear.")
        printNicely("Out of fear you run into the cave, where the bear can not get you since the hole for the cave is to small.\n")
        cave()
        #bear_choice = int(input("Do you 1. Decide to fight the bear with your cutting knife.\n2. Run and shelter in the cave since the hole for the cave is too small for the bear to enter in. "))
        #if bear_choice == 1:
         #   printNicely("You pull out your knife and decide to fight the bear but the bear weighs like 3 times your weight and overpowers you. ")
        #    printNicely("The bear than begins to claw your face off and you die...(not the best idea)")
         #   passTime(5)
         #   printNicely("GAME OVER!")
          #  return(bear_choice)

def cave():
    printNicely("You enter the dark cave and you can barely see.")
    printNicely("You feel your hands around looking for a light source or something to use to make some light")
    printNicely("You find a flint and stone and are able to create a light source\n")
    printNicely("You stumble upon an unusual egg.")
    printNicely("You pick up the egg and it feels warm... very warm")
    printNicely("You decide to keep the egg and put it in your backpack")
    printNicely("All of a sudden your fire goes out and you hear a loud monstrous noise")
    printNicely("Forgetting to pack an extra pair of underpants you run away to the entrance of the cave and never look back.")
    printNicely("You end up running all the way back to your house and you hear the egg start to crack open.\n")
    printNicely("You take the egg out of you bag\n")
    printNicely("You hear the heartbeat")
    printNicely("You hear it again")
    printNicely("The egg cracks open and the animals high pitched sound rings through your ears as the tiny claws try to rip apart the egg.")
    return -1

def drinking():
    if drink != 4:
        if drink == 1:
            printNicely("You get the nice cold water and chug it down. You then put the bottle back into the fridge.")
            printNicely("After drinking the water you then grab your backpack and go outside")
        if drink == 2:
            printNicely( "You drink the juice and you end up liking it so much that you finish the entire bottle and throw it away.")
            printNicely("After drinking the juice you then grab your backpack and go outside")
        if drink == 3:
            printNicely("You drink the milk and start to feel very tired so you rub your eyes and go upstairs to your bed. ")
            printNicely("You wake up the next morning to the birds chirping. Opening your eyes you see the sun peer through the tiny hole cut out into the wall.\n")
            printNicely("Feeling thirsty again you head into your fridge and grab a water bottle and put it in your backpack and go outside ")
            inventory.append("Water Bottle")
        return int(input("Where do you want to go?\n1. Barn\n2. Lake\n3. Go for a run\n"))
    else:
        printNicely("You drink the mystery substance")
        printNicely("and you collapse on the ground and you realize it was bleach and you die(thank god it's over) ")
        printNicely("GAME OVER!")
        gameLoop = False
        return -1

#Local Variables

inventory = ["Small cutting knife"]
allFed = False
fed = 0


#beginning of Program

printNicely("You wake up to the birds chirping. Opening your eyes, you see the sun peer through the tiny hole cut out into the wall.\n")
printNicely("You feel thirsty and walk down to the kitchen")
printNicely("You look in the fridge, thinking what you want to drink.")

drink = int(input("1. Water\n2. Juice\n3. Milk\n4. Bottle without a label\n"))
gameLoop = True
drank = False
while gameLoop:
    if not drank:
        choice_area = drinking()
        if choice_area == -1:
            break
        drank = True
    elif choice_area == 1:
        choice_area = barn()
    elif choice_area == 2:
        choice_area = lake()
        if choice_area == -1:
            break
    elif choice_area == 3:
        run()
        printNicely("The end.")
        printNicely("Part Two Coming Summer 2018")
        gameLoop = False


