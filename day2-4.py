# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:30:26 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    
    x,y,z = mc.player.getTilePos()  
    mc.setBlock(x,y,z-1,46)