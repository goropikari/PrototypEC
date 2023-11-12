import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap, HoldTapRepeat
from kmk.handlers.sequences import send_string
from kmk.modules.mouse_keys import MouseKeys
import scanner
import os

keyboard = KMKKeyboard()

low_threshold = 1.7
high_threshold = 2

S1 = 0
S2 = 1
S3 = 2
S4 = 3
S5 = 4
S6 = 5
S7 = 6
S8 = 7

row_pins = (board.GP5, board.GP4, board.GP3, board.GP2)
adc_port = board.GP28
discharge_port = board.GP14
mux_sels = (board.GP8, board.GP7, board.GP6)
col_channels = [S6, S4, S1, S2, S3]
data_pin = board.GP15


tap_time = 125

keyboard.modules.append(MouseKeys())

holdtap = HoldTap()
holdtap.tap_time = tap_time
holdtap.prefer_hold = False
keyboard.modules.append(holdtap)

layer = Layers()
layer.tap_time = tap_time
layer.prefer_hold = True
keyboard.modules.append(layer)

keyboard.coord_mapping = [
      0,  1,  2,  3,  4,
      5,  6,  7,  8,  9,
     10, 11, 12, 13, 14,
     15, 16, 17, 18, 19,
]

##################################
# keymap
##################################
N00 = send_string("00")

keyboard.keymap = [
    # default layer
    [
        KC.P7   , KC.P8 , KC.P9     , KC.PSLS, KC.TG(1) ,
        KC.P4   , KC.P5 , KC.P6     , KC.PAST, KC.NLCK  ,
        KC.P1   , KC.P2 , KC.P3     , KC.PMNS, KC.PEQL  ,
        KC.P0   , N00   , KC.PDOT   , KC.PPLS, KC.PENT
    ],
    # mouse layer
    [
        KC.MW_UP, KC.NO    , KC.MB_MMB , KC.NO     , KC.TG(1),
        KC.MW_DN, KC.MB_LMB, KC.MS_UP  , KC.MB_RMB , KC.TAB,
        KC.MW_LT, KC.MS_LT , KC.MS_DN  , KC.MS_RT  , KC.LSFT,
        KC.MW_RT, KC.NO    , KC.NO     , KC.NO     , KC.PENT
    ],
]

keyboard.matrix = scanner.ECMatrixScanner(
    col_channels=col_channels,
    rows=row_pins,
    mux_sels=mux_sels,
    adc_port=adc_port,
    discharge_port=discharge_port,
    low_threshold=low_threshold,
    high_threshold=high_threshold,
    debug=os.getenv('DEBUG', 0) == 1,
)

if __name__ == '__main__':
    keyboard.go()
