{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# File Input and Output\n",
    "\n",
    "There are a lot of situations where being able to write to or read from a file can be useful for a Python program. Let's look at how you can interact with these files both as inputs and outputs.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Setup\n",
    "\n",
    "Run the below cell to set up the environment."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "!ls\n",
    "!echo \"This is a test file!\" > filename.txt\n",
    "!ls"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Getting Started\n",
    "\n",
    "Opening a file in Python is very easy, and only changes slightly whether you're reading or writing to a file.\n",
    "\n",
    "Here's the general structure of how you can open a file, whether for input or for output:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "file_obj = open(<filename here>, <access specifier>)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The filename is a path to a filename, whether an absolute path (e.g. `/home/username/some_text.txt`) or a relative path (e.g. `./folder/text_file.txt`). //Save for advanced????\n",
    "\n",
    "The access specifier defines how the program interacts with the file. These can be modes like reading, writing, appending, and more. In the following sections, we'll show how you can use each of these modes in your programs."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Input\n",
    "\n",
    "The `\"r\"` access specifier opens a file for reading. The following line opens a file called `filename.txt` for reading, and put the file object in a variable called `my_file`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_file = open(\"filename.txt\", \"r\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "`my_file` is only an object that lets you interface with `filename.txt`. To store the contents of `filename.txt` in a variable, you can use `.read()` on `my_file`, like so:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "file_text = my_file.read()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This copies the "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Wvhen opening a file for reading, you will receive an error if the file does not exist within the same folder as your Python program.\n",
    "\n",
    "Calling the read() function on a file variable will return a string of characters from the file. Just calling `my_file.read()` will return a string of the entire contents of the file. Calling read with a integer parameter will tell it how many characters to read starting from the beginning of the file. For example, `my_file.read(10)` will return a string of the first 10 characters from the file.\n",
    "\n",
    "Calling readline() on the file variable will return a string of all characters until the next occurrence of the newline character (\"\\n\").\n",
    "\n",
    "\n",
    "## Output\n",
    "There are two different ways to open a file for writing.\n",
    "\n",
    "The first is only for creating a new file. It will create a brand new file with the name that you give, and if a file by that name already exists **it will be overwritten, so be careful**. In this case, the second parameter becomes \"w\" for \"writing\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_file = open(\"filename.txt\", \"w\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now if you want to open a file that already exists and you **don't** want it to be completely overwritten, you can instead open that file for appending. The second parameter now becomes \"a\" for \"appending\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_file = open(\"filename.txt\", \"a\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Whether you open the file for writing or appending, the function used to write text into that file is very simple: write(). You can pass any string into this function and it will write it to the file. Including a newline character (\"\\n\") will force the next string written to the file to begin on a new line."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_file = open(\"filename.txt\", \"a\")\n",
    "my_file.write(\"Now this file has some text in it!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It's important to remember that any time you're done using a file, you should **always** make sure to close it using the close() function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_file = open(\"filename.txt\", \"w\")\n",
    "#Your\n",
    "#Code\n",
    "#Here\n",
    "my_file.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Usually it's not a big deal, but there are ways that people could steal private information if you don't remember to close your files!"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
