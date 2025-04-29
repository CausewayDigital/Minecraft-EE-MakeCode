# Factory
Repair the airship


## Repair the Hull @showdialog

![Airship Factory](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-4/factory/cover.jpg)

It looks like the crew at the airship factory need a hand repairing one of their new airships. Send your Agent in to fix the holes!


Before we get started, close this window and find your agent, it should be inside the airship.   

## Step 1
Now you have found your agent, let's move the agent forward by one block, to have it hover over the first hole for repair.

**Write the code to move your agent forward.**

```python
agent.move(FORWARD, 1)
```

## Step 2
Now with the agent in place, we'll need to move the agent down to the bottom of the docks to collect the fallen blocks below.   

To do this, we will use a while loop that moves the agent down, only running as long as there is air below it.   



**Complete the while loop below, to run the move line, when `agent.inspect` in the DOWN direction is equal to `"air"`!**
### *User Code* 
```Python
while agent.    (    ).id ==            :
    # Finish the while loop above 
    agent.move(DOWN)
```
When you're ready, move to the next section.
## Step 3



As the agent is at the bottom of the dock, it can collect the blocks that have broken and fallen down. You can see where these blocks are by using the viewing gallery below the airship.



To collect blocks, use the `agent.collect` function.



Here's how to use it:

```python

agent.collect_all()

```



**Write an `agent.collect` line, to collect the fallen blocks, in the code block below.**
### *User Code* 
```Python


# Write your code above
```
## Step 4



With the agent now holding onto the block to repair the airship with, we need to move it back to the correct position, to replace the block.



The Factory worker told you that the `y` coordinate to repair is at `157`.



To get the y position of the agent, use:

```python

agent.position.y

```



**Complete the code below, to loop the code when the agent's y coordinate is not equal to `157`. Note != means "is not equal".**
### *User Code* 
```Python
while(            !=    ):
    agent.move(UP)
```
Once you have finished this section, move on to the last section!
## Step 5



Now that the agent is at the correct y (altitude) coordinate, you can place the block that your agent just collected, using the `agent.place` function.



Here's a reminder on how to use the function...

```python

agent.place(direction, slot_number)

```



**In the code block below, write the line to place the block from slot number `1`, in the `DOWN` direction.**
### *User Code* 
```Python


# Add your `agent.place` code above
```
## Step 6



Great, now that you have successfully guided your agent through fixing one block, let's put all of the previous code together into one big `while` loop to automate fixing the rest of the airship.



**Complete the while loop below, so that the outer while loop runs while agent `inspect` FORWARD direction is equal to `"air"`.**
### *User Code* 
```Python
while agent.    (    ).id ==      :
    # Complete the while loop above
    # Step 1
    agent.move(FORWARD)
    
    # Step 2
    while agent.inspect(DOWN).id == "air":
        agent.move(DOWN)

    # Step 3
    agent.collect_all()

    # Step 4
    while agent.position.y != 157:
        agent.move(UP)

    # Step 5
    agent.place(DOWN,1)
```
Great! Run your code and have your agent finish repairing the airship.
