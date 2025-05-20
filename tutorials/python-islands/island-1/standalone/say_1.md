### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0
### @codeStop players set @s f1-say-complete 1


# Island-1-Say
```template
player.say("Hello world!")
```

## Using the say() command @showdialog

In this activity, we will be exploring the `say()` command in Python. The `say()` command is used to output a message to the chat, from you! 

Here's how it works:
```python
player.say("Hello world!")
```
And what it would output:
![Say output](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/standalone/say1.jpg)

## Try it Yourself
Try the program below by pressing the Run button.    
What else might you want to say, try tweaking the text sections within the " " and see what happens.


## Why do you need quotation marks? @showdialog
As you can see we put quotation marks " " around the text within the say command.   

But why are these needed?...   

This is because, in Python, text (also known as a String) is marked as being contained within quotation marks.


## Why do you need quotation marks?
Try removing the second quotation mark. You will see that your code editor underlines the issue and you can't run your code.

Once you put back the quotation mark the red line will disappear and you will be able to run your code again.
```python
player.say("Hello world!")
```

## What are some other types of data? @showdialog

Strings (text) are just one type of data within Python. There are a few other interesting **Datatypes**.   
- Integers: Whole numbers, for example, 1, 5, -2
- Floats: Decimal numbers, for example, 1.4, 5.7, -3.8
- Booleans: True or False

The `say()` command supports outputting each of these, without the need for quotation marks.

## Other types of data
Try removing everything within the brackets of `player:player.say()`, including the quotation marks, and putting a different datatype within the brackets.

For example, an integer (5), a float (1.4), or a boolean (True)

```diffpython
player.say()
----------------------
player.say(5)
```

## Task complete
To finish the task change your code to output `"Task complete"`.

```diffpython
player.say()
----------------------
player.say("Task complete")
```
