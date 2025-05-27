agent.move(FORWARD, 1)

for i in range(3):
    for j in range(3):
        agent.destroy(DOWN)
        agent.move(DOWN, 1)

    if agent.inspect(AgentInspection.BLOCK, FORWARD) == GOLD_ORE:
        agent.destroy(DOWN)

    agent.move(UP, 3)
    agent.move(FORWARD, 2)

agent.move(BACK, 3)
agent.move(LEFT, 3)

for i in range(3):
    for j in range(3):
        agent.destroy(DOWN)
        agent.move(DOWN, 1)

    if agent.inspect(AgentInspection.BLOCK, FORWARD) == GOLD_ORE:
        agent.destroy(DOWN)

    agent.move(UP, 3)
    agent.move(BACK, 2)
