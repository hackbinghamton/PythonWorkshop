# Unit Converter Project

# Project Overview

---

Welcome to the Unit Converter Project! This project is unlike the tutorials you have been going through thus far. Rather than telling you exactly what to do and how to do it, you'll be creating a project on your own with some small hints and nudges in the right direction. This will allow you to use the skills you have picked up in the previous sections to actually build something! 

If you are new to Python, this will not be so easy. But that's **okay**. This will be tough, but it **will** be worth it in the end. If you are get stuck and can't figure out how to continue, there are many organizers that can assist you. If you are working alone and are completely stuck, you *can* take a look at our finished project [here](https://github.com/HackBinghamton/PythonWorkshop/blob/unit-converter-project/Projects/unit-converter-completed.py), but we recommend you do everything you can on your own before taking a peek at it. 

This project can be very simple. The goal for this project is to create a program that will allow you to convert between two different units. If you're up for a challenge, you can also create a starting menu that will allow you to select from multiple conversion options, and handle any type of input. The cool thing about this project is that it can be as easy or as difficult as you want it to be. We recommend that you start off small and work your way up from there with incremental improvements. 

## Prerequisites

Before starting this project, you should have an understanding of 

1. [Data Types and Variables](https://colab.research.google.com/github/HackBinghamton/PythonWorkshop/blob/master/Intro/DataTypesAndVariables.ipynb)
2. [Printing and Input](https://colab.research.google.com/github/HackBinghamton/PythonWorkshop/blob/master/Intro/Printing_and_Input.ipynb)
3. [Control Flow](https://colab.research.google.com/github/HackBinghamton/PythonWorkshop/blob/master/Intro/ControlFlow.ipynb)
4. [Functions](https://colab.research.google.com/github/HackBinghamton/PythonWorkshop/blob/master/Intro/Functions.ipynb)
5. [Imports](https://colab.research.google.com/github/HackBinghamton/PythonWorkshop/blob/master/Intro/Imports.ipynb)
6. [Loops](https://colab.research.google.com/github/HackBinghamton/PythonWorkshop/blob/master/Intermediate/Loops.ipynb)

## Demo

Here is a demo of the project we will be creating: 

[![Unit Converter Project Demo](https://i.imgur.com/Dx3LeY7.png)](https://www.youtube.com/watch?v=OcBrMgludR4 "Unit Converter Project Demo")

As you can see from the short clip above, the program accepts two **parameters**. It accepts a `choice` and a `value` separated by a space. So the input of `1 30` signifies converting choice 1 (Celsius to Fahrenheit) with a value of 30 (Celsius). The output is then `86.0` (Fahrenheit).

# Project Development

## Working Backards

Let's take a look at the finished product and work backwards from there. If we take a look at the demo above, this is the user flow that we are able to observe:

- Menu with different options
- Asking for user input
- Handling user input and respond to the options selected
- Using the value from input to do the conversion
- Output the value to the screen
- Ask for user input again

You can implement these features in whatever way you want, and there isn't necessarily a *correct* order. What we will do in this project, however, is start with the conversions themselves, and then build the menu around it.

Let's start building the project!

## Creating the Conversions

So let's create the conversions. In a clean `.py` file, define a brand new function:

```python
def convert(choice, value):
	if choice == 1:
		return (amount * (9/5)) + 32
```

This code corresponds to the Celsius to Fahrenheit option from above. If the user selected choice 1, the `convert()` function returns the converted value. We recommend that you create a few more choices on your own now. Feel free to use the internet to look for formulas to implement. Some ideas can be Kelvin to Fahrenheit, Inches to Millimeters, Liters to Quarts, Kilograms to Pounds, or even years to seconds - be creative and have fun with them! 

Once you've got your options created and conversions implemented, move on to the next section, where you will actually handle user input. 

## Handling User Input

This next part can be accomplished in all sorts of different ways, but we just did it by having it handled in a single function, called `ask_question`:

```python
def ask_question():
	conversion = input("Enter a choice followed by the amount which you would like to convert: ")
	conversion_list = conversion.split()
	
	choice = conversion_list[0]
	amount = conversion_list[1]

	answer = convert(int(choice), int(amount)) # Not a good solution because there are lots of ways in which this can go wrong (more on this later)
  print(f"Answer: {answer}")
```

This is the start of our function: we are just asking for user input and then splitting up the response into an array by spaces. 

Then we separate each input, and call the convert function that we created above, passing in the choice and value. This should be pretty straightforward. There are lots of problems with this approach, which we will address at the end, but assuming the user does exactly what we want, this would work!  

## Our Main function

Now that we have our two functions created, we just want to make sure that they get called at the right time. To do so, we are going to create a new function, `main()`:

```python
def main():
    prompt = """
==============
UNIT CONVERTER
==============

What would you like to convert?

1. Celsius to Fahrenheit
2. Your option here
3. Your option here
.
.
.
N. Your N-th option here

(-1 to quit program)
            """
    print(prompt)
    # loop till user quits program
    while ask_question():
        pass
    print("\nThanks for using my unit conversion program!")

main()
```

This is how our function looks. You will need to change the conversion text to match what you implemented. You'll notice that we have a loop that continues running while `ask_question()` is true. As soon as it is false, we print a final massage for the program and it ends. 

## Testing for Edge Cases

Now comes the hard part. This program has a lot of issues. If the user does exactly what we tell them to, this project would be completed. The reality, however, is that users in the real world are really good at breaking programs, so we will want to think and see how can debug our code and make it userproof. 

Here are some problems that you will want to think about and address:

- What happens if the user doesn't input integers, but some other value (string or decimal or boolean)?
- What if the user doesn't input number in the right format? (`1 1 1` or `1` would be invalid input)
- What if the user doesn't input anything?
- What if the user selects a choice that doesn't exist?

Think about these problems and think how you can address them in the right function.

## Finishing and Polishing

If you were succcessfully able to address the edge cases, congratulations! You fought your way through a fairly difficult and complex task. 

Now are just want to put some finished touches on the project. For example, you might not have implemented a way to exit out of the project yet. Can you add functionality so that if the user types `-1` as a choice the program will simply end? 

Once you are done with that, go through the project one more time and see if there is functionality that doesn't look quite right. Test your code again, trying to break it, and make sure that you understand the lines of code you wrote. If you copied some code from online or from our completed repository (that's fine), consider adding some comments to ensure that you understand what is happening. 

# Conclusion

---

Are you satisfied with the project? If so, you're done! Congratulations! 

Now you can show this off to your friends and they'll be super jealous at how quickly you can convert liters to milliliters. 

Next, you can continue going through the intermediate tutorials, where you will learn how to create more complex and even cooler (seems impossible, I know) project. Good luck to you and your programming journey!