# nyndro counter
import os.path


if os.path.isfile("countery_users.txt"):
    open_file = open("countery_users.txt", "r")
    

    for x in open_file:
        data = x.strip().split(',')
        print(data[0])
     

    open_file.close()




