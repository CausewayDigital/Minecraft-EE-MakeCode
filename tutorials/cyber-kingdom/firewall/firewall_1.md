### @explicitHints 1
### @flyoutOnly true

# Allowing everything

## What's a Firewall? @unplugged
A Firewall is a filtering system for traffic entering (and sometimes exiting) a network or location.    
It is based on created allow or deny rules to allow or deny different types of traffic.   
In this task, you will be building up a series of rules to allow or deny different characters into the castle.

## Villagers @unplugged
It looks like there are a group of villagers on their way. Let's start by creating a firewall that allows all.   
![Villages](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/main/tutorials/cyber-kingdom/firewall/images/level_1.jpg)
## Step 1
It looks like there are a group of villagers on their way. Let's start by creating a firewall that allows all.   
When you are ready to try the firewall, press the play button.
```template
cyber.setupFirewall(function () {
})
```

### ~ tutorialhint
```blocks
cyber.setupFirewall(function () {
    cyber.allowAll()
})

```

```package
causeway-digital-makecode-extension=github:causewaydigital/pxt-causeway-digital-extension#cyber-kingdom
```