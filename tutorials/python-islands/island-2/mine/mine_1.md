### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Mine - 1 

```customts
/**
 * Functions for working in the mine
 */
namespace agent {
    /**
    * Checks if the ground below the agent is stable
    */
    //% block="agent check ground stable"
    export function check_ground_unstable(): boolean{
        const agent_pos = agent.getPosition()
        if (positions.equals(agent_pos, world(88, 146, 167))){
            return true
        }
        return false
    }

    /**
     * Alert ground below agent is unstable
     */
    //% block
    export function alert(){
        if(agent.check_ground_unstable()){
            player.say("Unstable ground alert!!!")
            agent.destroy(DOWN)
        }else{
            player.say("This seems to be a false alarm, the ground below the agent seems pretty stable... Try moving to a different location")
        }
    }
}
```

```ghost
player.say("")
agent.check_ground_unstable()
agent.alert()
agent.move(FORWARD, 1)
```

## Testing the unstable ground @showdialog

With an area of unstable ground having opened up, use your agent to test each block to check it is safe.

You have been informed by the miner that an area of ground has opened up and sank down. He is concerned that the ground below could be unstable and has asked if you can use your agent (which can float), to check each block individually to see if it is safe.

![Unstable ground](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-2/mine/cover1.jpg)

## Testing the ground

The miner has provided your agent with a special function to check the ground below it is safe, ``||agent:agent.check_ground_unstable()||``

This function will provide back:

- **True**  : If the ground below your agent is stable.
- **False** : If the ground below your agent is unstable.

**Using ``||player:player.say()||`` check if the ground below your agent is safe.**
```spy
player.say(agent.check_ground_unstable())
```

## Alerting

The 2nd special function the miner has given your agent is ``||agent:agent.alert()||``

You should run this piece of code if you find any unstable ground.

**Using what you learnt in the previous sections on if statements, create a program that runs alert() if the unstable ground is detected**

```spy
if (agent.check_ground_unstable()){
    agent.alert()
}
```

## Scanning the gravel pit
Now add in ``||agent:agent.move()||`` to block by block, move your agent around the gravel area.

**Update you code to move your agent **FORWARD** each time your code runs**
```diffspy
if (agent.check_ground_unstable()){
    agent.alert()
}
---------------------------------
agent.move(FORWARD, 1)
if (agent.check_ground_unstable()){
    agent.alert()
}
```

## Scan the whole gravel pit
Once your code is complete, try using it to check each gravel block to find if any are unstable.