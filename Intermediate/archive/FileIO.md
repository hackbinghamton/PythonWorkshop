# File Input and Output

There are a lot of situations where being able to write to or read from a file can be useful for a Python program. Let's look at how you can interact with these files both as inputs and outputs.

Opening a file in Python is very easy, and only changes slightly whether you're reading or writing to a file.

## Input
The following code will open a file for reading:

```python
my_file = open("filename.txt", "r")
```

Note that you must give the complete file name as the first parameter, including any file type extension. The second parameter, "r" specifies "reading".

When opening a file for reading, you will receive an error if the file does not exist within the same folder as your Python program.

Calling the read() function on a file variable will return a string of characters from the file. Just calling `my_file.read()` will return a string of the entire contents of the file. Calling read with a integer parameter will tell it how many characters to read starting from the beginning of the file. For example, `my_file.read(10)` will return a string of the first 10 characters from the file.

Calling readline() on the file variable will return a string of all characters until the next occurrence of the newline character ("\n").


## Output
There are two different ways to open a file for writing.

The first is only for creating a new file. It will create a brand new file with the name that you give, and if a file by that name already exists **it will be overwritten, so be careful**. In this case, the second parameter becomes "w" for "writing".

```python
my_file = open("filename.txt", "w")
```

Now if you want to open a file that already exists and you **don't** want it to be completely overwritten, you can instead open that file for appending. The second parameter now becomes "a" for "appending".

```python
my_file = open("filename.txt", "a")
```

Whether you open the file for writing or appending, the function used to write text into that file is very simple: write(). You can pass any string into this function and it will write it to the file. Including a newline character ("\n") will force the next string written to the file to begin on a new line.

```python
my_file = open("filename.txt", "a")
my_file.write("Now this file has some text in it!")
```

It's important to remember that any time you're done using a file, you should **always** make sure to close it using the close() function:

```python
my_file = open("filename.txt", "w")
#Your
#Code
#Here
my_file.close()
```

Usually it's not a big deal, but there are ways that people could steal private information if you don't remember to close your files!
