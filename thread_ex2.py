import threading


def soma():
    soma = 0
    for i in range(20):
        soma += 1
    print(threading.current_thread().getName(), 'soma ', soma)

lista_threads = list()

for t in range(5):
    th = threading.Thread(target=soma,name='Threading'+str(t))
    lista_threads.append(th)
    th.start()

for thread in lista_threads:
    thread.join()