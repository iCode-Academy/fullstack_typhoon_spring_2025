# File Meta Data
import os

if os.path.exists('advanced.txt'):
    size = os.path.getsize('advanced.txt')
    print(size)

    # get modification time
    mod_time = os.path.getmtime('advanced.txt')
    print(mod_time)
    os.rename('advanced.txt', 'new_advanced.txt')
    print('renamed')
    os.remove('new_advanced.txt')
    print('removed')

