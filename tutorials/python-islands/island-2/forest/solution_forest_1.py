for i in range(5):
    if not agent.is_nest():
        agent.harvest()
    agent.next_location()
