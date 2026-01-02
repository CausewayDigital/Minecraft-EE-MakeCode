agent.set_item(STONE, 64, 1)
agent.set_slot(1)

for i in range(19):
    agent.destroy(FORWARD)
    agent.move(FORWARD, 1)
    agent.destroy(UP)

    block = agent.inspect_block(DOWN)

    if block == CAVE_LAVA:
        agent.place(DOWN)
        