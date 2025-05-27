while agent.inspect(AgentInspection.BLOCK, FORWARD) == AIR:
    agent.move(FORWARD, 1)
    agent.place(DOWN)
player.say("I've reached the end")
