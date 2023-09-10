import random
from time import sleep
import sys

# Function to roll a pair of 6-sided dice
def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

# Functions to calculate the skill, stamina and luck scores based on dice rolls
def calculate_skill_score(rolls):
    return sum(rolls)


def calculate_stamina_score(rolls):
    return sum(rolls)

def calculate_luck_score(rolls):
    return sum(rolls)

# Initialize global scores
skill_score, stamina_score, luck_score = 0, 0, 0

# Function to play the adventure game STAGE 1
def play_stage_1():
    global skill_score, stamina_score, luck_score
    print("Welcome to Stage 1. The offices of VIPERCALL TECHNOLOGIES - YOUR FIRST DAY\n")
    sleep(3)
    print("You are a keen gamer with decent technology skills and last week you finished working your dead-end job as a fast-food delivery rider.\n")
    sleep(6)
    print("You've recently secured a new job at a start-up company called Vipercall Technologies, which investigates online scams. There's something new on the market - a groundbreaking and eagerly awaited video game called Peril Quest, powered by the first neural network games engine where players can enter breathtakingly realistic realms. And it's within this game that some of the most prolific online scams are currently taking place.\n")
    sleep(14)
    print("The main office of Vipercall Technologies consists of two rows of four desks and a large curved communications screen. The owners have purposely kept everything uncluttered and minimal within the small office. One of the rows of desks has just enough room to house powerful PCs, monitors, and keyboards. A separate demonstration room called Studio X is situated at the far end of the office within which is a stand where four sleek, translucent headbands and haptic skins are placed. You are keen to get to know your new coworkers and make an impression. Your current aim is to find out what goes on in Studio X.\n")
    sleep(1)
    print ("Before embarking on your venture, you must first establish some initial strengths. You have been preparing for this quest for quite some time, by learning technology and gaming skills. Some of which you have become highly knowledgeable in.\n")
    sleep (8)
    print("To progress to each new level you will have to navigate through various scenarios, using your luck and skill scores, and hold a decent stamina score to progress to the next stage.\n")
    sleep(7)
    print("It's time to start your adventure. You will now roll dice to determine your Skill, Stamina, and Luck scores.")
    sleep(6)
    
    input("Press Enter to roll the dice and determine your SKILL score...>")
    
    # Roll a pair of dice to determine player's scores
    dice_rolls = roll_dice()
    
    print(f"You rolled the dice: {dice_rolls}\n")
    
    skill_score = calculate_skill_score(dice_rolls)

    sleep(3)
    print(f"Your SKILL score is {skill_score}!\n")

    input("Press Enter to roll the dice and determine your STAMINA score...")

    dice_rolls = roll_dice()

    print(f"You rolled the dice: {dice_rolls}\n")

    stamina_score = calculate_stamina_score(dice_rolls)

    sleep(3)
    print(f"Your STAMINA score is {stamina_score}!\n")

    #luck
    input("And finally, Press Enter to roll the dice and determine your LUCK score...")

    dice_rolls = roll_dice()

    print(f"You rolled the dice: {dice_rolls}\n")

    luck_score = calculate_luck_score(dice_rolls)

    sleep(3)
    print(f"Your LUCK score is {luck_score}!\n")


    # First options for the player to choose 
    print ("Your sitting at your desk and you look around.\n")
    print("WHAT WILL YOU DO?\n")
    sleep(4)
    
    print("1 - Smile at a collegue dressed in a rock band t-shirt and beanie hat sitting opposite you?")
    sleep(4)
    print("2 - Offer to make the boss a coffee?")
    sleep(3)
    
    # Prompt user for a choice
    choice = input("Choose 1 or 2>")

    if choice == "1":
        print("Checking your luck score...\n")
        sleep(3)
        if luck_score < 7:
            print("The girl looks agitated and shoots you a disapproving stare. 3 STAMINA points deducted.")
            stamina_score -=3 # Subtract 3 from stamina
            print(f"your current STAMINA score is {stamina_score}:\n")
            print ("They say chivalry is dead. Not suprising with you around. You need to sharepen your act in the next level...\n")
            sleep(6)
            play_stage_2()

        else:
            print("The girl runs her fingers through her hair and gives you a shy smile. 5 STAMINA points added.\n")
            sleep(3)
            stamina_score +=5
            print(f"your current STAMINA score is {stamina_score}:\n")
            play_stage_2()
    
    elif choice == "2":
        print("Checking your skill score...")
        sleep(3)
        if skill_score < 7:
            print("You find a coffee machine in the corner of the kitchen. You press a button and flood the surface with brown water. People in the kitchen laugh at you. Your STAMINA points take a collosal hit.")
            sleep(7)
            stamina_score -=5
            print(f"your current STAMINA score is {stamina_score}:\n")
            sleep(2)
            print("There's just no coming back from this...")
            sleep(2)
            sys.exit("Your adventure ends here...")

        else:
            print ("You whip up two amazing cups of coffee like a true barista. You hand one to the boss who is impressed. 3 STAMINA points added.")
            stamina_score +=3
            print(f"your current STAMINA score is {stamina_score}:\n")
            sleep(5)
            play_stage_2()





    
#Stage 2 

