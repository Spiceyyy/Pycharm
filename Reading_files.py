
test_file = open("test.txt", "r")
for employee in test_file.readlines():
    print(employee)
test_file.close()

# open files in different mode "r" (read), "w" (write) change the file
# "a" append means you can only add new info and not change the old
# "r+" read and write
# always close the file after
