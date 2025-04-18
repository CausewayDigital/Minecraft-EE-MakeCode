# Ran 5 times
if agent.is_nest():
    agent.next_location()
else:
    agent.harvest()
    agent.next_location()