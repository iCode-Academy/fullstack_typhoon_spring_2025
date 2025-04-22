# File write

# Write one
file = open('output.txt', 'w')
file.write('Hello World')
file.close()

# write two
file = open('output.txt', 'w')
file.writelines(['Line 1\n', 'Line 2\n', 'Line 3\n'])
file.close()

# write three - append
file = open('log.txt', 'a')
file.write('New Log Entry \n')
file.close()
