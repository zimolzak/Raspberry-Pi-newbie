#!/usr/bin/env python

""" A simple Pong game played with eight LEDs.

Imagine a 2 row by 4 column LED array. Player 1 can move up and down
in column 1. The ball is any of the four LEDs in columns 2-3. Player 2
can move up and down in column 4.

.  b  .  p2
p1 .  .  .
"""

from blinkenlights import setup, cleanup
from fourleds import light, clear
from time import sleep
import random

pins = [37, 33, 31, 29, 36, 32, 22, 18]
#       yp  ym  gp  gm  rp  rm  bp  bm

setup(pins)

### Test pattern

clear(pins)
for i in pins:
    light(i)
    sleep(0.1)
    clear(pins)

#### Definitions

class Ball:
    def __init__(self, LL, UL, LR, UR):
        self.field = [[LL, UL], [LR, UR]]
        self.field_pins = [LL, UL, LR, UR]
        self.x = random.randint(0,1)
        self.y = random.randint(0,1)
        clear(self.field_pins)
        light(self.field[self.x][self.y])
    def hit(self):
        self.x = self.x ^ 1 # always go to opposite side
        self.y = random.randint(0,1)
        clear(self.field_pins)
        light(self.field[self.x][self.y])
        sleep(1)
    def miss(self):
        clear(self.field_pins)
        for i in range(4): ### blink the whole field
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

def imperfect(player, ball, success_rate=0.99):
    assert 0 <= success_rate <= 1
    if random.uniform(0,1) < success_rate:
        player.move(ball.y)
    else:
        player.move(ball.y ^ 1)

#### Set up the global variables

myball = Ball(33, 29, 32, 18)
p1 = Player(37, 31)
p2 = Player(36, 22)
winner = None

order = []
if myball.x == 0:
    order = [p1, p2]
else:
    order = [p2, p1]

#### Main game loop

while True:
    imperfect(order[0], myball)
    sleep(0.5)
    inplay = myball.swing_by(order[0])
    if not inplay:
        winner = order[1]
        break
    imperfect(order[1], myball)
    sleep(0.5)
    inplay = myball.swing_by(order[1])
    if not inplay:
        winner = order[0]
        break

### A little victory dance

clear(pins)
for i in range(25):
    winner.move(0)
    sleep(0.2)
    winner.move(1)
    sleep(0.2)

cleanup()
