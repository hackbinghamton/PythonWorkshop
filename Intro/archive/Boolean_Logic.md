# Boolean Logic
As you saw in Functions your python code can respond to conditions.
An easy way to do this is with if/else blocks.

```
a = 23
if a==87:
    print("how?")
elif a<16:
    print("wait...what?")
else:
    print("it worked!")
```

This code should print it worked!
Can you explain why?

```
a = 23
if a==87:
    print("how?")
elif a<16:
    print("wait...what?")
elif a>5:
    print("look now.")
else:
    print("it worked!")
```

This code should print only look now.
Your computer tests each of the statements after an if or elif. 
When it finds a True statement it completes only the block under it and skips the rest.
If you have two "if"s in a row, the second "if" won't be skipped.
Only "elif"s or "else" get skipped.

Many different statements cam be put after an if/elif.
An *==* indicates two statements are equivalent *!=* is the opposite.
Other logic symbols include *<*, *<=*, *>*, *>=*.
In python *'and'* indicates intersect and *'or'* indicates union.

```
if 5==5 and 4<=27:
    print("this should print)

if True:
    print("this should print")
```   

### Write a function that utilizes logic symbols
---
#### Next Section (Recommended): Input
