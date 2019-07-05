'''
Script to demonstrate how to write files locally in Python3
'''

# Create a file handler (fh) and open it for appending
fh = open('output1', 'a')

# Create a variable for a counter and assign a value
counter = 1

# Start a loop to cycle through numbers
while counter < 10:

    fh.write('{0}\n'.format(str(counter)))
    counter += 1

fh.close()