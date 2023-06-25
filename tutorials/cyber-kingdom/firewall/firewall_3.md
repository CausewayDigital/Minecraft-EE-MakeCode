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


## Stop the virus
Add another rule to stop the virus. 
Can you see anything that might help us distinguish between a villager and a virus?


```template
cyber.setupFirewall(function () {
cyber.allowAll()
cyber.addDenyFirewallRule(cyber.requireLegs(Legs.OverFourLegs))
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