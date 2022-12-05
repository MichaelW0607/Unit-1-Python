my_file = open("michael.txt", "r+")
#print(my_file.readlines())
#print("hello")
#print("world")
for line in my_file.readlines():
    print(line, end ="")
my_file.writelines(["im writing from python"])