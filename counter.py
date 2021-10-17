# nyndro counter
import os.path

if os.path.isfile("countery.txt"):
    open_file = open("countery.txt", "r")

    counter_current = int(open_file.readline())
    counter_goal = int(open_file.readline())
    
    open_file.close()
else:
    counter_current = 0
    counter_goal = 100_000
    

def show_how_many_done():
    print("Stan obecny", counter_current)
    

def show_how_many_left():
    print("Pozostało", counter_goal)
    

def add_number():
    global counter_current
    global counter_goal

    print("Podaj ile zrobiłaś")
    number = input()

    if number.isnumeric():
        counter_current = counter_current + int(number)
        counter_goal = counter_goal - int(number)

        save_file = open("countery.txt", "w")
        save_file.write(str(counter_current) + "\n")
        save_file.write(str(counter_goal))
        save_file.close()

    else:
        print("To nie jest liczba")


show_how_many_done()
show_how_many_left()
add_number()
show_how_many_done()
show_how_many_left()

input('Naciśnij ENTER aby wyjść')


