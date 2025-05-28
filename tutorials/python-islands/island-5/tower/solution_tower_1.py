def build_tower():
    for i in range(0, 15):
        agent.move(UP, 1)
        agent.draw_square(3)

# Write your code above this line
telescope.start_building()
