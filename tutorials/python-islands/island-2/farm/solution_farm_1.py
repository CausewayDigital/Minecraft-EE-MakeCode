for i in range(4):
    agent.move(FORWARD, 3)
    block = agent.inspect(AgentInspection.BLOCK, DOWN)
    if block == WHEAT:
        agent.approve()
    else:
        agent.reject()
