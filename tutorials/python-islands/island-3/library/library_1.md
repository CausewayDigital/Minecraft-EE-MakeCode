### @flyoutOnly true
### @diffs true
### @hideDone true
### @codeStart players set @s codeExecution 1
### @codeStop players set @s codeExecution 0

# Library

```customts
/**
 * Functions for working in the Library
 */
namespace agent {
    /**
    * Checks if the Spellbook is in shelf
    */
    //% block="agent check shelf %direction"
    //% direction.defl=FORWARD
    export function found_book(direction: SixDirection): boolean {
        let block = agent.inspect(AgentInspection.Block, direction)
        if (block == DEAD_BRAIN_CORAL_BLOCK) {
            return true
        }
        return false
    }

    /**
     * Marks the shelf the Spellbook is in
     */
    //% block="agent mark book %direction"
    //% direction.defl=FORWARD
    export function mark_book(direction: SixDirection){
        if(direction === FORWARD){
            agent.place("back", 1)
        }else{
            player.say("Seems like the agent can only mark facing forward of the bookshelf")
        }
    }
}
```

```ghost
for (let count = 0;count < 5;count++){
    if (agent.found_book(FORWARD)){
        agent.mark_book(FORWARD)
    }
    agent.move(UP, 1)
}
```

```template-ignore
if (agent.found_book(FORWARD) === ){
    player.say("Found the book!")
} else {
    player.say("")
}
```

## Spell book finding @showdialog

Locate the spellbook in the library that is needed by the Wizard.

![Bookshelves](https://raw.githubusercontent.com/CausewayDigital/Minecraft-EE-MakeCode/refs/heads/master/tutorials/python-islands/island-3/library/shelves.jpg)

## Scanning shelves
The library has lots of shelves of books. They all look the same... However, will we find the right book?

*"I can help with that! I have added a special function to your agent called ``||agent:agent.found_book(DIRECTION)||``. It can be used in an **if statement** to confirm if the bookshelf you are checking has the needed book on it. It returns True if the book is found or False if not." - Willow - Librarian*

**Find your agent and finish off the code provided to check the bookshelf in front of it.**

```spy
if (agent.found_book(FORWARD) == true){
    player.say("Found the book!")
} else {
    player.say("No book here!")
}
```

## Scanning an entire column of books

So that isn't the right book then... But there are plenty more bookshelves to check. You can use a ``||loops:for||``to check multiple bookshelves in 1 go!

**Count the number of bookshelves in the columns, then create a for loop using the code from the previous activity, that will check all the books in that column.**

```diffspy
if (agent.found_book(FORWARD) == true){
    player.say("Found the book!")
} else {
    player.say("No book here!")
}
---------------------------------------
for (let count = 0; count < 5; count++){
    if (agent.found_book(FORWARD) == true){
        player.say("Found the book!")
    } else {
        player.say("No book here!")
    }
    agent.move(UP, 1)
}
```

## Marking the shelf

Once you have found the book, you need to mark that shelf so the librarian can get you the book.

The librarian has added another function to the agent, ``||agent:agent.mark_book(DIRECTION)||``, which should be run on the shelf your agent has found the book on.


```diffspy
for (let count = 0; count < 5; count++){
    if (agent.found_book(FORWARD) == true){
        player.say("Found the book!")
    } else {
        player.say("No book here!")
    }
    agent.move(UP, 1)
}
---------------------------------------
for (let count = 0; count < 5; count++){
    if (agent.found_book(FORWARD) == true){
        player.say("Found the book!")
        agent.mark_book(FORWARD)
    } else {
        player.say("No book here!")
    }
    agent.move(UP, 1)
}
```

## Getting the book

Once you have marked the shelf, walk back over to the librarian and ask her to get the book for you. Be careful though to make sure it is the correct shelf, as the librarian is very busy.
