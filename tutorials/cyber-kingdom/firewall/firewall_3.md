### @explicitHints 1
### @flyoutOnly true

# Anomaly 2

```ghost
cyber.setupFirewall(function () {
    cyber.allowAll()
    cyber.addDenyFirewallRule(cyber.requireHat(WearingHat.NoHat))
    cyber.addDenyFirewallRule(cyber.requireHoldingItem(HoldingItem.NoItem))
    cyber.addDenyFirewallRule(cyber.requireLegs(Legs.TwoLegs))
})

```

## Anomaly 2 @showdialog
It's another anomaly!   
![Anomaly](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/main/tutorials/cyber-kingdom/firewall/images/level_3.jpg)


## Stop the anomaly
This is a different anomaly! Add another rule to stop this particular anomaly. 
Can you see anything that might help us distinguish between a villager and the anomaly?   
Remember, you can press the < (back) button to check the lookout view again.


```template
cyber.setupFirewall(function () {
cyber.allowAll()
cyber.addDenyFirewallRule(cyber.requireLegs(Legs.OverFourLegs))
})
```

### ~ tutorialhint
Are those villagers wearing hats?


```package
causeway-digital-makecode-extension=github:causewaydigital/pxt-causeway-digital-extension#cyber-kingdom
```