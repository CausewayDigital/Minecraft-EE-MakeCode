# Run four times (one for each seed)
agent.move(FORWARD, 3)
block = agent.inspect(AgentInspection.BLOCK, DOWN)
if block == WHEAT:
    agent.approve()
else:
    agent.reject()

