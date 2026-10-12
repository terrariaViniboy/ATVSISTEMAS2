import threading
import time

contador = 0

def Joao():
    global contador

    for i in range(5):
        contador += 1
        print(f"João realizou uma tarefa. Total = {contador}")
        time.sleep(1)

def Maria():
    global contador

    for i in range(5):
        contador += 1
        print(f"Maria realizou uma tarefa. Total = {contador}")
        time.sleep(1)

t1 = threading.Thread(target=Joao)
t2 = threading.Thread(target=Maria)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Total Final:", contador)
