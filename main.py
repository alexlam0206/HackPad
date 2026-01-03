import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.handlers.sequences import simple_key_sequence

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

keyboard.row_pins = (board.GP0, board.GP2)          # Bottom row: SW2, SW4, SW6
keyboard.col_pins = (board.GP7, board.GP1, board.GP4)           # Top row: SW1, SW3, SW5
keyboard.diode_orientation = keyboard.DIODE_COL2ROW

# Mac shortcuts
CMD_H = simple_key_sequence((KC.LCMD, KC.H))
CMD_W = simple_key_sequence((KC.LCMD, KC.W))

keyboard.keymap = [
    [CMD_H, KC.UP, CMD_W],      # Top row
    [KC.LEFT, KC.DOWN, KC.RIGHT] # Bottom row
]

if __name__ == "__main__":
    keyboard.go()
