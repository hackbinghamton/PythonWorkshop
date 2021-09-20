# Text-based Aventure Game Project

# Project Overview

Welcome to the Text-based Adventure Game Project! This project is unlike the tutorials you have been going through thus far. Rather than telling you exactly what to do and how to do it, you'll be creating a project on your own with some small hints and nudges in the right direction. This will allow you to use the skills you have picked up in the previous sections to actually build something! 

You can take a look at the completed project [HERE](https://github.com/HackBinghamton/PythonWorkshop/blob/text-based-adventure-project/Projects/text-based-adventure.py).

In this project, you will be creating a Game class that tells the user a story that you will create, and then prompt the user to pick the best 'answer'. You will be able to be creative and add as many features as you'd like and as many branches to the story as you would want to. 

The instruction are going to be barebones, because we want you to play around with writing code yourself and come up with your own story, making this project completely unique to you. Our instructions will simply explain what we did, and give you ideas of what you can do in your own project. 

## Prerequisites

Before starting this project, you should have an understanding of the sections included in

1. [Introductory Python](https://github.com/HackBinghamton/PythonWorkshop/tree/master/Intro)
2. [Intermediate Python](https://github.com/HackBinghamton/PythonWorkshop/tree/master/Intermediate)

## Demo

Here is a demo of the project we will be creating:

[![Text-Based Adventure Game Demo](https://i.imgur.com/kdOtnhH.png)](https://youtu.be/-8Ddwuj5PwU "Text-Based Adventure Game Demo")

As you can see in the demo above, we are printing a story to the user, printing some attributes about the player, and then directing the player to select an option for the story to branch off of (though we did not implement any branches). 

# Project Development

## Kicking it off

To start off, let's begin by creating our `Game` class and some of the methods that we expect to implement. We're going to want a `story()`, a `prompt()`, some kind of action that the user can perform, and then an end to the story.

Here's how we did it, but feel free to go completely off-course for this project.

```python
class Game: 
    def __init__(): # Start the game
        pass

    def attack(): # An action the player can perform
        pass

    def prompt(): # Prompts the user to select an action for our player to perform

   def endGame(): # Ends our adventure
       pass

    def story(): # Tells the story to our player
        pass
```

## The init function

The `__init__` function is where you can keep track of different values relating to your player. For example, you might want to keep track of your player's `health`, `attack_strength`, `defense_strength`, `speed`, or `hunger`.

Our `__init__` function welcomes the player to the game, asks for the player's name, and then initializes `max_health`, `current_health`, and `max_attack`, to be used while playing the game. 

## The story

Because this is a text-based adventure game, the story is main part of our game. 

The way we did this is by printing out text to the screen introducing the story with `print("Story here")`, and then directing the user to respond inside of the `prompt()` function. 

As an example, here is the beginning of our story

```python
    def story(self):
        print("\nYou wake up cold and afraid in a dark, wet dungeon...")
        print("You see a pair of green eyes looking at you in the corner of the room...")
        print("You have no choice but to attack!!")
        self.prompt("attack", "GOBLIN", 5)
        print("You take the GOBLIN's sword...")
        print("Its body lies in front of an open door...")
        self.prompt("enter")
        print("You see another GOBLIN and a large, ugly TROLL...")
        print("The GOBLIN lunges at you!")
        self.prompt("attack", "GOBLIN", 6)
        ...
```

Again, feel absolutely free to change the story to your liking. 

Next, we will handle user input to make the story interactive. 

## Building our dynamic adventure

Now we're going to respond to user input by implementing our `prompt()` function. 

Here is our entire `prompt()` function. Let's break it down to see how you might implement yours. 

```python
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
                        print("...")
                        print("")
                    print"It was a health potion!")
                    print("Bonus health has been added!")
                    self.current_health += 10
                    print("<< Current health: " + str(self.current_health) + " >>")
                    prompt_status = False
```

As you can tell, we have a big `while` loop with a bunch of nested `if` statements, meaning that we will continue prompting the user with responses until the situation is over (for example, keep fightingin an enemy until you defeat them).

We pass in a `type` variable, and then check for the different types that our game supports, such as `drink`, `attack`, and `enter`. You can make your own prompt function support as many `type`s as you see fit. 

So we check the type, then ask for user input, check the user input, and then run code to respond to it. 

For example, if you wanted your story to feature a bar fight, you can create `type`s to respond to things such as `attack`, `defend`, or even `end_fight`. 

Then you can return the results from prompt and use that to create branches off of your story. So if you ended your bar fight gracefully, maybe you can have a branch of your story where you become great friends with the person who was at some point your enemy. And if your player decided to go ahead with the fight, you might want to create consequences for doing so. 


## Final touches

Once you're happy with the result of the branches of your story and are done responding to all of the conditionals, you can begin going back through your code and adding some more features to make your game *even better*. 

We added a small function that makes your game print out your story in a much more game-like way, called `pokePrint`.

Here's how we implemented it

```python
def pokePrint(self, string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.025)
    print("")
    time.sleep(.9)
```
This function prints out each character at a time rather than printing out an entire line all it once. This makes it a lot easier for your player to read through the story. So in our `story()`, we replaced each `print()` statement, with `self.pokePrint()`.


Another feature in our game ia a `levelUp` function. The way this works is that after attacking some enemies and defeating them, your player will sometimes "Level Up", restoring your health, and increase your attack strength. You can make a similar feature, perhaps making it randomly give powerups to your player or making it so that a player can upgrade their max health. 

Some other ideas for features include:
    
-  An experience-based system where your player can redeem points for better strength or health capabilities


- Make your story only have 1 branch that allows your player to win. This would make your player keep playing the game until they can make the "correct" decisions and win! It's an easy way to make your game longer with a bit less creative work. 

- Look into how to make different [colored text](https://www.geeksforgeeks.org/print-colors-python-terminal/) appear on the screen to make the reading less boring!


# Conclusion

Are you satisfied with the project? If so, you're done! Congratulations! 

Now you can send this game to your friends, and have them play it! 
