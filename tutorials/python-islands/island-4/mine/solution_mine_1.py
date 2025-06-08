found_diamond = 0
while found_diamond < 3:
    if agent.check_ore(FORWARD) == DIAMOND_ORE:
        agent.mark_diamond()
        found_diamond = found_diamond + 1
    else:
        agent.mark_bin()