### @explicitHints 1
### @flyoutOnly true

# First filters

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
We need to create a rule to stop it coming in the castle!   


## Deny rule
We need to come up with a rule to block access to the virus, but still allow villagers in.   
Add a ``||cyber:Add deny firewall rule||`` block to your rules. It allows you to tell the guards to deny access to anyone that satisfies the rule.  

### Distinguishing Features
Can you see anything that might help us distinguish between a villager and a virus?
```template
cyber.setupFirewall(function () {
cyber.allowAll()
})
```

### ~ tutorialhint
```blocks
cyber.setupFirewall(function () {
    cyber.allowAll()
    cyber.addDenyFirewallRule(cyber.requireHat(WearingHat.NoHat))
})

```

```package
causeway-digital-makecode-extension=github:causewaydigital/pxt-causeway-digital-extension#cyber-kingdom
```