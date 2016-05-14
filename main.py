import subprocess
import codecs
import psutil
import shutil
import sys
import os

#  check if DediProg GUI software is running, otherwise script will hang
for p in psutil.process_iter():
    try:
        if p.name() == 'dedipro.exe':
            print('DediProg GUI software is running!!!')
            print('Please close the application before running this script')
            print('\npress any key to quit')
            input()
            quit()
    except psutil.Error:
        pass

do = True
new_mac = '888888888788'
tmp_path = r'' + os.environ['TEMP']

if len(sys.argv) == 1:
    print('No path to bios provided, press any key to quit')
    input()
    quit()

while do:
    print('Enter new MAC address (type "quit" to exit)')
    new_mac = input()
    if new_mac == 'quit':
        quit()
    elif len(new_mac) < 12:
        print('Bad MAC address, try again, or type "quit" to exit')
    elif len(new_mac) == 12 and new_mac != 'quit':
        do = False

temp_bios = os.path.join(tmp_path, 'temp_bios.spi')
shutil.copy2(sys.argv[1], temp_bios)

with open(temp_bios, 'r+b') as f:
    f.seek(0x00001000)
    mac = int(codecs.encode(f.read(6), 'hex'), 10)
    if mac == 888888888788:
        print('\n\nWill burn bios file with MAC: %s\n\n' % new_mac)
        f.seek(0x00001000)
        f.write(bytes.fromhex(new_mac))
    else:
        print('MAC address is not in the expected position, stopping operation\npress any key to quit')
        input()
        quit()

write_bios = subprocess.Popen(['cmd.exe', '/c', 'dpcmd.exe', '-d', '-e', '-p', temp_bios, '-v'], shell=True)
write_bios.wait()
os.remove(temp_bios)
