### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Ship docking

```template
for (let count = 0; count < 5; count++){
    player.say("Hello")
}
```

## Getting started with Loops @showdialog

In Python, if you want to run something multiple times (without copying and pasting code lots of times), you use what is called a loop.

There are 2 main types of loops in Python:

- **For loop** - Use this if you know how many times you want to loop for.

- **While loop** - Use this if you don't know how many times you are going to want to loop for.

We will be focusing on the **for loop** in this world.

A ``||loops: for loop||``is created using the following syntax:

```spy
for (let count = 0; count < 5; count++){
    player.say("hello")
}
```

The above code will run the `player.say("hello")` command 5 times.

## Covering the hatches @showdialog

![Captain](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-3/ship/captain.jpg)

**Captain Papert** - *We are just coming into dock now, but first, you wouldn't mind helping me cover over the hatches? They are down on the main deck of the ship.*

## Use your agent to cover the deck

Captain Papert has given your Agent some **carpet** (in slot 1). Can you use a ``||loops:for loop||`` to place the carpet over the hatches with ``||agent:agent.place()||``?

*Once you have completed a row, use your **whistle** (or ``||agent:agent.move()||``) to move your agent along, then run your code again.*

```spy
for (let count = 0; count < 6; count++){
    agent.move(FORWARD, 1)
    agent.place(DOWN)
}
```

## Note
To proceed to the next step, you must have completed the previous task!

## Building the gang plank

![Gangplank location](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-3/ship/gangplank.jpg)

Now the hatches are covered. The captain has brought the airship in as close as he can to the dock.

You will need to build a gangplank. Your agent has now got some planks in slot 1 of its inventory.

**Create a ``||loops:for loop||`` program to build the gangplank out to reach the dock. You will have to guess how far away the island is!**

```diffspy
for (let count = 0; count < 6; count++){
    agent.move(FORWARD, 1)
    agent.place(DOWN)
}
----------------------------
for (let count = 0; count < 8; count++){
    agent.move(FORWARD, 1)
    agent.place(DOWN)
}
```

## Gang Plank built!

Once complete, close this window and explore the town.
