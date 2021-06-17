from collections import namedtuple

# line's structure
Pos = namedtuple('pos', ['x1', 'y1', 'x2', 'y2'])
Line = namedtuple('line', ['pos', 'type', 'name'])
