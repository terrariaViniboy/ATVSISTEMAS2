
import threading
import time

def acessar_recurso(nome_thread):
    
    try:
        with open("status.txt", "r") as f:
            valor = f.read().strip()
    except FileNotFoundError:
        with open("status.txt", "w") as f:
            f.write("0")
        valor = "0"

    if valor == "0":
        print(f"[{nome_thread}] Recurso disponível. Reservando recurso...")
        
        with open("status.txt", "w") as f:
            f.write("1")
            
        print(f"[{nome_thread}] Utilizando recurso...")
        
        time.sleep(2) 
        
        print(f"[{nome_thread}] Liberando recurso...")
        
        with open("status.txt", "w") as f:
            f.write("0")
            
        print(f"[{nome_thread}] Recurso liberado com sucesso!")

    
    elif valor == "1":
        print(f"[{nome_thread}] Recurso ocupado. Tente novamente mais tarde.")
        
    
    else:
        print(f"[{nome_thread}] Valor inválido no arquivo.")


with open("status.txt", "w") as f:
    f.write("0")

t1 = threading.Thread(target=acessar_recurso, args=("Thread-1",))
t2 = threading.Thread(target=acessar_recurso, args=("Thread-2",))


t1.start()
time.sleep(0.5) 
t2.start()

t1.join()
t2.join()

print("Execução finalizada.")