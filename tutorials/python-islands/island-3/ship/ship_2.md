### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Ship Docking 2

## Building the Gang Plank @showdialog

![Gangplank location](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-3/ship/gangplank.jpg)

Now the hatches are covered. The captain has brought the airship in as close as he can to the dock.

You will need to build a gangplank. Your agent has now got some planks in slot 1 of its inventory.

## Building the Gang Plank

**Create a ``||loops:for||`` loop program that moves your agent `FORWARD`, while placing blocks bellow, to build the gangplank out to reach the dock. You will have to guess how far away the island is!**

```python
for i in range(8):
    agent.move(FORWARD, 1)
    agent.place(DOWN)
```

## Gang Plank built!

Once complete, close this window and explore the town.

