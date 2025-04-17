### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0


# Introduction to Variables


```template
// Edit the text (String) below to add your own message
my_amazing_variable = "Test" 

// This line below outputs the contents of your variable to game chat
player.say(my_amazing_variable)
```


## What are Variables? @showdialog
In this activity, you will be exploring the use of `Variables` within Python and how they work.   

In programming, `Variables` are temporary places to store information. They allow data to be saved and accessed later. Each `Variable` has a name, that you give it.   

To create a variable, have a look at the code below:

```python

my_amazing_variable = "Hello world"

```


## Try it Youself
Run the program and see what happens. Perhaps try tweaking the text sections within the " ".


## Overwriting a Variable @showdialog

You can also change the contents of a `Variable` you have already created, with the same process, for example:

```python

my_amazing_variable = "Hello"

# This line below will overwrite "Hello" with "World" instead

my_amazing_variable = "World"

```

## Try Overwriting a Variable
Try changing `my_amazing_variable` between where you create it and where you use the command `||player:player.say(STRING)||`.

```python

my_amazing_variable = "Hello"

// This line below will overwrite "Hello" with "World" instead

my_amazing_variable = "World"

```

## Variable Conclusion @showdialog
Variables are extremely powerful and are used everywhere in coding!   

In Python, they can store any data (including Strings, Integers, Floats or Booleans) and can be accessed easily elsewhere within your program.   

Remember, they always use the following format: 
```python
variable_name = data_being_stored
```
For example:
```python
name = "bob"
age = 5
```

Once you have finished, change your code so it outputs "Task complete".

## All Done
Once you have finished, change your code so it outputs "Task complete" to complete the task.

```python
my_amazing_variable = "Test"
my_amazing_variable = "Task complete"

player.say(my_amazing_variable)
```
