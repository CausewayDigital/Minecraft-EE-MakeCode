# This moves to, tills, and places the seeds for the first point.
agent.move(LEFT, 3)
agent.till(DOWN)
agent.place(DOWN)

# This does the second point assuming the agent starts at the first point.
agent.move(RIGHT, 3)
agent.move(FORWARD, 1)
agent.till(DOWN)
agent.place(DOWN)

# This does the third and final point assuming the agent starts at the second point.
agent.move(RIGHT, 4)
agent.move(FORWARD, 1)
agent.till(DOWN)
agent.place(DOWN)
