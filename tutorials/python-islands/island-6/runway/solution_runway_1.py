runway_design = runway.get_runway_design()
for row in runway_design:
    for block in row:
        if block:
            agent.set_slot(1)
            agent.place(DOWN)
        agent.move(RIGHT, 1)
    agent.move(FORWARD, 1)
    agent.return_agent()
