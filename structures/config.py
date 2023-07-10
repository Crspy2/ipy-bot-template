from enum import Enum

class Colors(Enum):
    red = 0xE85041
    green = 0x65C97A
    blue = 0x1D6EF0
    yellow = 0xEBCE10

class Config():
    def __init__(self):
        self.colors: Colors = Colors
        self.price_multiplier = 2
        self.log_channel_id = 1123133377751560293
        self.sellix_product_id = "640d631074c7d"
        self.partner_discount = 0.50  # 50%
