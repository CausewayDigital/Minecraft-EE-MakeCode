### @explicitHints 1
### @flyoutOnly true

# Soldiers

```ghost
cyber.setupFirewall(function () {
    cyber.allowAll()
    cyber.addDenyFirewallRule(cyber.requireHat(WearingHat.NoHat))
    cyber.addDenyFirewallRule(cyber.requireHoldingItem(HoldingItem.NoItem))
    cyber.addDenyFirewallRule(cyber.requireLegs(Legs.TwoLegs))
    cyber.addDenyFirewallRule(cyber.ruleAnd(cyber.requireLegs(Legs.OverFourLegs), cyber.requireHoldingItem(HoldingItem.NoItem)))
    cyber.addDenyFirewallRule(cyber.requireEyewear(WearingEyeware.WearingEyeware))
    cyber.addDenyFirewallRule(cyber.requireCrest(cyber.createGridString(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)))
})

```

## Soldiers @showdialog
The rival kingdom it seems didn't take kindly to us blocking access to their spies and have sent soldiers!
![Soldiers](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/main/tutorials/cyber-kingdom/firewall/images/level_6.jpg)


## Soldiers!
Quickly, create some rules to block these solders, we can't have them getting through the castle walls!   
We could use their royal crest on the shields to help differentiate them. Our soldiers have a **golden** and **purple** crest, they must be allowed back in.   


```template
cyber.setupFirewall(function () {
cyber.allowAll()
cyber.addDenyFirewallRule(cyber.requireLegs(Legs.OverFourLegs))
cyber.addDenyFirewallRule(cyber.ruleAnd(cyber.requireHat(WearingHat.NoHat), cyber.requireHoldingItem(HoldingItem.NoItem)))
cyber.addDenyFirewallRule(cyber.requireEyewear(WearingEyeware.WearingEyeware))
})
```

### ~ tutorialhint
Pay special attention to the soldiers shields, could we filter by those? Be careful not to block our soldiers though!
![Soldiers Shields](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/main/tutorials/cyber-kingdom/firewall/images/level_6_shields.jpg)



```package
causeway-digital-makecode-extension=github:causewaydigital/pxt-causeway-digital-extension#cyber-kingdom
```