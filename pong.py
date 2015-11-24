#!/usr/bin/env python

from blinkenlights import setup, cleanup
from fourleds import light, clear
from time import sleep
import random

pins = [37, 33, 31, 29, 36, 32, 22, 18]
#       yp  ym  gp  gm  rp  rm  bp  bm

setup(pins)
clear(pins)
for i in pins:
    light(i)
    sleep(0.1)
    clear(pins)

class Ball:
    def __init__(self, LL, UL, LR, UR):
        self.field = [[LL, UL], [LR, UR]]
        self.field_pins = [LL, UL, LR, UR]
        self.x = random.randint(0,1)
        self.y = random.randint(0,1)
        clear(self.field_pins)
        light(self.field[self.x][self.y])
    def hit(self):
        self.x = self.x ^ 1 # go to opposite side
        self.y = random.randint(0,1)
        clear(self.field_pins)
        light(self.field[self.x][self.y])
        sleep(1)
    def miss(self):
        clear(self.field_pins)
        for i in range(4):
            light(self.field_pins)
            sleep(0.2)
            clear(self.field_pins)
            sleep(0.2)
    def swing_by(self, player):
        if player.y == self.y:
            self.hit()
            return True
        else:
            self.miss()
            return False

class Player:
    def __init__(self, low, high):
        self.range = [low, high]
        self.y = random.randint(0,1)
        clear(self.range)
        for i in range(6):
            light(self.range[self.y])
            sleep(0.1)
            clear(self.range)
            sleep(0.1)
        light(self.range[self.y])
    def move(self, direction):
        assert (direction==0 or direction==1)
        self.y = direction
        clear(self.range)
        light(self.range[self.y])

myball = Ball(33, 29, 32, 18)
p1 = Player(37, 31)
p2 = Player(36, 22)

order = []
if myball.x == 0:
    order = [p1, p2]
else:
    order = [p2, p1]

for i in range(5):
    order[0].move(myball.y) # auto move
    sleep(0.5)
    myball.swing_by(order[0])
    order[1].move(myball.y) # auto move
    sleep(0.5)
    myball.swing_by(order[1])

order[0].move(myball.y ^ 1) # auto fail
sleep(0.5)
myball.swing_by(order[0])

cleanup()
