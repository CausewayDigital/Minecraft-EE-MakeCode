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
})

```

## Soldiers @showdialog
The rival kingdom it seems didn't take kindly to us blocking access to their spies and have sent soldiers!
![Soldiers](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/main/tutorials/cyber-kingdom/firewall/images/level_6.jpg)


## Spies!
Quickly, create some rules to block these solders, we can't have them getting through the castle walls! 
I wonder how we could differentiate them from normal villagers?   


```template
cyber.setupFirewall(function () {
cyber.allowAll()
cyber.addDenyFirewallRule(cyber.requireLegs(Legs.OverFourLegs))
cyber.addDenyFirewallRule(cyber.ruleAnd(cyber.requireHat(WearingHat.NoHat), cyber.requireHoldingItem(HoldingItem.NoItem)))
cyber.addDenyFirewallRule(cyber.requireEyewear(WearingEyeware.WearingEyeware))
})
```


```package
causeway-digital-makecode-extension=github:causewaydigital/pxt-causeway-digital-extension#cyber-kingdom
```