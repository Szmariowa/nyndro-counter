# nyndro counter
import os.path


if os.path.isfile("countery_users.txt"):
    open_file = open("countery_users.txt", "r")
    for x in open_file:
        print(x)

    open_file.close()
