from enum import Enum

class Colors(Enum):
    red = 0xE85041
    green = 0x65C97A
    blue = 0x1D6EF0
    yellow = 0xEBCE10

class Config():
    def __init__(self):
        self.colors: Colors = Colors
