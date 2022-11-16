my_list = [ "cars","sports","food","music","excercises"]
print(my_list)
# creation of my first list
my_list.append("drinks")
print(my_list)
print(my_list[3])
print(my_list[-1])
my_list[0] = "movies"
print(my_list)
del my_list[2]
print(my_list)
my_tuple = ("pizza","hotdogs","tacos","steak","soup")
# creating my tuple list
print(my_tuple)
print(len(my_list))
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
second_list = ["apples","bananas","oranges","peaches","tangerines"]
# creation of my second list
print(my_list + second_list)
print(">".join(my_list + second_list))
names= "anna,wesley,saint".split(",")
print(names)