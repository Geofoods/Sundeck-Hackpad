import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler 

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

# --- Rotary encoder setup (A=GP26, B=GP28) ---
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# One encoder: (A, B)
encoder_handler.pins = (
    (board.GP26, board.GP28),
)

encoder_handler.map = (
    ((KC.VOLD, KC.VOLU),),
)

# --- Buttons (your existing 6 digital pins) ---
PINS = [board.D3, board.D4, board.D2, board.D1, board.D5, board.D6]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Define macros
macros.add_record(KC.MACRO_1, [
    Press(KC.LGUI), Tap(KC.S), Release(KC.LGUI),
    Tap(KC.S), Tap(KC.P), Tap(KC.O), Tap(KC.T),
    Tap(KC.I), Tap(KC.F), Tap(KC.Y), Tap(KC.ENTER)
])

macros.add_record(KC.MACRO_2, [
    Press(KC.LGUI), Press(KC.LSFT), Tap(KC.S), Release(KC.LSFT), Release(KC.LGUI)
])

macros.add_record(KC.MACRO_3, [
    Press(KC.LCTRL), Tap(KC.T), Release(KC.LCTRL)
])

macros.add_record(KC.MACRO_4, [
    Press(KC.LALT), Tap(KC.TAB), Release(KC.LALT)
])

keyboard.keymap = [
    [
        KC.MPLY,      # button 1: Play/Pause
        KC.MACRO_1,   # button 2: open Spotify
        KC.MACRO_2,   # button 3: screenshot
        KC.MUTE,      # button 4: mute/unmute
        KC.MACRO_3,   # button 5: Ctrl+T
        KC.MACRO_4,   # button 6: Alt+Tab
    ]
]

if __name__ == '__main__':
    keyboard.go()
