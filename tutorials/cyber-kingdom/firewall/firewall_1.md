### @explicitHints 1
### @flyoutOnly true

# Allowing everything

## Villagers @unplugged
It looks like there are a group of villagers on their way. Let's start by creating a firewall that allows all.   
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