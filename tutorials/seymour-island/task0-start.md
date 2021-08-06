

### @flyoutOnly 1

# Introduction

```template
player.onItemInteracted(BLAZE_ROD, function () {
})

```

# 0. Introduction

## Introduction @unplugged

Welcome onboard, my name is Captain Papert. We have just left port and are on our way.   
Sailing time will be a few days, depending on the winds.   

![Captain](https://github.com/gbaman/minecraft-ee-seymour-island/raw/master/media/captain.jpg)

In this world, you will be solving a series of puzzles, using code. You can access the coding window at any time by pressing the **C** key on your keyboard.    
To solve these tasks, you will need to use an Agent.      
      
Wait, you didn't bring one....?

## Agent @unplugged

That's ok, you can borrow my spare Agent. You better look after him!

This little robot is your key to solving tasks in this world.   
It can move around, place blocks and break blocks as well!

![Agent](https://github.com/gbaman/minecraft-ee-seymour-island/raw/master/media/agent.jpg)

## Get started @unplugged

Let's get you started on training using your new Agent. First, lets try writing
some code to instruct it to move from the Diamond block to the Gold block.   
![Agent moving](https://github.com/gbaman/minecraft-ee-seymour-island/raw/master/media/task0-move.gif)

You may wish to close this window (hit the **esc** key) to find your agent.   
Remember, you can open it up again by pressing **C**

## Time to code
Drag out an ``||Agent:agent move||`` block into the ``||player:on item used||`` block.   
You will then need to change the **forward** to **left**.   
You might also need to change the number of steps...   

When you are ready to run your code, close this code window with the **esc** key
and while holding your **Blaze Rod** in your hand, right click.    
Use your keyboard number keys to select the correct slot. 

```blocks
player.onItemInteracted(BLAZE_ROD, function () {
    agent.move(LEFT, 2)
})
```

```package
seymour=github:gbaman/minecraft-ee-seymour-island
```
