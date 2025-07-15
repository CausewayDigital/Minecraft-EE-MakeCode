\### @flyoutOnly true

\### @diffs true

\### @hideDone true

\### @codeStart players set @s codeExecution 1

\### @codeStop players set @s codeExecution 0





\# Lawnmower

Tell your friend what to do

```template

lawnmower.start()



while (true) {

&nbsp;   if (lawnmower.isHouseInFront()) {



&nbsp;   } else if (lawnmower.isAtEndOfGarden()) {



&nbsp;   } else if (lawnmower.goalPostInFront()) {



&nbsp;   } else {



&nbsp;   }

}

```



```customts

//% color=green weight=100 icon="\\uf085"

namespace lawnmower {



&nbsp;   //% block="Start Lawnmower"

&nbsp;   export function start() {

&nbsp;   }



&nbsp;   //% block="Move Lawnmower Forwards"

&nbsp;   export function move\_forward() {

&nbsp;       if (checkInBounds()) {

&nbsp;           agent.move(FORWARD, 1)

&nbsp;       } else {

&nbsp;           player.say("You take the lawnmower out of the garden!")

&nbsp;       }

&nbsp;   }



&nbsp;   export function getBlockInFrontCoord(): Position {

&nbsp;       let agentPos = agent.getPosition()

&nbsp;       let facingDirection = agent.getOrientation()



&nbsp;       switch (facingDirection) {

&nbsp;           case 0: {

&nbsp;               return positions.add(agentPos, pos(0, 0, 1));

&nbsp;               break;

&nbsp;           }

&nbsp;           case 90: {

&nbsp;               return positions.add(agentPos, pos(-1, 0, 0));

&nbsp;               break;

&nbsp;           }

&nbsp;           case -90: {

&nbsp;               return positions.add(agentPos, pos(1, 0, 0));

&nbsp;               break;

&nbsp;           }

&nbsp;           default: {

&nbsp;               return positions.add(agentPos, pos(0, 0, -1));

&nbsp;           }

&nbsp;       }

&nbsp;   }



&nbsp;   //% block="Is In Front of House"

&nbsp;   export function isHouseInFront() {

&nbsp;       let blockInFront = lawnmower.getBlockInFrontCoord()

&nbsp;       let z = blockInFront.getValue(Axis.Z)



&nbsp;       if (z < -195) {

&nbsp;           return true;

&nbsp;       } else {

&nbsp;           return false;

&nbsp;       }

&nbsp;   }



&nbsp;   //% block="Is Goal Post in the Way"

&nbsp;   export function goalPostInFront(): boolean {

&nbsp;       let blockInFront = lawnmower.getBlockInFrontCoord()



&nbsp;       let x = blockInFront.getValue(Axis.X)

&nbsp;       let z = blockInFront.getValue(Axis.Z)



&nbsp;       if ((x === -132 \&\& z === -168) || (x === -137 \&\& z === -168)) {

&nbsp;           return true;

&nbsp;       } else {

&nbsp;           return false;

&nbsp;       }

&nbsp;   }



&nbsp;   //% block="Is At End of Garden"

&nbsp;   export function isAtEndOfGarden(): boolean {

&nbsp;       let blockInFront = lawnmower.getBlockInFrontCoord()



&nbsp;       let x = blockInFront.getValue(Axis.X)

&nbsp;       let z = blockInFront.getValue(Axis.Z)



&nbsp;       if ((x <= -139 \&\& z > -175) || z > -166) { 

&nbsp;           return true;

&nbsp;       } else {

&nbsp;           return false

&nbsp;       }

&nbsp;   }



&nbsp;   export function checkInBounds() {

&nbsp;       let blockInFront = lawnmower.getBlockInFrontCoord()



&nbsp;       let x = blockInFront.getValue(Axis.X)

&nbsp;       let z = blockInFront.getValue(Axis.Z)



&nbsp;       if (x >= -145 \&\& x <= -131 \&\& z >= -195 \&\& z <= -166 \&\& !(x >= -144 \&\& x <= -139 \&\& z >= -174 \&\& z <= -166) \&\& !(x === -132 \&\& z === -168) \&\& !(x === -137 \&\& z === -168)) {

&nbsp;           return true;

&nbsp;       } else {

&nbsp;           return false;

&nbsp;       }



&nbsp;   }



&nbsp;   //% block="Turn Lawnmower $direction"

&nbsp;   export function turn(direction: TurnDirection) {

&nbsp;       switch (direction) {

&nbsp;           case (TurnDirection.Left): {

&nbsp;               agent.turnLeft();

&nbsp;               break;

&nbsp;           } case (TurnDirection.Right): {

&nbsp;               agent.turnRight();

&nbsp;               break;

&nbsp;           }

&nbsp;       }

&nbsp;   }

}

```



