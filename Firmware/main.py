import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.handlers.sequences import simple_key_sequence
+from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.SCL, board.TX, board.RX, board.SCK, board.MISO, board.MOSI]
keyboard.matrix = KeysScanner(pins=PINS, value_when_pressed=False)
# Mac shortcuts
CMD_H = simple_key_sequence((KC.LCMD, KC.H))
CMD_W = simple_key_sequence((KC.LCMD, KC.W))

keyboard.keymap = [
    [CMD_H, KC.UP, CMD_W],      # Top row
    [KC.LEFT, KC.DOWN, KC.RIGHT] # Bottom row
]

if __name__ == "__main__":
    keyboard.go()
