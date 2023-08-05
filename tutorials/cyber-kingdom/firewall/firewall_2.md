### @explicitHints 1
### @flyoutOnly true

# Anomaly 1

```ghost
cyber.setupFirewall(function () {
    cyber.allowAll()
    cyber.addDenyFirewallRule(cyber.requireHat(WearingHat.NoHat))
    cyber.addDenyFirewallRule(cyber.requireHoldingItem(HoldingItem.NoItem))
    cyber.addDenyFirewallRule(cyber.requireLegs(Legs.TwoLegs))
})

```

## Anomaly 1 @showdialog
It's some anomalies! This anomaly seems to have a lot of legs and is trying to enter the castle...
We need to create a rule to stop it coming in the castle!   
![Anomaly](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/main/tutorials/cyber-kingdom/firewall/images/level_2.jpg)


## Deny rule
We need to come up with a rule to block access to the anomaly, but still allow villagers in.   
Add a ``||cyber:Add deny firewall rule||`` block to your rules. It allows you to tell the guards to deny access to anything that satisfies the rule.  

### Distinguishing Features
Can you see anything that might help us distinguish between a villager and this anomaly?   
Press the < (back) button to check the lookout view for what is coming if you aren't sure.
```template
cyber.setupFirewall(function () {
cyber.allowAll()
})
```

### ~ tutorialhint
```blocks
cyber.setupFirewall(function () {
    cyber.allowAll()
    cyber.addDenyFirewallRule(cyber.requireLegs(Legs.OverFourLegs))
})

```

```package
causeway-digital-makecode-extension=github:causewaydigital/pxt-causeway-digital-extension#cyber-kingdom
```
