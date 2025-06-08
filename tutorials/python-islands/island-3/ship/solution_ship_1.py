# Use the whistle to get your agent to the block just in front of the hatches
# Run the code (repeat for each row of hatches)
for count in range(6):
    agent.move(FORWARD, 1)
    agent.place(DOWN)