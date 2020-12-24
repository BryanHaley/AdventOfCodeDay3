# open the data files
data_file = open("data.txt", "r")

# read the data into a string
data = data_file.read()

# close the file as we now have its data in memory and no longer need it
data_file.close()

# count the number of rows in the data
num_rows = data.count("\n") + 1

# count the number of columns in the data
num_cols = data.find("\n")

def find_tree_hits(data, slope_x, slope_y):
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
        curr_index = curr_x+(curr_y*(num_cols+1)) # compensate for new line characters by adding 1 to num_cols 

        if curr_index > len(data)-1:
            break

        # check if there's a tree here
        if data[curr_index] == '#':
            num_trees_hit += 1

    return num_trees_hit

hits  = find_tree_hits(data,1,1)
hits *= find_tree_hits(data,3,1)
hits *= find_tree_hits(data,5,1)
hits *= find_tree_hits(data,7,1)
hits *= find_tree_hits(data,1,2)

# print the answer to console
print(hits)