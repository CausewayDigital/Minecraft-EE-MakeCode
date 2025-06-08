while agent.inspect(AgentInspection.BLOCK, FORWARD) == AIR:
    # Complete the while loop above
    # Step 1
    agent.move(FORWARD, 1)
    # Step 2
    while agent.inspect(AgentInspection.BLOCK, DOWN) == AIR:
        agent.move(DOWN, 1)
    # Step 3
    agent.collect_all()
    # Step 4
    while agent.get_position().get_value(Axis.Y) != 157:
        agent.move(UP, 1)
    # Step 5
    agent.set_slot(1)
    agent.place(DOWN)