\## Introduction @showdialog



Let's tell your friend where to go with the lawnmower. To do this we will use codeblocks. 



So your friend knows where they need to go, you must tell them what to do if they meet certain objects such as the end of the garden or a goal post.



\## Getting to the House

When your friend gets to the house he needs to `||lawnmower:turn||` right, `||lawnmower:move||` forwards, and `||lawnmower:turn||` right again. This will line him up on the next row along ready to cut some more grass.



```block

lawnmower.turn(TurnDirection.Right)

lawnmower.move\_forward()

lawnmower.turn(TurnDirection.Right)

```



\## Getting to the end of the Garden

When your friend gets to the end of the garden, the shed or the fence, they also need to move to cut the next row of grass. Although, this time, they will need to `||lawnmower:turn||` left, `||lawnmower:move||` forwards, and `||lawnmower:turn||` left instead.



```block

lawnmower.turn(TurnDirection.Left)

lawnmower.move\_forward()

lawnmower.turn(TurnDirection.Left)

```



\## Going Around a Goalpost

When your fried gets to a goalpost they will need to go around it (the goalpost is 1 block). See if you can work out how they might do this. There is a hint if you get stuck or want to check.



```block

lawnmower.turn(TurnDirection.Right)

lawnmower.move\_forward()

lawnmower.turn(TurnDirection.Left)

lawnmower.move\_forward()

lawnmower.move\_forward()

lawnmower.turn(TurnDirection.Left)

lawnmower.move\_forward()

lawnmower.turn(TurnDirection.Right)

```



\## No Obstacles

If there are no obstacles in front of your friend, they are not at either end of the garden or a goalpost in the way, then they should just move the lawnmower forwards.



```block

lawnmower.move\_forward()

```



```ghost

lawnmower.start()



while (true) {

&nbsp;   if (lawnmower.isHouseInFront()) {

&nbsp;       lawnmower.turn(TurnDirection.Right)

&nbsp;       lawnmower.move\_forward()

&nbsp;       lawnmower.turn(TurnDirection.Right)

&nbsp;   } else if (lawnmower.isAtEndOfGarden()) {

&nbsp;       lawnmower.turn(TurnDirection.Left)

&nbsp;       lawnmower.move\_forward()

&nbsp;       lawnmower.turn(TurnDirection.Left)

&nbsp;   } if (lawnmower.goalPostInFront()) {

&nbsp;       // Go around goalpost

&nbsp;       lawnmower.turn(TurnDirection.Right)

&nbsp;       lawnmower.move\_forward()

&nbsp;       lawnmower.turn(TurnDirection.Left)

&nbsp;       lawnmower.move\_forward()

&nbsp;       lawnmower.move\_forward()

&nbsp;       lawnmower.turn(TurnDirection.Left)

&nbsp;       lawnmower.move\_forward()

&nbsp;       lawnmower.turn(TurnDirection.Right)

&nbsp;   } else {

&nbsp;       lawnmower.move\_forward()

&nbsp;   }

}

```

