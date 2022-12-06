my_file = open("michael.txt", "a")
#print(my_file.readlines())
#print("hello")
#print("world")
my_file.write("im writing from python\n")
my_file.close()
my_file=open("michael.txt")
for line in my_file.readlines():
    print(line, end ="")
    