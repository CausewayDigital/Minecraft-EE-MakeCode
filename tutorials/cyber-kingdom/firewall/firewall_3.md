### @explicitHints 1
### @flyoutOnly true

# Virus

```ghost
cyber.setupFirewall(function () {
    cyber.allowAll()
    cyber.addDenyFirewallRule(cyber.requireHat(WearingHat.NoHat))
    cyber.addDenyFirewallRule(cyber.requireHoldingItem(HoldingItem.NoItem))
    cyber.addDenyFirewallRule(cyber.requireLegs(Legs.TwoLegs))
})

```

## Virus @showdialog
It's a Virus!   
![Virus](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/main/tutorials/cyber-kingdom/firewall/images/level_3.jpg)


## Stop the virus
A different type of malware is coming! Add another rule to stop the virus. 
Can you see anything that might help us distinguish between a villager and a virus?   
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