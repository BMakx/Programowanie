import time
string = "Cześć jak masz na imie? "
for i in string:

    print(i, end='', flush=True)
    time.sleep(0.1)

name = input()
n_string = "Miło mi Cię poznać " + name + "!"
for i in n_string:

    print(i, end='', flush=True)
    time.sleep(0.1)

