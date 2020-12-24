# why doesn't python have real constants this is dumb
slope_x = 3
slope_y = 1

# open the data files
data_file = open("data.txt", "r")
output_file = open("output.txt", "w")

# read the data into a string
data = data_file.read()

# close the file as we now have its data in memory and no longer need it
data_file.close()

# count the number of rows in the data
num_rows = data.count("\n") + 1

# count the number of columns in the data
num_cols = data.find("\n")

# remove superfluous new line characters from string
data = data.replace("\n", "")

curr_index = 0
curr_x = 0
curr_y = 0
num_trees_hit = 0

# loop through the data
while 1:
    # move our current location
    curr_x += slope_x
    curr_y += slope_y

    # wrap around x if we exceed num_col
    if curr_x >= num_cols: # this would break if slope_x > num_cols but oh well
        curr_x -= num_cols

    # translate coordinates into an index in the string
    curr_index = curr_x+(curr_y*num_cols)

    if curr_index > len(data)-1:
        break

    # check if there's a tree here
    if data[curr_index] == '#':
        num_trees_hit += 1
        # replace the cell with X or O for visualization
        data = data[:curr_index] + "X" + data[curr_index + 1:]
    else:
        data = data[:curr_index] + "O" + data[curr_index + 1:]


# print the answer to console
print(num_trees_hit)

# write the data back out to the output file for visualization purposes
# put the newlines back in
curr_index = num_cols
while 1:
    data = data[:curr_index] + "\n" + data[curr_index:]
    curr_index += num_cols+1
    if curr_index > len(data):
        break

# write to file
output_file.write(data)
output_file.close()