#!/usr/bin/env python3
from mcpi.minecraft import Minecraft
from mcpi import block
#################################################
def init():
    mc = Minecraft.create()
    x, y, z = mc.player.getTilePos()
    if z > 70:
        # We need room along the z axis for the steet
        z = 70

    mc.setBlocks(x-15, -1, z+999, x+999, -1, z+999, block.DIAMOND.id)

    return mc

