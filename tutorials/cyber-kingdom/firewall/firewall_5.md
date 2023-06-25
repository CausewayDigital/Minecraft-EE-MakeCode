### @explicitHints 1
### @flyoutOnly true

# TUTORIAL 5

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


## More villagers
You may need to make rules using an **and** statement. This means you can combine 2 rules together.   


```template
cyber.setupFirewall(function () {
cyber.allowAll()
cyber.addDenyFirewallRule(cyber.requireLegs(Legs.OverFourLegs))
cyber.addDenyFirewallRule(cyber.requireHat(WearingHat.NoHat))
})
```

### ~ tutorialhint
```blocks
cyber.setupFirewall(function () {
    cyber.allowAll()
    cyber.addDenyFirewallRule(cyber.requireLegs(Legs.OverFourLegs))
    cyber.addDenyFirewallRule(cyber.requireHat(WearingHat.NoHat))
})

```

```package
causeway-digital-makecode-extension=github:causewaydigital/pxt-causeway-digital-extension#cyber-kingdom
```