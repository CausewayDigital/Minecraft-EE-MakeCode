def on_forever():
    blocks.replace(ICE,
        blocks.block_by_id(LAKE_WATER),
        pos_camera(-1, -1, -1),
        pos_camera(1, -1, 1))
loops.forever(on_forever)
