### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0


# Python Islands 1 - Farming

```template
// Add your code below
agent
```

## Introduction to farming @showdialog
Using our agent, let's help the farmer till the ground and plant some seeds. The farmer has already placed the seeds in the agent inventory, ready to go!   

![Farming](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-1/farm/farm.jpg)

## Moving the agent into place
The farmer has added 3 markers over the field to show you where to till the soil.
Use `||agent:agent.move(DIRECTION, 1)||` to move your agent to one of the markers.   
Remember to change the `1` above to the number of blocks you want to move.
```python
agent.move(LEFT, 3)
```


## Tilling the required spots 
Tilling prepares normal dirt so you can grow seeds. Once you have your agent directly on top of a dirt block (using `||agent:agent.move(FORWARD)||`), you should till it.
To till dirt using your agent, use `||agent:agent.till(DIRECTION)||`. 


```python
agent.move(LEFT, 3)
agent.till(DOWN)
```

## Planting seeds
Now that the ground has been tilled, you should see the marker change to a white colour.  
Next, you need to plant the seeds using `||agent:agent.place(DIRECTION)||`.


```python
agent.move(LEFT, 3)
agent.till(DOWN)
agent.place(DOWN)
```

## Plant the rest of the seeds
Now you have planted a seed it's time to finish the job by planting the other 2 seeds. 
Take a look for the markers placed by the farmer.  

