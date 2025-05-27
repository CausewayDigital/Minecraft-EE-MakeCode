for i in range(8):
    agent.move(FORWARD, 1)
    block = agent.inspect(AgentInspection.BLOCK, DOWN)
    if block == WHEAT:
        agent.destroy(DOWN)
        agent.place(DOWN)
    elif block == AIR:
        agent.place(DOWN)

agent.move(LEFT, 1)
if block == WHEAT:
    agent.destroy(DOWN)
    agent.place(DOWN)
elif block == AIR:
    agent.place(DOWN)

for i in range(7):
    agent.move(BACK, 1)
    block = agent.inspect(AgentInspection.BLOCK, DOWN)
    if block == WHEAT:
        agent.destroy(DOWN)
        agent.place(DOWN)
    elif block == AIR:
        agent.place(DOWN)

agent.move(LEFT, 1)
if block == WHEAT:
    agent.destroy(DOWN)
    agent.place(DOWN)
elif block == AIR:
    agent.place(DOWN)

for i in range(7):
    agent.move(FORWARD, 1)
    block = agent.inspect(AgentInspection.BLOCK, DOWN)
    if block == WHEAT:
        agent.destroy(DOWN)
        agent.place(DOWN)
    elif block == AIR:
        agent.place(DOWN)
