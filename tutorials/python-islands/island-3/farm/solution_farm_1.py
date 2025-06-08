# Run once for each row, use the whistle to call the agent to the start of each row
for i in range(0, 8):
    agent.move(FORWARD, 1)
    block = agent.inspect(AgentInspection.BLOCK, DOWN)
    if block == WHEAT:
        agent.destroy(DOWN)
        agent.place(DOWN)
    elif block == AIR:
        agent.place(DOWN)
