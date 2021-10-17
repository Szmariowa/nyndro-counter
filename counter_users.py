# nyndro counter
import os.path

x = Justyna, Michał, Jaskier
users = x.split(",")
print(users)

if os.path.isfile("countery_users.txt"):
    open_file = open("countery_users.txt", "r")

    counter_current_Justyna = int(open_file.readline())
    counter_goal_Justyna = int(open_file.readline())

    counter_current_Michał = int(open_file.readline())
    counter_goal_Michał = int(open_file.readline())

    counter_current_Jaskier = int(open_file.readline())
    counter_goal_Jaskier = int(open_file.readline())
    
    open_file.close()
else:
    counter_current_Justyna = 0
    counter_goal_Justyna = 100_000

    counter_current_Michał = 0
    counter_goal_Michał = 100_000

    counter_current_Jaskier = 0
    counter_goal_Jaskier = 100_00

def show_how_many_done():
    print("Stan obecny", counter_current_Justyn)
    

def show_how_many_left():
    print("Pozostało", counter_goal_Justyn)