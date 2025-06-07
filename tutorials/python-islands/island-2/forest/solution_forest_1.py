# Run 5 times (one for each nest)
if agent.is_nest():
    agent.next_location()
else:
    agent.harvest()
    agent.next_location()
