#!/usr/bin/env python

import sys
from lcd import lcd_string, tn

pipe_contents = sys.stdin.read()
pipe_contents = pipe_contents.replace('\n', ' ')

lcd_string(pipe_contents, tn)
