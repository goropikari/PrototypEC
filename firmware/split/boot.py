import board
import storage
import digitalio
import supervisor
import usb_cdc
import os

supervisor.runtime.next_stack_limit = 4096 + 4096
supervisor.runtime.autoreload = False

# if os.getenv('DEBUG') != 1:
#     usb_cdc.disable()

# GP26 を VCC に短絡するとストレージとして認識される
reset = digitalio.DigitalInOut(board.GP26)
reset.pull = digitalio.Pull.DOWN
if not reset.value:
    storage.disable_usb_drive()
