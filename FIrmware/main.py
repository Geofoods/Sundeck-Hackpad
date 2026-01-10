# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here! (added two more pins)
PINS = [board.D3, board.D4, board.D2, board.D1, board.D5, board.D6]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
keyboard.keymap = [
    [
        KC.MPLY,  # button 1: Play/Pause toggle (media key)
        KC.Macro( # button 2: open Spotify
            Press(KC.LGUI), Tap(KC.S), Release(KC.LGUI),
            Tap(KC.S), Tap(KC.P), Tap(KC.O), Tap(KC.T),
            Tap(KC.I), Tap(KC.F), Tap(KC.Y), Tap(KC.ENTER)
        ),
        KC.Macro( # button 3: take screenshot
            Press(KC.LGUI), Press(KC.LSFT), Tap(KC.S), Release(KC.LSFT), Release(KC.LGUI)
        ),
        KC.Macro( # button 4: open VS Code
            Press(KC.LGUI), Tap(KC.S), Release(KC.LGUI),
            Tap(KC.C), Tap(KC.O), Tap(KC.D), Tap(KC.E), Tap(KC.ENTER)
        ),
        KC.Macro( # button 5: open new tab (Ctrl+T)
            Press(KC.LCTRL), Tap(KC.T), Release(KC.LCTRL)
        ),
        KC.Macro( # button 6: Alt+Tab (switch windows)
            Press(KC.LALT), Tap(KC.TAB), Release(KC.LALT)
        ),
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()