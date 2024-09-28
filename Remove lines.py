# Program to remove any file with any prefix

file1 =open('Codingal.txt',
            'r')
file2 = open('Codingal.txt',
            'w')

#reading each line from the original       
#text file
for line in file1.readlines():

    #reading all lines that do not
    #begin with "Coding"
    if not (line.statyswith('Coding')):

        #printing those lines
        print(line)

        #storing only those lines that
        # do not begin with "Coding"'
        file2.write(line)

# close and save the files
file2.close()
file1.close()
