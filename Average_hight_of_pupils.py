# Implementing the task
# Find out the average hight of pupils from each class

# Creating the function to update dictionary
def u_d(d, key, value):
    if key in d:
        d[key][0] += value
        d[key][1] += 1
    else:
        d[key] = [value, 1]
    return d

# Reading the file and putting data to the dictionary
a = {}
string = ''
with open('dataset_3380_5.txt') as inf:
    for line in inf:
        string = line.split() # It is important to use split() in order to write the words in the string as separate elements but not the letters
        u_d(a, int(string[0]), int(string[2]))

# Showing the average hight from each class out of all pupils
for i in range(1, 12):
    if i in a:
        print(i, a[i][0] / a[i][1])
    else:
        print(i, '-')
print(a)

