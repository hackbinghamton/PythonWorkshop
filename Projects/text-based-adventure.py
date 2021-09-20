import time
import sys
import webbrowser
import random

class Game:
    def __init__(self):
        print("\n\t<< Welcome to the HackBU adventure game! >> \n")
        time.sleep(1)
        self.name = str(input("Enter your character's name: ")).upper()
        self.max_health = 20
        self.current_health = self.max_health
        self.max_attack = 10
        print("<< Current health: " + str(self.current_health) + " >>")
        print("<< Current max attack: " + str(self.max_attack) + " >>")
        time.sleep(1)

    def pokePrint(self, string):
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.025)
        print("")
        time.sleep(.9)

    def attack(self, monster_name, monster_resistance):
        if random.randrange(1, self.max_attack) > monster_resistance:
            self.pokePrint("You slayed the " + monster_name + "!")
            return False
        else:
            if monster_name == "GOBLIN":
                self.current_health -= random.randrange(1, 3)
            elif monster_name == "TROLL":
                self.current_health -= random.randrange(2, 5)
            elif monster_name == "JOE":
                self.current_health -= random.randrange(4, 8)
            self.pokePrint("You took damage!")
            if self.current_health <= 0:
                self.pokePrint("You died...")
                self.pokePrint("\n\t<< Game Over >>")
                sys.exit()
            print("<< Current health: " + str(self.current_health) + " >>")
            return True


    def prompt(self, type, str_cond="null", int_cond=0):
        prompt_status = True
        while prompt_status:
            if type == "enter":
                user_inp = input("\n\tType [e] to enter the next room: ")
                if user_inp == "e":
                    prompt_status = False
            elif type == "attack":
                user_inp = input("\n\tType [a] to attack! ")
                if user_inp == "a":
                    prompt_status = self.attack(str_cond, int_cond)
            elif type == "drink":
                user_inp = input("\n\tType [d] to drink the potion! ")
                if user_inp == "d":
                    for i in range(3):
                        self.pokePrint("...")
                        print("")
                    self.pokePrint("It was a health potion!")
                    self.pokePrint("Bonus health has been added!")
                    self.current_health += 10
                    print("<< Current health: " + str(self.current_health) + " >>")
                    prompt_status = False

    def levelUp(self):
        self.pokePrint("\n\tLEVEL UP!")
        self.pokePrint("\tHealth has been boosted and restored!")
        self.pokePrint("\tMax attack has been boosted!\n")
        self.max_health += 7
        self.current_health = self.max_health
        self.max_attack += 5
        print("<< Current health: " + str(self.current_health) + " >>")
        print("<< Current max attack: " + str(self.max_attack) + " >>")

    def endGame(self):
        self.pokePrint("JOE collapses to the ground.")
        self.pokePrint("He says:")
        self.pokePrint("'Bruh'")
        self.pokePrint("'You can take my money ig...'")
        ### uncomment the next line to force the 1HP easter egg ###
        #self.current_health = 1
        if self.current_health == 1:
            self.pokePrint("'But one last thing...'")
            for i in range(3):
                self.pokePrint("...")
            self.pokePrint("'Get wrecked, kid ;)'")
            webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0&ab_channel=DeeckPeeck")
        else:
            self.pokePrint("'GG...'")
            print("\n\tVICTORY to " + self.name + "!!")
            print("\n>>thanks for playing!\n")


    def story(self):
        self.pokePrint("\nYou wake up cold and afraid in a dark, wet dungeon...")
        self.pokePrint("You see a pair of green eyes looking at you in the corner of the room...")
        self.pokePrint("You have no choice but to attack!!")
        self.prompt("attack", "GOBLIN", 5)
        self.pokePrint("You take the GOBLIN's sword...")
        self.pokePrint("Its body lies in front of an open door...")
        self.prompt("enter")
        self.pokePrint("You see another GOBLIN and a large, ugly TROLL...")
        self.pokePrint("The GOBLIN lunges at you!")
        self.prompt("attack", "GOBLIN", 6)
        self.levelUp()
        self.pokePrint("The TROLL stumbles toward you with his large CLUB...")
        self.prompt("attack", "TROLL", 8)
        self.pokePrint("In the corner of the room, you see a magical potion...")
        self.prompt("drink")
        self.pokePrint("\nYou hear low, deep moaning coming from the next room...")
        self.pokePrint("You feel chills running down your spine...")
        self.prompt("enter")
        self.pokePrint("Four more TROLLs even bigger than the last turn around and look at you...")
        self.pokePrint("They start walking toward you...")
        self.pokePrint("Attack!!")
        for i in range(4):
            self.prompt("attack", "TROLL", 10)
        self.levelUp()
        self.pokePrint("As the last TROLL falls to his knees, you feel an intense wave of heat blast through a narrow doorway...")
        self.pokePrint("A loud, deep roar echoes throughout the dungeon...")
        self.pokePrint("You raise your sword and enter the doorway...")
        self.prompt("enter")
        self.pokePrint("A long, narrow, rickety staircase trails down towards the abyss of the deep dungeon...")
        self.pokePrint("As you walk down the staircase, the heat grows stronger and stronger...")
        self.pokePrint("You reach a set of large wooden double doors...")
        self.prompt("enter")
        self.pokePrint("You enter a massive chamber, filled with gold...")
        self.pokePrint("Except for one corner...")
        self.pokePrint("It's completely dark...")
        self.pokePrint("Until two blood-red eyes open...")
        self.pokePrint("It's JOE! The legendary RED DRAGON!")
        self.prompt("attack", "JOE", 16)
        self.endGame()


def main():
    HackBU = Game()
    HackBU.story()

main()
