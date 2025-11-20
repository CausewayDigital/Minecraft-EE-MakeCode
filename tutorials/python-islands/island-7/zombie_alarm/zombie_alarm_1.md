### @flyoutOnly true
### @diffs false
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Zombie Alarm

## Introduction @showdialog

In this exercise, you will build a program in Python that follows the flowchart below.

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/zombie_alarm/images/flowchart.png)

Zombies are always an issue, in this exercise build a system that can alert everyone to the presence of any zombies that have spawned!

Following the program flowchart below, create a Python program that:

- Check if zombie has spawns and if true:
    - Plays thunder sound
    - Whispers to all players

## Part 1

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/zombie_alarm/images/flowchart-landscape_1.png)

Code the flowchart.

```python
def on_entity_spawned(mob, spawner):
    pass
events.on_entity_spawned(on_entity_spawned)
```

- Create a function that is called when a mob spawns

## Part 2

![Cover image](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-7/zombie_alarm/images/flowchart-landscape_2.png)

Code the flowchart.

```
```
- If the mob is a zombie, play the thunder sound and send a message to the chat
- Otherwise ignore the mob spawn

```ghost
def on_entity_spawned(mob, spawner):
    if mob == ZOMBIE:
        music.play_sound(Sound.THUNDER)
        player.say("Zombie Spawned!")
events.on_entity_spawned(on_entity_spawned)
```

```package
events
music=github:microsoft/makecode-minecraft-music#v0.0.8
```