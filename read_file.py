'''
Script to demonstrate how to read files locally
'''

# Create a file handler (fh) and read in a certain file
fh = open('read_file.py', 'r')

# Create a variable for a counter and assign a value
counter = 1

# Start a for loop to iterate over all the contents of the fh
for line in fh.readlines():

    # For each line, we 'strip()' off the end return characters
    # then print it to the console using the value of the 
    # counter variable as a line number
    print('{0} : {1}'.format(counter, line.strip()))
    
    # Increment the counter variable by 1
    counter += 1