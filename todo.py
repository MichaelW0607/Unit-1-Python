todos = []
while True:
    print("your todos are:")
    print(todos)
    x=input("what todo would you like to add?")
    todos.append(x)
    my_todo = open["todo.txt", "a"]
    my_todo.write(x,"\n")
    my_todo.close()
    my_todo = open("todo.txt")