def play_stage_2():
    global skill_score, stamina_score, luck_score
        
    print("You have made it through the first morning in your new job. NICE! By the end of the day you need to figure out how to see what goes on in Studio X!")
    sleep(6)
    print ("You've had a nice lunch laid on by the company (Can't beat a free lunch!) as well as an intro explaining what the company does and the experimental work that goes on in Studio X.\n")
    sleep(8)
    print("After gaining access to various systems, you look around the office. Behind you is a senior developer you've been introduced to who has music blaring from their headphones as they tap away on their keyboard.\n")
    sleep(8)
    print("Your swivel chair squeaks and creaks everytime you move slightly. You notice a much more modern, stylish faux-leather chair in the vacant desk next to you.\n")
    sleep(6)
    print("You need to plan your next move. WHAT WILL YOU DO?\n")
    sleep(2)
    print ("1 - As it's pretty quiet, you decide to check some upcoming sporting fixtures online?\n")
    sleep (4)
    print("2 - Try and attract the attention of the senior developer working at his workstation?\n")
    sleep(5)
    print("3 - Replace your old crappy chair with the newer, more stylish chair. It appears to be unused.\n")
        
    choice = input("Choose 1, 2 or 3 >") # Prompt user for a choice
    if choice == "1":
        print("Checking your luck score...")
        sleep(3)
        if luck_score < 8:
            print("A supervisor, a smartly dressed lady with a sour expression strides over to your desk. She explains that you're never going to advance anywhere with that pitiful attitude.\n")
            sleep(6)
            stamina_score -=4 # Subtract 3 from Stamina
            sleep(2)
            print ("You STAMINA score has taken a hit. You've lost 4 STAMINA points.")
            sleep (4)
            print(f"your current STAMINA score is {stamina_score}:\n")
            sleep(4)
            if stamina_score <6: 
                 print(f"your STAMINA is too low to continue.\n")
                 sleep(3)
                 sys.exit("Your adventure ends here")


        else:
            print("You spend a perfectly relaxing 30 minutes browsing the web on company time. RESULT!. 5 STAMINA points added.")
            stamina_score +=5
            print(f"your current STAMINA score is {stamina_score}:")
            sleep (3)
            play_stage_3()
                
    elif choice == "2":
            print("Checking your luck score...\n")
            sleep(3)
            if luck_score <= 7:
                print("You call out his name but he appears to ignore you. Eventhough his music has stopped he ignores you a second time. EMBAARASSING! 3 STAMINA points deducted\n")
                stamina_score -=3
                print(f"your current STAMINA score is {stamina_score}:\n")
                sleep(4)
                play_stage_3()
                
                if stamina_score <6: 
                 print(f"your STAMINA is too low to continue.\n")
                 sleep(3)
                 sys.exit("Your adventure ends here")
            else:
                print ("You strike up an interesting converation with the lead developer who tells you his name is Tobias invites you into Studio X at the end of the day to give you demo. PHAT!. 3 STAMINA points added.")
                stamina_score +=3
                print(f"your current STAMINA score is {stamina_score}:\n")
                play_stage_3()

                    
    elif choice == "3":
                print("Checking your skill score...\n")
                sleep(3)
                if skill_score < 7:
                    print("You slide the new chair under a desk and take a seat. It crunches on its spindle and you colapse on the floor. The whole office erupts into raptious laughter! Seriously don't bother coming to work again.\n")
                    sleep(7)
                    stamina_score -=3
                    print("your credibility is in tatters. You fail in your quest here...")
                else:
                    print ("You slide the new chair under a desk and take a seat and swivel around like a BOSS! Who's the young hotshot in the power throne now! 6 STAMINA points added.")
                    stamina_score +=6
                    print(f"your current STAMINA score is {stamina_score}:\n")
                    sleep (5)
                    play_stage_3()
    else:
        print("Invalid choice. Please choose a valid option.")
            # Handle invalid choices here

#Stage 3 

def play_stage_3():
    global skill_score, stamina_score, luck_score
    print("Welcome to the next stage... - Studio X!\n")
    sleep(3)
    print("Everyone else in the office has left for the day, the lead developer Tobias, smiles and whispers that your understanding of gaming will never be the same again and your mind will soon be blasted into oblivion then leads you into Studio X!")
    sleep(8)
    print ("Once inside Studio X you waste no time, and as prompted by Tobias, you put on a translucent headband and a thin haptic gaming cape. A high-end gaming computer is powered up and then something unbelivable happens...\n")
    sleep(12)
    print ("It takes what feels like an age for your mind to catch up with itself. You eventually feel yourself mouthing the words WHERE THE HELL AM I? You can only describe what you're seeing as an out of body experience.\n")
    sleep(12)
    print ("You don't really know what else to say as you arrive at the virtual area known as the Influx gaming lounge. Your mind tries to pick out something particularly incredible that you see, but it's also what you feel that's blown you away.")
    sleep(12)
    print ("You hear a familiar voice speaking softly in your headphones. 'Don't move. Stay just where you are for a while until you acclimatize.' It says.\n")
    sleep(10)
    print ("The detail projected from your mixed-reality headband is spectacular.\n")
    sleep(6)
    print ("Extraordinary vistas pan out before your eyes of an emerald sea with a boundless stretch of pure white sandy beach beyond your veranda and snow-capped mountains in he distance as they then reformed into something more low-resolution with a flicker of your eyes...")
    sleep(7)
    print("Tobias says that from tomorrow you will be working with him and a few other collegues within this game to be part of an exiting new project his team are involved in.\n")
    sleep (7)
    print ("You wonder how you are going to sleep that night thinking about all the possibilities for the day ahead.")
    

play_stage_1()