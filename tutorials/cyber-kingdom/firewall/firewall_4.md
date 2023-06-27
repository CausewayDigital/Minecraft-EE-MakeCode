### @explicitHints 1
### @flyoutOnly true

# Combining rules

```ghost
cyber.setupFirewall(function () {
    cyber.allowAll()
    cyber.addDenyFirewallRule(cyber.requireHat(WearingHat.NoHat))
    cyber.addDenyFirewallRule(cyber.requireHoldingItem(HoldingItem.NoItem))
    cyber.addDenyFirewallRule(cyber.requireLegs(Legs.TwoLegs))
    cyber.addDenyFirewallRule(cyber.ruleAnd(cyber.requireLegs(Legs.OverFourLegs), cyber.requireHoldingItem(HoldingItem.NoItem)))
})

```

## More villagers @showdialog
It looks like there's a large group of villagers on their way.   
Are they all going to be allowed through the firewall? 
![Villagers](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/main/tutorials/cyber-kingdom/firewall/images/level_4.jpg)


## More villagers
You may need to make rules using an **and** statement. This means you can combine 2 rules together.   
Watch out, some of these villages don't have hats, but they are carrying items like a pickaxe or map.   


```template
cyber.setupFirewall(function () {
cyber.allowAll()
cyber.addDenyFirewallRule(cyber.requireLegs(Legs.OverFourLegs))
cyber.addDenyFirewallRule(cyber.requireHat(WearingHat.NoHat))
})
```

### ~ tutorialhint
The virus has 2 legs and doesn't seem to be holding anything.

```package
causeway-digital-makecode-extension=github:causewaydigital/pxt-causeway-digital-extension#cyber-kingdom
```