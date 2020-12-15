import os
import re

button_mapping = {
    'Button 1': 'key ctrl c',
    'Button 2': 'key ctrl v',
    'Button 3': 'key ctrl z',
    'Button 8': 'button 4',
    'Button 9': 'button 5'

}


# Shows which screens are available.
# This function is not needed for the program to work.
def get_displays():
    output = os.popen('xrandr').read().splitlines()
    displays = [line.split()[0] for line in output if " connected " in line]
    print(displays)


def find_device_id(device_name):
    output = os.popen('xsetwacom  --list devices').read()
    devices = output.split('\n')

    for item in devices:
        if item.find(device_name) > 0:
            return re.search('id: \d{1,3}', item).group().replace('id: ', '')


def set_stylus_display_area(device_id, display_name):
    print('xsetwacom set ' + device_id + ' MapToOutput ' + display_name)
    os.system('xsetwacom set ' + device_id + ' MapToOutput ' + display_name)


def set_tablet_buttons(device_id):
    for button in button_mapping:
        print('xsetwacom set ' + device_id + ' ' + button + ' ' + button_mapping[button])
        os.system('xsetwacom set ' + device_id + ' ' + button + ' ' + button_mapping[button])


def main():
    get_displays()

    stylus_id = find_device_id("stylus")
    if stylus_id:
        set_stylus_display_area(stylus_id, 'DisplayPort-0')
    pad_id = find_device_id("pad")
    if pad_id:
        set_tablet_buttons(pad_id)


if __name__ == '__main__':
    main()

