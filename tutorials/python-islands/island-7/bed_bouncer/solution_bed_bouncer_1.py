def on_jump():
    if blocks.test_for_block(BED, player.position()):
        mobs.apply_effect(LEVITATION, mobs.target(NEAREST_PLAYER), 2, 1)
        mobs.apply_effect(REGENERATION, mobs.target(NEAREST_PLAYER), 3, 2)

player.on_travelled(BOUNCE, on_jump)
